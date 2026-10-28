# Format standar CBT HTML — HIDUP BERDAMPAK

Status: **rancangan integrasi, belum aktif**.

## Aturan penting

- File HTML lama tetap dapat diunggah dan dijalankan, tetapi nilainya belum otomatis masuk Parent Dashboard.
- Untuk file CBT baru, ChatGPT harus menghasilkan 1 file HTML lengkap dengan soal, navigasi, timer, dan kemampuan menghitung jawaban.
- Kunci jawaban harus diproses dan divalidasi oleh server sebelum nilai disimpan; server tidak boleh menerima begitu saja angka nilai dari HTML.
- HTML yang diunggah berjalan terisolasi; jangan mengizinkan akses langsung ke session Admin atau rahasia API.
- Setiap pengerjaan mempunyai `attempt_id` UUID yang stabil agar penyimpanan ulang tidak menyebabkan nilai ganda.
- Sesudah soal selesai, browser mengirim pilihan jawaban A–E dan attempt ID; server menghitung nilai dan mencatatnya ke `learning_results`.
- Untuk HTML yang belum mengikuti format standar, sistem harus menampilkan peringatan bahwa nilai belum terintegrasi.

## Tahapan peluncuran

1. Tetapkan manifest metadata dan kunci jawaban di database saat upload.
2. Tambahkan jembatan komunikasi aman antara HTML terisolasi dan API penilaian.
3. Pastikan hasil masuk Neon Preview dan terlihat di Parent Dashboard Preview.
4. Baru buat pull request ke `main`, setelah pengujian dan pemeriksaan keamanan.

Jangan klaim nilai CBT HTML baru sudah otomatis tersimpan sebelum langkah 1–3 selesai dan diuji.
