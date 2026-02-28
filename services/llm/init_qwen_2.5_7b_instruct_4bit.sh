./build/bin/llama-server \
    -m /Users/sirrea/workspaces/data_science/saltLM/models/qwen_2.5_7b_instruct_4bit/qwen2.5-7b-instruct-q4_k_m-00001-of-00002.gguf \
    -c 2048 \
    -t 8 \
    --host 0.0.0.0 \
    --port 8080