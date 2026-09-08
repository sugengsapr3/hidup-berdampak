# Peta Situs — HIDUP. BERDAMPAK

Acuan pengembangan untuk setiap halaman/screen.
Domain live: **https://hidupberdampak.vercel.app**

Cara membaca tabel:
- **URL** = alamat halaman (tambahkan di depan dengan domain live)
- **Route** = nama fungsi di `app.py` (dipakai `url_for('nama')` di template)
- **Template** = file HTML di `templates/`
- **Sumber Data** = variabel di `data.py` yang mengisi halaman
- **Status** = tingkat kematangan untuk membantu prioritas pengembangan

---

## 1. Halaman Utama & Statis

| Halaman | URL | Route | Template | Sumber Data | Status |
|---|---|---|---|---|---|
| Beranda | `/` | `home` | `home.html` | `JOURNEYS`, `PILLARS` | Siap |
| Tentang | `/tentang` | `about` | `about.html` | `SITE`, `PILLARS` | Siap |
| Bergabung (newsletter) | `/bergabung` | `join` | `join.html` | `SITE.newsletter` | Siap (form belum kirim email) |
| Login | `/login` | `login` | `login.html` | - | Tampilan saja (belum ada autentikasi) |
| Pencarian | `/cari?q=...` | `search` | `search.html` | semua konten (index) | Berfungsi |
| 404 | (otomatis) | `not_found` | `404.html` | - | Siap |

---

## 2. Kelas

| Halaman | URL | Route | Template | Sumber Data | Status |
|---|---|---|---|---|---|
| Daftar Kelas | `/kelas` | `courses` | `courses.html` | `COURSES` | Siap |
| Detail Kelas | `/kelas/<slug>` | `course_detail` | `course_detail.html` | `COURSES` | Konten contoh (harga dummy) |

Slug kelas yang tersedia:
- `/kelas/sistem-produktif-30-hari`
- `/kelas/dasar-kebebasan-finansial`
- `/kelas/mulai-channel-youtube`

---

## 3. Tutorial

| Halaman | URL | Route | Template | Sumber Data | Status |
|---|---|---|---|---|---|
| Daftar Tutorial | `/tutorial` | `tutorials` | `tutorials.html` | `TUTORIAL_TOPICS` | Siap |
| Detail Tutorial | `/tutorial/<slug>` | `tutorial_detail` | `tutorial_detail.html` | `TUTORIAL_TOPICS` | Konten contoh |

Slug tutorial yang tersedia:
- `/tutorial/produktivitas`
- `/tutorial/keuangan`
- `/tutorial/pengembangan-diri`
- `/tutorial/konten`

Catatan: submenu dropdown "Tutorial" di navbar mengarah ke tiap detail di atas.

---

## 4. Perjalanan (tema reflektif brand)

| Halaman | URL | Route | Template | Sumber Data | Status |
|---|---|---|---|---|---|
| Daftar Perjalanan | `/perjalanan` | `journeys` | `journeys.html` | `JOURNEYS` | Siap |
| Detail Perjalanan | `/perjalanan/<slug>` | `journey_detail` | `journey_detail.html` | `JOURNEYS` | Siap |

Slug perjalanan yang tersedia:
- `/perjalanan/manusia-dan-lobang`
- `/perjalanan/financial-freedom`
- `/perjalanan/bekal-akhirat`
- `/perjalanan/keluarga-legacy`
- `/perjalanan/urat-malu`
- `/perjalanan/pengembangan-diri`

---

## 5. Lainnya

| Halaman | URL | Route | Template | Sumber Data | Status |
|---|---|---|---|---|---|
| Untuk Bisnis | `/untuk-bisnis` | `business` | `business.html` | `BUSINESS_OFFERS` | Konten contoh |
| Sumber Daya | `/sumber-daya` | `resources` | `resources.html` | `RESOURCES` | Konten contoh (belum ada file unduhan) |

---

## Struktur Navigasi (navbar)

Diatur oleh variabel `NAV` di `data.py`:

```
Kelas          -> /kelas
Untuk Bisnis   -> /untuk-bisnis
Tutorial  (v)  -> /tutorial   [dropdown: 4 topik -> /tutorial/<slug>]
Sumber Daya    -> /sumber-daya
Tentang        -> /tentang
[Login]        -> /login
[Search 🔍]    -> /cari
```

Footer memuat: tautan sosial media (`SITE.socials`) dan email (`SITE.email`).

---

## Panduan Cepat Pengembangan

**Menambah halaman baru:**
1. Tambah fungsi route di `app.py` dengan `@app.route("/path")`
2. Buat file template di `templates/`
3. (Opsional) tambah data di `data.py`
4. (Opsional) tambah ke `NAV` agar muncul di navbar

**Mengubah konten (tanpa sentuh kode):**
- Edit teks, judul, dan daftar di `data.py` — semua konten ditarik dari sana.

**Mengubah tampilan/gaya:**
- Semua gaya ada di `static/css/style.css`.
- Warna diatur lewat variabel di `:root` (mis. `--gold`, `--bg`).

**Menerbitkan perubahan (deploy):**
- Commit lalu `git push` ke GitHub `sugengsapr3/hidup-berdampak`.
- Vercel otomatis deploy ulang dalam ~1 menit.

---

## Prioritas Pengembangan yang Disarankan

Fitur yang masih "tampilan saja" dan bisa dimatangkan:
1. **Login/Autentikasi** — perlu database + manajemen akun & sesi.
2. **Form Bergabung & Login** — hubungkan ke layanan email / penyimpanan data.
3. **Sumber Daya** — sediakan file asli untuk diunduh.
4. **Konten Kelas & Tutorial** — ganti teks contoh dan harga dummy dengan data riil.
5. **Pencarian** — sudah berfungsi; bisa ditingkatkan (highlight kata, ranking).
