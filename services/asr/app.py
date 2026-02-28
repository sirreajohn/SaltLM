from fastapi import FastAPI, UploadFile
from faster_whisper import WhisperModel
import tempfile
import shutil

app = FastAPI()

model = WhisperModel("base", compute_type="int8")

@app.post("/transcribe")
async def transcribe(file: UploadFile):
    with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
        shutil.copyfileobj(file.file, temp_audio)
        temp_path = temp_audio.name

    segments, _ = model.transcribe(
        temp_path,
        vad_filter=True,
        vad_parameters=dict(
            min_silence_duration_ms=800
        )
    )
    text = " ".join([segment.text for segment in segments])

    return {"text": text}