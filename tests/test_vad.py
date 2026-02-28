import sounddevice as sd
import numpy as np
import torch
import wave
import queue
from silero_vad import load_silero_vad, get_speech_timestamps

RATE = 16000
CHANNELS = 1
SILENCE_TIMEOUT = 0.8

audio_queue = queue.Queue()

def callback(indata, frames, time, status):
    audio_queue.put(indata.copy())

model = load_silero_vad()

print("Listening...")

recording = []
silence_counter = 0
triggered = False

with sd.InputStream(samplerate=RATE, channels=CHANNELS, dtype="float32", callback=callback):

    while True:
        chunk = audio_queue.get().flatten()
        tensor = torch.from_numpy(chunk)

        speech = get_speech_timestamps(tensor, model, sampling_rate=RATE)

        if speech:
            triggered = True
            silence_counter = 0
            recording.append(chunk)
        elif triggered:
            silence_counter += len(chunk) / RATE
            recording.append(chunk)

            if silence_counter > SILENCE_TIMEOUT:
                break

print("Saving...")

audio = np.concatenate(recording)
audio_int16 = (audio * 32767).astype(np.int16)

with wave.open("output.wav", "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(RATE)
    wf.writeframes(audio_int16.tobytes())

print("Saved to output.wav")