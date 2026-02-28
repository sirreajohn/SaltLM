import requests
import time
import subprocess
import tempfile


def get_audio(text=None):
    URL = "http://localhost:8001/synthesize"
    if text is None:
        text = "This is a live test of the Docker TTS container."

    payload = {
        "text": text,
        "voice": "bf_isabella"
    }

    start = time.perf_counter()
    response = requests.post(URL, json=payload)
    end = time.perf_counter()

    print(f"TTS: total time taken: {end - start:.2f}")
    if response.status_code == 200:
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            f.write(response.content)
            temp_path = f.name

        subprocess.run(["afplay", temp_path])
    else:
        print("Error:", response.status_code, response.text)


def get_llm_resp(user_prompt=None):

    URL = "http://localhost:8080/v1/chat/completions"

    with open("./sys_prompt.txt") as f:
        system_prompt = f.read()


    if user_prompt is None:
        user_prompt = "Explain VAD."

    payload = {
        "model": "ignored",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 200
    }

    start = time.perf_counter()
    response = requests.post(URL, json=payload)
    end = time.perf_counter()

    print(f"LLM: total time taken: {end - start:.2f}")
    res_text = response.json()["choices"][0]["message"]["content"]
    print(res_text)
    return res_text


def test_pipe():
    user_prompt = input("enter something: ")
    res_text = get_llm_resp(user_prompt)
    get_audio(res_text)


if __name__ == "__main__":
    test_pipe()

