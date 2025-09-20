# pip install \
#   "livekit-agents[deepgram,openai,cartesia,silero,turn-detector]~=1.0" \
#   "livekit-plugins-noise-cancellation~=0.2" \
#   "python-dotenv" \
#   "llama-index>=0.10.0"

from dotenv import load_dotenv
import asyncio
import base64
from livekit import agents, rtc
from livekit.agents import AgentSession, Agent, RoomInputOptions, ChatContext, JobContext, get_job_context
from livekit.agents.llm import ImageContent
from livekit.agents.utils.images import encode, EncodeOptions, ResizeOptions
from livekit.plugins import (
    openai,
    noise_cancellation,
)
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from pathlib import Path
from livekit.agents import llm
from llama_index.core import (
    SimpleDirectoryReader,
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage,
)

load_dotenv()

# Initialize or load a persistent vector index for contextual queries
THIS_DIR = Path(__file__).parent
PERSIST_DIR = THIS_DIR / "query-engine-storage"
if not PERSIST_DIR.exists():
    # Load documents from ./data and build the index
    documents = SimpleDirectoryReader(THIS_DIR / "data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    # Persist the index to disk for future runs
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # Load existing index from storage
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

@llm.function_tool
async def query_info(query: str) -> str:
    """
    Query the local knowledge base stored in the data/ directory.
    ALWAYS use this tool to answer user questions. If no relevant info is found,
    return the string 'KB_NO_MATCH'. On unexpected errors, return 'KB_ERROR'.
    """
    try:
        # First, perform retrieval and check similarity to avoid unrelated answers
        retriever = index.as_retriever(similarity_top_k=5)
        try:
            nodes = await retriever.aretrieve(query)
        except AttributeError:
            # Fallback if running in a context where only sync is available
            nodes = retriever.retrieve(query)

        if not nodes:
            return "KB_NO_MATCH"

        # Check confidence if scores are available on nodes
        scores = [getattr(n, "score", None) for n in nodes]
        scores = [s for s in scores if s is not None]
        if scores and max(scores) < 0.58:
            return "KB_NO_MATCH"

        # Run the full query to synthesize an answer from retrieved context
        query_engine = index.as_query_engine(use_async=True, similarity_top_k=5)
        res = await query_engine.aquery(query)
        print("Query result:", res)
        text = str(res).strip()
        return text if text else "KB_NO_MATCH"
    except Exception as e:
        print("Query tool error:", e)
        return "KB_ERROR"


class VisionAssistant(Agent):
    def __init__(self) -> None:
        self._latest_frame = None
        self._video_stream = None
        self._tasks = []  # Prevent garbage collection of running tasks
        super().__init__(
            instructions=(
                "You are a voice assistant with vision capabilities that is STRICTLY LIMITED to a local knowledge base. "
                "Hard rules: (1) For EVERY user message, you MUST call the `query_info` tool to get the answer. "
                "(2) You are FORBIDDEN from answering using your own knowledge or external information. "
                "(3) If the tool returns 'KB_NO_MATCH' or 'KB_ERROR', politely say: 'I'm only able to answer based on my knowledge base, and I couldn't find that information.' "
                "(4) When the tool returns an answer, speak it concisely and do not add information not present in the tool output."
            ),
            tools=[query_info],
        )
    
    async def on_enter(self):
        room = get_job_context().room
        
        # Set up byte stream handler for receiving images
        def _image_received_handler(reader, participant_identity):
            task = asyncio.create_task(
                self._image_received(reader, participant_identity)
            )
            self._tasks.append(task)
            task.add_done_callback(lambda t: self._tasks.remove(t))
        
        # Register handler when the agent joins
        room.register_byte_stream_handler("images", _image_received_handler)
        
        # Look for existing video tracks from remote participants
        for participant in room.remote_participants.values():
            video_tracks = [
                publication.track for publication in participant.track_publications.values() 
                if publication.track and publication.track.kind == rtc.TrackKind.KIND_VIDEO
            ]
            if video_tracks:
                self._create_video_stream(video_tracks[0])
                break
        
        # Watch for new video tracks
        @room.on("track_subscribed")
        def on_track_subscribed(track: rtc.Track, publication: rtc.RemoteTrackPublication, participant: rtc.RemoteParticipant):
            if track.kind == rtc.TrackKind.KIND_VIDEO:
                self._create_video_stream(track)
    
    async def _image_received(self, reader, participant_identity):
        """Handle images uploaded from the frontend"""
        image_bytes = bytes()
        async for chunk in reader:
            image_bytes += chunk

        chat_ctx = self.chat_ctx.copy()

        # Encode the image to base64 and add it to the chat context
        chat_ctx.add_message(
            role="user",
            content=[
                "Here's an image I want to share with you:",
                ImageContent(
                    image=f"data:image/png;base64,{base64.b64encode(image_bytes).decode('utf-8')}"
                )
            ],
        )
        await self.update_chat_ctx(chat_ctx)
    
    async def on_user_turn_completed(self, turn_ctx: ChatContext, new_message: dict) -> None:
        # Add the latest video frame, if any, to the new message
        if self._latest_frame:
            if isinstance(new_message.content, list):
                new_message.content.append(ImageContent(image=self._latest_frame))
            else:
                new_message.content = [new_message.content, ImageContent(image=self._latest_frame)]
            self._latest_frame = None
    
    # Helper method to buffer the latest video frame from the user's track
    def _create_video_stream(self, track: rtc.Track):
        # Close any existing stream (we only want one at a time)
        if self._video_stream is not None:
            self._video_stream.close()

        # Create a new stream to receive frames
        self._video_stream = rtc.VideoStream(track)
        
        async def read_stream():
            async for event in self._video_stream:
                # Process the frame (optionally resize it)
                image_bytes = encode(
                    event.frame,
                    EncodeOptions(
                        format="JPEG",
                        resize_options=ResizeOptions(
                            width=1024,
                            height=1024,
                            strategy="scale_aspect_fit"
                        )
                    )
                )
                # Store the latest frame for use later
                self._latest_frame = f"data:image/jpeg;base64,{base64.b64encode(image_bytes).decode('utf-8')}"
        
        # Store the async task
        task = asyncio.create_task(read_stream())
        self._tasks.append(task)
        task.add_done_callback(lambda t: self._tasks.remove(t) if t in self._tasks else None)


async def entrypoint(ctx: agents.JobContext):
    # Vision assistant with OpenAI
    session = AgentSession(
        llm=openai.realtime.RealtimeModel(
            voice="coral"
        )
    )

    # Optional: Add initial image context
    initial_ctx = ChatContext()
    # Uncomment and replace with actual image URL if needed
    # initial_ctx.add_message(
    #     role="user",
    #     content=[
    #         "Here is a picture to analyze", 
    #         ImageContent(image="https://example.com/image.jpg")
    #     ],
    # )

    await session.start(
        room=ctx.room,
        agent=VisionAssistant(),  # Use our vision-enabled assistant
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
            video_enabled=True,  # Enable video input
        ),
    )

    await session.generate_reply(
        instructions="Greet the user in ENGLISH and introduce yourself as a WSM Customer Support representative named Melissa. Let them know you can help them with their queries related to Webshop Manager. NEVER use any other language other than ENGLISH."
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint)) 