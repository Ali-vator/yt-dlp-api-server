from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, JSONResponse
from yt_dlp import YoutubeDL
import uuid
import os

app = FastAPI()

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.get("/")
async def root():
    return {"status": "API is up and running!"}

@app.get("/download")
async def download_video(url: str = Query(..., description="رابط الفيديو")):
    try:
        filename = f"{uuid.uuid4()}.mp4"
        output_path = os.path.join(DOWNLOAD_FOLDER, filename)

        ydl_opts = {
            'format': 'best[ext=mp4]',
            'outtmpl': output_path,
            'quiet': True,
            'cookiefile': 'cookies.txt'  # استخدم الكوكيز هنا
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return FileResponse(output_path, media_type="video/mp4", filename=filename)

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
