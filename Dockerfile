FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy agent code
COPY . .

# Download models 
RUN python vision_agent.py download-files

# Expose check port
EXPOSE 8081

# Run agent in dev mode (second command)
CMD ["python3", "vision_agent.py", "dev"]