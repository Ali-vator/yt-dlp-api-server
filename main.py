from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, JSONResponse
from yt_dlp import YoutubeDL
import uuid
import os
import shutil
import zipfile
import re

app = FastAPI()

BASE_DOWNLOAD_FOLDER = "downloads"
os.makedirs(BASE_DOWNLOAD_FOLDER, exist_ok=True)

def get_format_option(quality: str) -> str:
    if quality == "audio":
        return "bestaudio"
    elif quality.endswith("p") and quality[:-1].isdigit():
        return f"bestvideo[height<={quality[:-1]}]+bestaudio/best[height<={quality[:-1]}]"
    return "best"

@app.get("/")
async def root():
    return {"status": "API is up and running!"}

@app.get("/download")
async def download_video(
    url: str = Query(..., description="رابط الفيديو أو القائمة"),
    quality: str = Query("best", description="جودة الفيديو: best, 720p, 1080p, audio")
):
    try:
        session_id = str(uuid.uuid4())
        session_path = os.path.join(BASE_DOWNLOAD_FOLDER, session_id)
        os.makedirs(session_path, exist_ok=True)

        ydl_opts = {
            'format': get_format_option(quality),
            'outtmpl': os.path.join(session_path, '%(title)s.%(ext)s'),
            'quiet': True,
            'cookiefile': 'cookies.txt'
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        files_downloaded = os.listdir(session_path)

        if len(files_downloaded) == 0:
            raise Exception("No files downloaded.")

        elif len(files_downloaded) == 1:
            original_file = files_downloaded[0]
            original_path = os.path.join(session_path, original_file)

            # استخراج الامتداد الأصلي
            ext = os.path.splitext(original_file)[1] or ".mp4"

            # تحديد اسم الملف النهائي الثابت
            if quality == "audio":
                safe_filename = "audio.mp3"
            elif quality != "best":
                safe_filename = f"video_{quality}.mp4"
            else:
                safe_filename = "video.mp4"

            safe_path = os.path.join(session_path, safe_filename)
            os.rename(original_path, safe_path)

            return FileResponse(
                safe_path,
                media_type="application/octet-stream",
                filename=safe_filename
            )

        else:
            zip_name = f"{session_id}.zip"
            zip_path = os.path.join(BASE_DOWNLOAD_FOLDER, zip_name)

            with zipfile.ZipFile(zip_path, 'w') as zipf:
                for file_name in files_downloaded:
                    original_file = os.path.join(session_path, file_name)
                    zipf.write(original_file, arcname=file_name)

            shutil.rmtree(session_path)
            return FileResponse(zip_path, media_type="application/zip", filename=zip_name)

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
