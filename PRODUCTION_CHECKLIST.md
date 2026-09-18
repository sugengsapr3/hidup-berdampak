# Checklist Pindah ke Production — HIDUP. BERDAMPAK

Panduan mengaktifkan pembayaran uang sungguhan (dari sandbox → production).
Status per bagian: ✅ sudah, ⏳ menunggu, ⬜ belum dikerjakan.

Domain live: https://hidupberdampak.vercel.app
Repo: github.com/sugengsapr3/hidup-berdampak (auto-deploy ke Vercel)

---

## A. Fondasi (SUDAH SELESAI)

- ✅ Situs live di Vercel + tersambung GitHub (auto-deploy saat push)
- ✅ Login Google (OAuth) berfungsi di production Google
- ✅ Database PostgreSQL (Neon) tersambung; tabel users, courses, enrollments, orders
- ✅ Sistem kelas berbayar: daftar kelas, detail, tombol beli
- ✅ Integrasi Midtrans: buat transaksi Snap + webhook /midtrans/notify + halaman selesai
- ✅ Kontrol akses: materi kelas hanya untuk yang sudah bayar
- ✅ Ruang belajar (modul/materi) per kelas
- ✅ Pembayaran SANDBOX teruji end-to-end (kelas masuk ke akun setelah bayar)
- ✅ Notification URL sandbox di-set: https://hidupberdampak.vercel.app/midtrans/notify
- ✅ Finish Redirect URL sandbox di-set: https://hidupberdampak.vercel.app/akun

---

## B. Menunggu pihak Midtrans (DI LUAR KENDALI KITA)

- ⏳ Business Review Midtrans di-approve
      Status terakhir: "In progress"
      Cek: dashboard Midtrans (mode Production) atau email sugengsapr3@gmail.com
      >> Tidak bisa lanjut ke bagian C sebelum ini APPROVED <<

---

## C. Saat Midtrans sudah APPROVED — aktifkan uang sungguhan (BELUM)

- ⬜ 1. Ambil Server Key PRODUCTION
       Dashboard Midtrans → ganti environment ke PRODUCTION →
       Settings → Access Keys → salin "Server Key" (format Mid-server-...)

- ⬜ 2. Pasang key production ke Vercel (bisa dibantu via CLI)
       - Ganti GOOGLE... (tidak perlu, itu Google)
       - Set MIDTRANS_SERVER_KEY = <server key production>
       - Set MIDTRANS_IS_PRODUCTION = 1   (ini yang mengalihkan ke server Midtrans asli)

- ⬜ 3. Set URL di dashboard PRODUCTION Midtrans (terpisah dari sandbox!)
       - Payment Notification URL: https://hidupberdampak.vercel.app/midtrans/notify
       - Finish Redirect URL:      https://hidupberdampak.vercel.app/akun

- ⬜ 4. Deploy ulang (push ke GitHub, Vercel auto-deploy)

- ⬜ 5. Verifikasi rekening bank untuk pencairan dana di dashboard Midtrans
       (Settings → Bank Account / Settlement). Wajib agar uang bisa cair.

- ⬜ 6. Tes 1 transaksi kecil dengan uang ASLI, pastikan:
       - Diarahkan kembali ke /akun setelah bayar
       - Kelas muncul di "Kelas Saya"
       - Dana tercatat di dashboard Midtrans (Balance)

---

## D. Menyiapkan produk (bisa dikerjakan kapan saja, TANPA nunggu Midtrans)

- ⬜ Isi materi/video kelas asli (ganti "Video segera hadir")
      Kirim ke pengembang: judul modul + link YouTube + catatan
      (video kelas berbayar sebaiknya di-set "Unlisted" di YouTube)
- ⬜ Sesuaikan judul, harga, deskripsi kelas dengan data riil
      (kelas sekarang: Dasar Hidup Berdampak 149rb, Financial Freedom Berkah 249rb,
       Keluarga & Legacy 199rb — masih data contoh)

---

## E. Kebersihan keamanan (disarankan, tidak mendesak)

- ✅ Rotate password database Neon (sudah di-reset, DATABASE_URL baru terpasang di Vercel, situs jalan normal)
- ⬜ (Sandbox key Midtrans tidak berisiko; nanti pakai key production yang baru)

---

## Catatan teknis penting

- Kode TIDAK perlu diubah untuk pindah ke production — cukup environment variable
  di Vercel (MIDTRANS_SERVER_KEY + MIDTRANS_IS_PRODUCTION=1).
- Sandbox & Production di Midtrans TERPISAH: key beda, URL notif/redirect harus
  di-set ulang di sisi production.
- Auto-deploy: setiap "git push" ke GitHub akan otomatis men-deploy ke Vercel.
