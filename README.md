# 🚀 yt-dlp-api-server 🌐

Welcome to **yt-dlp-api-server**, a powerful and lightweight API server powered by [yt-dlp](https://github.com/yt-dlp/yt-dlp) for extracting video and audio metadata and download URLs from thousands of supported sites! 📹🎧 Whether you're a developer building a media server or just need a simple way to fetch video info, this API has you covered. Deploy it locally or on a free platform like Railway with ease! 🛠️

---

## 📚 Features

- **🎥 Video Metadata**: Retrieve detailed info like title, description, duration, uploader, and more from video URLs.
- **📥 Download URLs**: Get direct download links for video or audio in various formats (e.g., MP4, MP3, WebM).
- **🔢 Format Selection**: Choose specific formats or quality levels (e.g., 1080p, 720p, best audio).
- **🌍 Multi-Platform Support**: Supports thousands of sites, including YouTube, Vimeo, SoundCloud, and more, thanks to yt-dlp.
- **⚡ Fast & Lightweight**: Built with efficiency in mind, using FastAPI for high-performance API endpoints.
- **🔐 Safe & Secure**: No video data is stored; URLs are fetched in real-time.
- **📜 Simple Endpoints**: Easy-to-use REST API with JSON responses for seamless integration.
- **API Endpoints**:
  - `GET /info?url={video_url}`: Fetch video metadata.
  - `GET /download?url={video_url}&format={format_id}`: Get download URL for a specific format.
  - `GET /formats?url={video_url}`: List available formats for a video.

---

## 🛠️ Getting Started

Follow these steps to run the API locally or deploy it to a free service like [Railway](https://railway.app) for public access! 🌟

### 🖥️ Run Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ali-vator/yt-dlp-api-server.git
   cd yt-dlp-api-server
   ```

2. **Install Dependencies**:
   - Ensure you have [Python 3.8+](https://www.python.org/) and [pip](https://pip.pypa.io/) installed.
   - Install required packages:
     ```bash
     pip install -r requirements.txt
     ```
   - Install `yt-dlp`:
     ```bash
     pip install yt-dlp
     ```

3. **Run the Server**:
   - Start the FastAPI server with:
     ```bash
     uvicorn main:app --reload
     ```
   - The API will be available at `http://localhost:8000`.

4. **Test the API**:
   - Open your browser or use `curl` to test an endpoint:
     ```bash
     curl "http://localhost:8000/info?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ"
     ```

### 🚂 Deploy on Railway

1. **Sign Up for Railway**:
   - Create a free account at [Railway](https://railway.app).

2. **Create a New Project**:
   - Click "New Project" and select "Deploy from GitHub".
   - Authorize Railway to access your GitHub account and select the `yt-dlp-api-server` repository.

3. **Configure the Deployment**:
   - Railway will detect your Python project automatically.
   - Add the following environment variables (if needed):
     - `PORT`: `8000` (or as required by Railway).
   - Ensure `requirements.txt` includes `fastapi`, `uvicorn`, and `yt-dlp`.

4. **Deploy**:
   - Click "Deploy" and wait for the build to complete.
   - Railway will provide a public URL (e.g., `https://your-app.railway.app`).

5. **Test the Deployed API**:
   - Use the public URL to access the API:
     ```bash
     curl "https://your-app.railway.app/info?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ"
     ```

---

## 📡 API Usage Examples

Here are some example `curl` commands to interact with the API. Replace `https://your-api-url` with `http://localhost:8000` (local) or your Railway URL (deployed).

1. **Get Video Metadata**:
   ```bash
   curl "https://your-api-url/info?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ"
   ```
   **Response** (example):
   ```json
   {
     "title": "Rick Astley - Never Gonna Give You Up",
     "uploader": "RickAstleyVEVO",
     "duration": 212,
     "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
   }
   ```

2. **List Available Formats**:
   ```bash
   curl "https://your-api-url/formats?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ"
   ```
   **Response** (example):
   ```json
   [
     {"format_id": "18", "ext": "mp4", "resolution": "360p"},
     {"format_id": "22", "ext": "mp4", "resolution": "720p"},
     {"format_id": "140", "ext": "m4a", "audio": "128kbps"}
   ]
   ```

3. **Get Download URL**:
   ```bash
   curl "https://your-api-url/download?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ&format=22"
   ```
   **Response** (example):
   ```json
   {
     "download_url": "https://some-direct-link.com/video.mp4",
     "format": "720p"
   }
   ```

---

## ❓ FAQ

- **Why is my video URL not working?**  
  Ensure the URL is valid and supported by `yt-dlp`. Check the [yt-dlp supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).[](https://github.com/yt-dlp/yt-dlp)

- **How do I update `yt-dlp`?**  
  Run `pip install --upgrade yt-dlp` to keep `yt-dlp` up-to-date.

- **Is there a rate limit?**  
  Locally, there’s no limit. On Railway’s free tier, you may hit resource limits; consider upgrading for heavy usage.

- **Can I use this for commercial projects?**  
  Check the [yt-dlp license](https://github.com/yt-dlp/yt-dlp/blob/master/LICENSE) and ensure compliance with the target site’s terms.

---

## 🤝 Contributing

We love contributions! 🎉 To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/awesome-feature`).
3. Commit your changes (`git commit -m "Add awesome feature"`).
4. Push to the branch (`git push origin feature/awesome-feature`).
5. Open a Pull Request.

Please follow the [Code of Conduct](CODE_OF_CONDUCT.md) and report issues via [GitHub Issues](https://github.com/Ali-vator/yt-dlp-api-server/issues).

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.

---

Built with ❤️ by [Ali-vator](https://github.com/Ali-vator). Happy downloading! 🎥
