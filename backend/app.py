from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
import tempfile
import mimetypes
from werkzeug.utils import secure_filename
from PIL import Image
import zipfile
import subprocess

app = Flask(__name__)
CORS(app)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'bmp', 'mp4', 'mov', 'avi', 'mkv', 'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt', 'zip', 'rar'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return jsonify({"message": "Kompresin 2.0 Backend is running!"})

@app.route('/compress', methods=['POST'])
def compress_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if not allowed_file(file.filename):
        return jsonify({"error": "File type not allowed"}), 400

    filename = secure_filename(file.filename)
    ext = filename.rsplit('.', 1)[1].lower()
    temp_dir = tempfile.mkdtemp()
    input_path = os.path.join(temp_dir, filename)
    file.save(input_path)

    # Kompresi sesuai tipe file
    if ext in ['jpg', 'jpeg', 'png', 'bmp', 'gif']:
        # Kompresi gambar
        output_path = os.path.join(temp_dir, f"compressed_{filename}")
        try:
            img = Image.open(input_path)
            if ext in ['jpg', 'jpeg']:
                img.save(output_path, quality=60, optimize=True)
            else:
                img.save(output_path, optimize=True)
        except Exception as e:
            return jsonify({"error": f"Gagal kompres gambar: {str(e)}"}), 500
        return send_file(output_path, as_attachment=True, download_name=f"compressed_{filename}")

    elif ext in ['mp4', 'mov', 'avi', 'mkv']:
        # Kompresi video (menggunakan ffmpeg, bitrate rendah)
        output_path = os.path.join(temp_dir, f"compressed_{filename}")
        try:
            cmd = [
                'ffmpeg', '-i', input_path,
                '-b:v', '800k', '-bufsize', '800k',
                '-vf', 'scale=iw*0.7:ih*0.7',
                '-preset', 'fast',
                '-y', output_path
            ]
            result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr.decode(errors='ignore')
            return jsonify({"error": f"Gagal kompres video: {error_msg}"}), 500
        except Exception as e:
            return jsonify({"error": f"Gagal kompres video: {str(e)}"}), 500
        return send_file(output_path, as_attachment=True, download_name=f"compressed_{filename}")

    else:
        # Kompresi file umum ke ZIP
        zip_path = os.path.join(temp_dir, f"compressed_{filename}.zip")
        try:
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(input_path, arcname=filename)
        except Exception as e:
            return jsonify({"error": f"Gagal kompres file: {str(e)}"}), 500
        return send_file(zip_path, as_attachment=True, download_name=f"compressed_{filename}.zip")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 