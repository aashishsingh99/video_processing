import os 
import sqlite3
import subprocess
from flask import Flask, request, jsonify

SQL_DB = 'video_db'
VIDEO_LOCAL_DIR = 'videos'
app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_video():
    file = request.files.get('video_file')
    max_file_size = request.form.get('maximum_video_file_size')
    min_duration = request.form.get('minimum_video_duration')
    max_duration = request.form.get('maximum_video_duration')
    os.makedirs(VIDEO_LOCAL_DIR)
    filename = file.filename
    filepath = os.path.join(VIDEO_LOCAL_DIR, filename)
    file.save(filepath)
    with sqlite3.connect(SQL_DB) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO videos_table (filename) VALUES (?)", (filename,))
        conn.commit()
        return jsonify({"message": "Video uploaded successfully", "filename": filename})
    return jsonify({"message": "Some errored occurred!", "filename": filename})

@app.route('/trim', methods=['POST'])
def trim_video():
    trim_data = request.get_json()
    filename = trim_data.get('filename')
    start_time = trim_data.get('starttime')
    end_time = trim_data.get('endtime')
    filepath = os.path.join(VIDEO_LOCAL_DIR, filename)
    trimmed_video_filepath = os.path.join(VIDEO_LOCAL_DIR, filename.replace('.','.trimmed'))
    try:
        subprocess.run([
                "ffmpeg",
                "-i", filepath,
                "-ss", str(start_time), 
                "-to", str(end_time),  
                "-c", "copy", 
                trimmed_video_filepath  
            ],check=True)
    except subprocess.CalledProcessError as e:
        return jsonify({"error": "Error during video trimming", "details": str(e)})
    return jsonify({"message": "Video trimmed successfully", "filename": trimmed_video_filepath})

@app.route('/merge', methods=['POST'])
def merge_videos():
    merge_data = request.get_json()
    filenames = merge_data.get('filenames', [])
    merged_filename = 'merged_video.mp4'
    merged_filepath = os.path.join(VIDEO_LOCAL_DIR, merged_filename)
    filepaths = []
    for filename in filenames:
        filepath = os.path.join(VIDEO_LOCAL_DIR, filename)
        filepaths.append(filepath)
    file_list_path = os.path.join(VIDEO_LOCAL_DIR, "file_list.txt")
    with open(file_list_path, 'w') as file_list:
        for filepath in filepaths:
            file_list.write(f"file '{filepath}'\n")
    try:
        subprocess.run(
            [
                "ffmpeg",
                "-f", "concat",  
                "-safe", "0",    
                "-i", file_list_path,
                "-c", "copy",    
                merged_filepath
            ],
            check=True
        )
    except subprocess.CalledProcessError as e:
        return jsonify({"error": "Error during video merging", "details": str(e)})
    
    return jsonify({"message": "Videos merged succesfully!", "filename": merged_filename})






