README
Video Management API
This project is a Flask-based API for managing video files. It provides functionality for uploading, trimming, merging, and generating shareable links for video files.

Features
Upload Videos: Upload video files to a local directory and store metadata in a SQLite database.
Trim Videos: Trim a section of a video file based on start and end times.
Merge Videos: Combine multiple video files into a single video.
Share Links: Generate shareable links for video files with an expiry time.
Prerequisites
Python 3.7 or higher
Flask
SQLite3
FFmpeg
Installation
Clone the repository:

bash
Copy code
git clone <repository-url>  
cd <repository-directory>  
Install dependencies:

bash
Copy code
pip install -r requirements.txt  
Install FFmpeg:
FFmpeg must be installed and available in the system's PATH.

FFmpeg Installation Guide
Configuration
Set the API token in the API_TOKEN variable in the script.

python
Copy code
API_TOKEN = '<your-api-token>'  
Ensure VIDEO_LOCAL_DIR and SQL_DB directories are writable by the application.

Endpoints
1. Upload Video
URL: /upload
Method: POST
Headers:

Authorization: Bearer <API_TOKEN>
Form Data:

video_file: The video file to upload.
maximum_video_file_size: (Optional) Maximum allowed size of the video file.
minimum_video_duration: (Optional) Minimum allowed duration of the video.
maximum_video_duration: (Optional) Maximum allowed duration of the video.
Response:

json
Copy code
{  
  "message": "Video uploaded successfully",  
  "filename": "<uploaded-filename>"  
}  
2. Trim Video
URL: /trim
Method: POST
Headers:

Authorization: Bearer <API_TOKEN>
Body (JSON):

json
Copy code
{  
  "filename": "<video-file-name>",  
  "starttime": "<start-time>",  
  "endtime": "<end-time>"  
}  
Response:

json
Copy code
{  
  "message": "Video trimmed successfully",  
  "filename": "<trimmed-video-filename>"  
}  
3. Merge Videos
URL: /merge
Method: POST
Headers:

Authorization: Bearer <API_TOKEN>
Body (JSON):

json
Copy code
{  
  "filenames": ["<video1>", "<video2>", "<video3>"]  
}  
Response:

json
Copy code
{  
  "message": "Videos merged successfully!",  
  "filename": "merged_video.mp4"  
}  
4. Share Link
URL: /share
Method: POST
Headers:

Authorization: Bearer <API_TOKEN>
Body (JSON):

json
Copy code
{  
  "filename": "<video-file-name>",  
  "expiry_seconds": <expiry-time-in-seconds>  
}  
Response:

json
Copy code
{  
  "message": "Link created",  
  "expiry": "<expiry-timestamp>"  
}  
Database Schema
The application uses an SQLite database with the following schema:

Table: videos

Column	Type	Description
id	INTEGER	Primary key, auto-incremented
filename	TEXT	Name of the video file
upload_time	TIMESTAMP	Timestamp of the upload (default: current)
Error Handling
Returns 401 Unauthorized for invalid or missing API tokens.
Returns 404 Not Found if a requested video file does not exist.
Returns 500 Internal Server Error for unexpected errors during processing.
Notes
Ensure FFmpeg is correctly installed and accessible in the system's PATH.
Video files are stored in the videos directory. Adjust VIDEO_LOCAL_DIR as needed.
License
This project is licensed under the MIT License.

Author
Aashish Kirti Singh
