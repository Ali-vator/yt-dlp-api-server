from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, JSONResponse
from yt_dlp import YoutubeDL
import uuid
import os
import shutil
import zipfile

app = FastAPI()

BASE_DOWNLOAD_FOLDER = "downloads"
os.makedirs(BASE_DOWNLOAD_FOLDER, exist_ok=True)

# تحويل جودة إلى صيغة yt-dlp
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
            file_path = os.path.join(session_path, files_downloaded[0])
            return FileResponse(file_path, media_type="application/octet-stream", filename=files_downloaded[0])

        else:
            zip_name = f"{session_id}.zip"
            zip_path = os.path.join(BASE_DOWNLOAD_FOLDER, zip_name)
            with zipfile.ZipFile(zip_path, 'w') as zipf:
                for file_name in files_downloaded:
                    zipf.write(os.path.join(session_path, file_name), arcname=file_name)

            shutil.rmtree(session_path)
            return FileResponse(zip_path, media_type="application/zip", filename=zip_name)

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
