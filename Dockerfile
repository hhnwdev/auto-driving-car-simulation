# Step 1: Build Stage (for installing dependencies)
FROM python:3.13-alpine AS base

# Set environment variables to prevent .pyc file generation and unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install build dependencies (gcc, musl-dev for compiling)
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Remove build dependencies after installing Python packages
RUN apk del .build-deps

# Copy the source code into the image
COPY . .

# Step 2: Production Stage (excluding test files)
FROM python:3.13-alpine AS cli

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory for final production image
WORKDIR /app

# Copy installed dependencies from the base stage
COPY --from=base /usr/local /usr/local

# Copy only essential files (main program) into the production image
COPY --from=base /app/main.py /app/main.py
COPY --from=base /app/car_simulation.py /app/car_simulation.py
COPY --from=base /app/requirements.txt /app/requirements.txt

# Set default command to run the CLI app
CMD ["python", "main.py"]
