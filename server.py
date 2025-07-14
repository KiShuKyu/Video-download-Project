# used AI to help with Flask

from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
    link = request.form['link'].strip()
    filename = request.form['filename'].strip()
    platform = request.form['platform']

    if not filename.endswith('.mp4'):
        filename += '.mp4'

    filepath = os.path.join('downloads', filename)

    ydl_opts = {
        'outtmpl': filepath
    }

    if platform == 'insta':
        ydl_opts['cookies'] = 'cookies.txt'

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        return send_file(filepath, as_attachment=True)
    except Exception as e:
        return f"⚠️ Download failed: {e}", 500


if __name__ == '__main__':
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    app.run(debug=True)
# end
