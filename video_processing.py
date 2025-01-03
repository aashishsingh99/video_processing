import os 
import sqlite3
from flask import Flask, request, jsonify

SQL_DB = 'video_db'


def upload_video():
    file = request.files.get('video_file')
    max_file_size = request.form.get('maximum_video_file_size')
    min_duration = request.form.get('minimum_video_duration')
    max_duration = request.form.get('maximum_video_duration')
    upload_folder = 'videos'
    os.makedirs(upload_folder)
    filename = file.filename
    filepath = os.path.join(upload_folder, filename)
    file.save(filepath)
    with sqlite3.connect(SQL_DB) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO videos_table (filename) VALUES (?)", (filename,))
        conn.commit()
        return jsonify({"message": "Video uploaded successfully", "filename": filename})
    return jsonify({"message": "Some errored occurred!", "filename": filename})


