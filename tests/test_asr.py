import sounddevice as sd
import soundfile as sf
import requests
import tempfile

ASR_URL = "http://localhost:8002/transcribe"

SAMPLE_RATE = 16000
# DURATION = 5  # seconds


def transcibe_mic(duration = 5):
    print("Speak now...")
    audio = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype="float32")
    sd.wait()
    print("Recording complete.")

    # Save to temp WAV
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        sf.write(f.name, audio, SAMPLE_RATE)
        temp_path = f.name

    # Send to ASR
    with open(temp_path, "rb") as f:
        files = {"file": ("audio.wav", f, "audio/wav")}
        response = requests.post(ASR_URL, files=files)

    if response.status_code == 200:
        transcription = response.json()["text"]
        print("Transcription:")
        print(transcription)
        return transcription
    else:
        print("Error:", response.status_code, response.text)



# if __name__ == "__main__":
#     continous_listen()