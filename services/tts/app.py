from fastapi import FastAPI
from fastapi.responses import Response
from kokoro import KPipeline
import soundfile as sf
import io

app = FastAPI()

pipeline = KPipeline(lang_code='b', repo_id='hexgrad/Kokoro-82M')

@app.post("/synthesize")
async def synthesize(payload: dict):
    text = payload["text"]
    voice = payload.get("voice", "af_heart")

    generator = pipeline(text, voice=voice)
    _, _, audio = next(generator)

    buffer = io.BytesIO()
    sf.write(buffer, audio, 24000, format="WAV")
    buffer.seek(0)

    return Response(buffer.read(), media_type="audio/wav")