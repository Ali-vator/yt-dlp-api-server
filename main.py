from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, JSONResponse
import yt_dlp
import os
import uuid

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Video Downloader API is working"}

@app.get("/download")
def download_video(url: str = Query(..., description="Video URL")):
    video_id = str(uuid.uuid4())
    output_path = f"{video_id}.mp4"

    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': output_path,
        'quiet': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

    return FileResponse(output_path, media_type='video/mp4', filename="video.mp4")

@app.get("/cleanup")
def cleanup():
    for file in os.listdir():
        if file.endswith(".mp4"):
            os.remove(file)
    return {"message": "All videos cleaned up"}
