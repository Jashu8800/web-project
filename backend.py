from flask import Flask, request, jsonify
import os
import yt_dlp

app = Flask(__name__)
cur_dir = os.getcwd()

def download_video(link, video_id):
    youtube_dl_options = {
        "format": "bestvideo",
        "outtmpl": os.path.join(cur_dir, f"{video_id}.mp4")
    }
    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        ydl.download([link])

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    link = data.get('link')
    video_id = "video_filename"  # You can generate unique filenames here
    try:
        download_video(link, video_id)
        return jsonify({"message": "Download successful", "filename": f"{video_id}.mp4"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)





