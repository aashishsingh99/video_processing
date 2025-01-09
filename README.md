README

Video Management API

This project is a Flask-based API for managing video files. It provides functionality for uploading, trimming, merging, and generating shareable links for video files.

Features
- Upload Videos: Upload video files to a local directory and store metadata in a SQLite database.
- Trim Videos: Trim a section of a video file based on start and end times.
- Merge Videos: Combine multiple video files into a single video.
- Share Links: Generate shareable links for video files with an expiry time.

---

Prerequisites
- Python 3.7 or higher
- Flask
- SQLite3
- FFmpeg

---

Installation

1. Clone the repository:
git clone <repository-url> cd <repository-directory>

2. Install dependencies:
pip install -r requirements.txt

3. Install FFmpeg:
FFmpeg must be installed and available in the system's PATH.
- FFmpeg Installation Guide: https://ffmpeg.org/download.html

---

Configuration

1. Set the API token in the `API_TOKEN` variable in the script.

2. Ensure `VIDEO_LOCAL_DIR` and `SQL_DB` directories are writable by the application.

---

Endpoints

1. Upload Video
URL: `/upload`
Method: `POST`
Headers:
- `Authorization`: `Bearer <API_TOKEN>`

Form Data:
- `video_file`: The video file to upload.
- `maximum_video_file_size`: (Optional) Maximum allowed size of the video file.
- `minimum_video_duration`: (Optional) Minimum allowed duration of the video.
- `maximum_video_duration`: (Optional) Maximum allowed duration of the video.


2. Ensure `VIDEO_LOCAL_DIR` and `SQL_DB` directories are writable by the application.

---

Endpoints

1. Upload Video
URL: `/upload`
Method: `POST`
Headers:
- `Authorization`: `Bearer <API_TOKEN>`

Form Data:
- `video_file`: The video file to upload.
- `maximum_video_file_size`: (Optional) Maximum allowed size of the video file.
- `minimum_video_duration`: (Optional) Minimum allowed duration of the video.
- `maximum_video_duration`: (Optional) Maximum allowed duration of the video.

3. Merge Videos
URL: `/merge`
Method: `POST`
Headers:
- `Authorization`: `Bearer <API_TOKEN>`

Body (JSON):
{ "filenames": ["<video1>", "<video2>", "<video3>"] }

4. Share Link
URL: `/share`
Method: `POST`
Headers:
- `Authorization`: `Bearer <API_TOKEN>`

Body (JSON):
{ "filename": "<video-file-name>", "expiry_seconds": <expiry-time-in-seconds> }

License
This project is licensed under the MIT License.

---

Author
Aashish Kirti Singh



