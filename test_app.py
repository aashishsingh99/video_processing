import os
import tempfile
import unittest
from datetime import datetime
from flask import jsonify
from video_processing import app, init_db, VIDEO_LOCAL_DIR, SQL_DB

class VideoManagementAPITestCase(unittest.TestCase):
    def setUp(self):
        """Set up a temporary database and testing environment."""
        self.db_fd, self.temp_db = tempfile.mkstemp()
        app.config['TESTING'] = True
        app.config['DATABASE'] = self.temp_db
        self.client = app.test_client()
        init_db()

        # Create temporary video directory
        self.temp_video_dir = tempfile.mkdtemp()
        app.config['VIDEO_LOCAL_DIR'] = self.temp_video_dir

    def tearDown(self):
        """Clean up after tests."""
        os.close(self.db_fd)
        os.unlink(self.temp_db)
        os.rmdir(self.temp_video_dir)

    def test_upload_video(self):
        """Test the video upload endpoint."""
        with open("sample_video.mp4", "wb") as f:  # Create a temporary video file
            f.write(b"dummy video content")

        with open("sample_video.mp4", "rb") as video_file:
            response = self.client.post(
                '/upload',
                data={
                    'video_file': video_file,
                    'maximum_video_file_size': '100'
                },
                headers={'Authorization': f'Bearer {app.config["API_TOKEN"]}'}
            )
        os.remove("sample_video.mp4")
        self.assertEqual(response.status_code, 200)
        self.assertIn('Video uploaded successfully', response.get_json()['message'])

    def test_trim_video(self):
        """Test the video trimming endpoint."""
        # Simulate a video upload
        filename = "sample_video.mp4"
        filepath = os.path.join(self.temp_video_dir, filename)
        with open(filepath, "wb") as f:
            f.write(b"dummy video content")

        # Trim video
        response = self.client.post(
            '/trim',
            json={
                'filename': filename,
                'starttime': '00:00:00',
                'endtime': '00:00:10'
            },
            headers={'Authorization': f'Bearer {app.config["API_TOKEN"]}'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('Video trimmed successfully', response.get_json()['message'])

    def test_merge_videos(self):
        """Test the video merging endpoint."""
        filenames = ["video1.mp4", "video2.mp4"]
        for filename in filenames:
            filepath = os.path.join(self.temp_video_dir, filename)
            with open(filepath, "wb") as f:
                f.write(b"dummy video content")

        response = self.client.post(
            '/merge',
            json={
                'filenames': filenames
            },
            headers={'Authorization': f'Bearer {app.config["API_TOKEN"]}'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('Videos merged successfully!', response.get_json()['message'])

    def test_share_link(self):
        """Test the video share link endpoint."""
        filename = "shareable_video.mp4"
        filepath = os.path.join(self.temp_video_dir, filename)
        with open(filepath, "wb") as f:
            f.write(b"dummy video content")

        response = self.client.post(
            '/share',
            json={
                'filename': filename,
                'expiry_seconds': 3600
            },
            headers={'Authorization': f'Bearer {app.config["API_TOKEN"]}'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('Link created', response.get_json()['message'])
        self.assertIn('expiry', response.get_json())

if __name__ == '__main__':
    unittest.main()
