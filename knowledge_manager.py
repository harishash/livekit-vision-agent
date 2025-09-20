"""
Knowledge Manager for Video Agent
Loads knowledge base files into memory and provides formatting functions.
"""


import os
from pathlib import Path



PROMPT_HEADER = "## KNOWLEDGE BASE"
PROMPT_DESCRIPTION = """
### Usage Guidelines
- Reference this knowledge when answering user questions
- Incorporate relevant details into your responses
- Prioritize this information over general knowledge when applicable
- Be specific and accurate when citing information from these documents
"""



class KnowledgeManager:
    """
    Manages knowledge base files for the video agent.
    Provides formatted access to knowledge files.
    """


    def __init__(self, knowledge_dir=None):
        """Initialize with the directory containing knowledge files"""
        if knowledge_dir is None:
            # Default to the 'data' directory in the same folder as this file
            self.knowledge_dir = (
                Path(os.path.dirname(os.path.abspath(__file__))) / "data"
            )
        else:
            self.knowledge_dir = Path(knowledge_dir)

        # Initial load (optional, format_knowledge will also refresh)
        self.knowledge_content = self._load_all_knowledge()


    def _load_all_knowledge(self):
        """Load all markdown knowledge files (*.md) from the knowledge directory into memory"""
        content = {}
        try:
            if not self.knowledge_dir.exists():
                return content
            for file_path in sorted(self.knowledge_dir.glob("*.md")):
                key = file_path.stem
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content[key] = f.read()
                except Exception:
                    content[key] = ""
        except Exception:
            # If anything goes wrong, return what we've collected so far
            pass
        return content


    def format_knowledge(self):
        """
        Format all knowledge for insertion into a prompt.
        Returns a formatted string with all knowledge content.
        This method reloads files on each call to pick up changes without restart.
        """
        # Reload knowledge on each call
        self.knowledge_content = self._load_all_knowledge()

        # Format each knowledge file with its title and content
        knowledge_sections = []
        for domain, content in self.knowledge_content.items():
            if content.strip():
                # Extract title from the content if it exists (assumed to be the first line)
                title = (
                    content.split("\n", 1)[0].strip("# ")
                    if content
                    else domain.capitalize()
                )
                formatted_section = f"### {title}\n\n{content}"
                knowledge_sections.append(formatted_section)

        # Combine all sections
        all_knowledge = "\n\n".join(
            [PROMPT_HEADER, PROMPT_DESCRIPTION] + knowledge_sections
        )
        return all_knowledge
