// Modal info pembuat
const infoBtn = document.getElementById('info-btn');
const infoModal = document.getElementById('info-modal');
const closeModal = document.querySelector('.close');

infoBtn.onclick = () => {
    infoModal.style.display = 'flex';
};
closeModal.onclick = () => {
    infoModal.style.display = 'none';
};
window.onclick = (event) => {
    if (event.target === infoModal) {
        infoModal.style.display = 'none';
    }
};

// Placeholder: upload form
const uploadForm = document.getElementById('upload-form');
const fileInput = document.getElementById('file-input');
const compressBtn = document.getElementById('compress-btn');
const progressBar = document.getElementById('progress-bar');
const downloadLink = document.getElementById('download-link');
const notification = document.getElementById('notification');
const selectedFile = document.getElementById('selected-file');

function formatBytes(bytes) {
    if (bytes === 0) return '0 B';
    const k = 1024;
    const sizes = ['B', 'KB', 'MB', 'GB', 'TB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

function ellipsis(str, max = 30) {
    return str.length > max ? str.slice(0, max) + '...' : str;
}

function addSuffixToFilename(filename, suffix = '(1)') {
    const dotIdx = filename.lastIndexOf('.');
    if (dotIdx === -1) return filename + suffix;
    return filename.slice(0, dotIdx) + suffix + filename.slice(dotIdx);
}

uploadForm.onsubmit = async (e) => {
    e.preventDefault();
    notification.textContent = '';
    progressBar.style.display = 'block';
    progressBar.innerHTML = '<div class="progress-bar"><div class="progress-bar-inner" id="progress-inner"></div></div>';
    downloadLink.style.display = 'none';

    const file = fileInput.files[0];
    if (!file) {
        notification.textContent = 'Pilih file terlebih dahulu!';
        progressBar.style.display = 'none';
        return;
    }

    // Tampilkan nama file yang dikompres
    notification.innerHTML = `<span class='filename'>${ellipsis(file.name, 30)}</span> sedang dikompres...`;

    const formData = new FormData();
    formData.append('file', file);

    // Progress bar animasi loading
    let progress = 0;
    const progressInner = document.getElementById('progress-inner');
    const progressInterval = setInterval(() => {
        progress = Math.min(progress + Math.random() * 20, 95);
        if (progressInner) progressInner.style.width = progress + '%';
    }, 300);

    try {
        const response = await fetch('http://localhost:5000/compress', {
            method: 'POST',
            body: formData
        });
        clearInterval(progressInterval);
        if (progressInner) progressInner.style.width = '100%';
        if (!response.ok) {
            const err = await response.json();
            throw new Error(err.error || 'Gagal kompres file');
        }
        const blob = await response.blob();
        const contentDisp = response.headers.get('Content-Disposition');
        let filename = 'hasil_kompresi';
        if (contentDisp && contentDisp.includes('filename=')) {
            filename = contentDisp.split('filename=')[1].replace(/"/g, '');
        }
        let originalName = file.name;
        let downloadName = addSuffixToFilename(originalName, '(1)');
        if (filename.endsWith('.zip')) {
            downloadName = addSuffixToFilename(originalName, '(1)') + '.zip';
        }
        const url = window.URL.createObjectURL(blob);
        downloadLink.href = url;
        downloadLink.download = downloadName;
        downloadLink.textContent = 'Download';
        downloadLink.style.display = 'inline-block';

        // Hitung pengurangan ukuran file
        const originalSize = file.size;
        const newSize = blob.size;
        const percent = originalSize > 0 ? (((originalSize - newSize) / originalSize) * 100).toFixed(1) : 0;
        let info = `Ukuran awal: ${formatBytes(originalSize)} | Ukuran akhir: ${formatBytes(newSize)} | Pengurangan: ${percent}%`;

        // Notifikasi khusus jika file dokumen di-zip
        if (filename.endsWith('.zip')) {
            info += '<br><span style="color:#ffd54f">File dokumen dikompres ke ZIP. Silakan ekstrak untuk mendapatkan file aslinya.</span>';
        }
        notification.innerHTML = `<span class='filename'>${ellipsis(downloadName, 30)}</span> berhasil dikompres!<br>${info}`;
    } catch (err) {
        clearInterval(progressInterval);
        notification.textContent = err.message.includes('ffmpeg') ? 'Gagal kompres video: ffmpeg belum terinstall atau terjadi error.' : err.message;
        downloadLink.style.display = 'none';
    }
};

fileInput.onchange = () => {
    if (fileInput.files.length > 0) {
        selectedFile.textContent = ellipsis(fileInput.files[0].name, 30);
    } // Jangan ubah apapun jika user batal memilih file
}; 