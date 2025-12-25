# Kompresin 2.0

Aplikasi kompresi data berbasis web dengan backend Python (Flask) dan frontend modern (HTML, CSS, JS).

## Struktur Project

- `backend/` : Backend Python (API kompresi file)
- `frontend/` : Frontend web (UI, animasi, gambar online)

## Manual Book Aplikasi (Detail)

### 1. Deskripsi Singkat
Kompresin 2.0 adalah aplikasi web yang memudahkan pengguna untuk mengompres berbagai jenis file (gambar, dokumen) agar ukurannya lebih kecil, sehingga lebih mudah disimpan dan dibagikan.

### 2. Fitur Utama
- Kompresi file gambar (jpg, jpeg, png, gif, bmp)
- Kompresi file dokumen (pdf, doc, docx, ppt, pptx, xls, xlsx, txt, zip, rar) ke format ZIP
- Tampilan modern, responsif, dan mudah digunakan
- Progress bar animasi saat proses kompresi
- Notifikasi hasil kompresi (ukuran awal, akhir, dan persentase pengurangan)
- Download hasil kompresi dengan nama file otomatis
- Modal info pembuat aplikasi

### 3. Langkah Penggunaan
#### A. Membuka Aplikasi
1. Buka link frontend aplikasi, misal: `https://kompresin-2-0-static.onrender.com` di browser (PC/HP).

#### B. Memahami Tampilan Utama
- **Header:** Judul aplikasi dan tombol info pembuat.
- **Ucapan Selamat Datang:** Penjelasan singkat aplikasi.
- **Dua Kotak Format:** Menjelaskan format file yang didukung (file umum, gambar).
- **Kotak Kompresi:**
  - Judul dan subjudul.
  - Tombol "Pilih File" (custom, besar, modern).
  - Nama file yang dipilih akan tampil otomatis.
  - Tombol "Kompres" untuk memulai proses.
  - Progress bar animasi.
  - Keterangan hasil kompresi (ukuran awal, akhir, pengurangan).
  - Tombol "Download" hasil kompresi.
- **Footer:** Copyright aplikasi.

#### C. Mengompres File
1. Klik **Pilih File** dan pilih file dari perangkat Anda.
2. Nama file akan muncul di bawah tombol.
3. Klik **Kompres** untuk memulai proses.
4. Progress bar akan berjalan selama proses berlangsung.
5. Setelah selesai, akan muncul info ukuran file awal, akhir, dan persentase pengurangan.
6. Klik **Download** untuk mengunduh file hasil kompresi.

#### D. Melihat Info Pembuat
1. Klik tombol **i** di pojok kanan atas.
2. Modal akan muncul berisi nama pembuat dan asal kampus.
3. Klik tanda silang (X) atau area luar modal untuk menutup.

### 4. Format File yang Didukung
- **Gambar:** jpg, jpeg, png, gif, bmp
- **File Umum:** pdf, doc, docx, ppt, pptx, xls, xlsx, txt, zip, rar (akan dikompres ke ZIP)

### 5. Troubleshooting & Catatan
- **File terlalu besar gagal upload:**
  - Coba gunakan file yang lebih kecil (<50MB).
- **Progress bar tidak bergerak:**
  - Tunggu beberapa saat, server gratis bisa sleep dan butuh waktu untuk aktif kembali.
- **Download tidak muncul:**
  - Pastikan file sudah selesai diproses dan tidak ada error.
- **CORS error:**
  - Pastikan backend sudah mengaktifkan flask-cors.

### 6. Catatan Hosting & Deploy
- **Frontend** di-deploy di Render Static Site (atau Vercel/Netlify).
- **Backend** di-deploy di Render Web Service (atau Railway/VPS).
- URL backend di `frontend/script.js` harus mengarah ke backend online.
- Untuk demo tugas kuliah, gunakan link frontend dari Render.

### 7. Tentang Pembuat
Aplikasi ini dibuat oleh:
- **Ahmad Surya Bimantara**
- **Abdullah Sallam**

Mahasiswa Teknik Informatika, UNISNU Jepara.

## Cara Menjalankan

Panduan lengkap akan ditulis setelah implementasi selesai. 