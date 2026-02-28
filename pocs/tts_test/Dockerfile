# Base image
FROM python:3.12-bookworm

ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    ffmpeg \
    libsndfile1 \
    libffi-dev \
    libssl-dev \
    git \
    curl \
    ca-certificates \
    espeak-ng \
    && rm -rf /var/lib/apt/lists/*

# Install Rust (non-interactive)
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

# Ensure cargo is in PATH
ENV PATH="/root/.cargo/bin:${PATH}"

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Set working directory
WORKDIR /app

# Default command
CMD ["sleep", "infinity"]