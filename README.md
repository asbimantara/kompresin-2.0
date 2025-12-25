# Kompresin 2.0

🔗 **Live Demo:** [https://kompresin-2-0.onrender.com](https://kompresin-2-0.onrender.com)

Aplikasi kompresi data berbasis web dengan backend Python (Flask) dan frontend modern (HTML, CSS, JS).

## Struktur Project

```
backend/
├── app.py              # Flask app (API + serve frontend)
├── static/             # Frontend files
│   ├── index.html
│   ├── script.js
│   └── style.css
├── requirements.txt
└── Procfile
frontend/               # Development frontend (duplikat untuk dev lokal)
```

## Fitur Utama

- ✅ Kompresi file gambar (jpg, jpeg, png, gif, bmp)
- ✅ Kompresi file dokumen (pdf, doc, docx, ppt, pptx, xls, xlsx, txt, zip, rar) ke format ZIP
- ✅ **3 Level Kompresi:**
  - 🌱 Ringan - Kualitas tinggi, kompresi ~20%
  - ⚖️ Normal - Seimbang, kompresi ~40%
  - 🔥 Maksimal - Ukuran kecil, kompresi ~60%
- ✅ Validasi file otomatis (tolak format tidak didukung)
- ✅ Tampilan modern, responsif, dark mode
- ✅ Progress bar animasi
- ✅ Notifikasi hasil kompresi (ukuran awal, akhir, persentase)
- ✅ Download hasil kompresi otomatis

## Cara Menggunakan

1. Buka [https://kompresin-2-0.onrender.com](https://kompresin-2-0.onrender.com)
2. Pilih level kompresi (Ringan/Normal/Maksimal)
3. Klik **Pilih File** dan pilih gambar atau dokumen
4. Klik **Kompres**
5. Tunggu proses selesai, lalu klik **Download**

> ⚠️ **Catatan:** Akses pertama mungkin lambat (~30 detik) karena server gratis perlu "bangun" dari sleep mode.

## Format File yang Didukung

| Kategori | Format |
|----------|--------|
| **Gambar** | jpg, jpeg, png, gif, bmp |
| **Dokumen** | pdf, doc, docx, ppt, pptx, xls, xlsx, txt, zip, rar |

## Cara Menjalankan Lokal

```bash
# 1. Clone repository
git clone https://github.com/asbimantara/kompresin-2.0.git
cd kompresin-2.0/backend

# 2. Install dependencies
pip install -r requirements.txt

# 3. Jalankan server
python app.py

# 4. Buka browser ke http://localhost:5000
```

## Teknologi

- **Backend:** Python, Flask, Pillow
- **Frontend:** HTML, CSS, JavaScript
- **Hosting:** Render (Web Service)

## Pembuat

- **Ahmad Surya Bimantara**
- **Abdullah Sallam**

Mahasiswa Teknik Informatika, UNISNU Jepara.

---

© 2025 Kompresin 2.0