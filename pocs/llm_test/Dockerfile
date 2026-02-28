FROM debian:bookworm

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Clone llama.cpp
RUN git clone https://github.com/ggerganov/llama.cpp.git

WORKDIR /app/llama.cpp

# Build
RUN make -j$(nproc)

# Expose server port
EXPOSE 8080

# Default command
CMD ["./server", "-m", "/models/model.gguf", "-c", "4096", "--host", "0.0.0.0"]