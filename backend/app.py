from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
import tempfile
import mimetypes
from werkzeug.utils import secure_filename
from PIL import Image
import zipfile

app = Flask(__name__)
CORS(app)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'bmp', 'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt', 'zip', 'rar'])


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

    # Ambil level kompresi dari request (default: normal)
    level = request.form.get('level', 'normal')
    
    # Tentukan quality berdasarkan level
    # light = kualitas tinggi (kompresi sedikit)
    # normal = seimbang
    # max = kompresi maksimal (kualitas rendah)
    quality_map = {
        'light': 80,   # ~20% kompresi
        'normal': 60,  # ~40% kompresi
        'max': 30      # ~60% kompresi
    }
    quality = quality_map.get(level, 60)

    # Kompresi sesuai tipe file
    if ext in ['jpg', 'jpeg', 'png', 'bmp', 'gif']:
        # Kompresi gambar
        output_path = os.path.join(temp_dir, f"compressed_{filename}")
        try:
            img = Image.open(input_path)
            if ext in ['jpg', 'jpeg']:
                img.save(output_path, quality=quality, optimize=True)
            else:
                # Untuk PNG/GIF, konversi ke format yang lebih kecil jika level max
                if level == 'max' and ext == 'png':
                    # Reduce colors for PNG on max compression
                    if img.mode in ('RGBA', 'LA'):
                        background = Image.new('RGB', img.size, (255, 255, 255))
                        background.paste(img, mask=img.split()[-1])
                        img = background
                    img = img.convert('P', palette=Image.ADAPTIVE, colors=256)
                img.save(output_path, optimize=True)
        except Exception as e:
            return jsonify({"error": f"Gagal kompres gambar: {str(e)}"}), 500
        return send_file(output_path, as_attachment=True, download_name=f"compressed_{filename}")


    else:
        # Kompresi file umum ke ZIP
        # Level ZIP: 1-9 (1=fastest, 9=best compression)
        zip_level_map = {
            'light': 3,   # Fast compression
            'normal': 6,  # Balanced
            'max': 9      # Maximum compression
        }
        zip_level = zip_level_map.get(level, 6)
        
        zip_path = os.path.join(temp_dir, f"compressed_{filename}.zip")
        try:
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=zip_level) as zipf:
                zipf.write(input_path, arcname=filename)
        except Exception as e:
            return jsonify({"error": f"Gagal kompres file: {str(e)}"}), 500
        return send_file(zip_path, as_attachment=True, download_name=f"compressed_{filename}.zip")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 