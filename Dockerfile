# Use Alpine-based Python image
FROM python:3.13-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install build dependencies
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev

# Copy requirements file
COPY requirements.txt requirements.txt

# Install Python dependencies (none required now, just placeholder)
RUN pip install --no-cache-dir -r requirements.txt

# Remove build dependencies after installation
RUN apk del .build-deps

# Copy source code
COPY . .

# Set default command to run the CLI app
CMD ["python", "main.py"]
