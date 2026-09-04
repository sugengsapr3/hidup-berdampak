# HIDUP. BERDAMPAK

Website brand "HIDUP. BERDAMPAK" dibuat dengan Python + Flask.

## Menjalankan secara lokal

```bash
pip install -r requirements.txt
python app.py
```

Buka http://127.0.0.1:5000

## Deploy ke Vercel (gratis)

Aplikasi ini siap deploy ke Vercel dengan zero-config. Vercel otomatis
mengenali instance Flask bernama `app` di `app.py`.

### Langkah

1. Buat akun di https://github.com dan https://vercel.com
   (login Vercel dengan "Continue with GitHub").
2. Buat repository baru di GitHub, lalu upload semua file proyek ini
   (sertakan folder `static/` dan `templates/`; abaikan `__pycache__/`).
3. Di Vercel: **Add New -> Project**, pilih repo tadi, klik **Deploy**.
4. Setelah live, buka **Settings -> Domains** untuk mengatur subdomain,
   misalnya `hidupberdampak.vercel.app` (jika masih tersedia).

## Struktur

```
.
├── app.py            # entrypoint Flask (instance `app`)
├── data.py           # konten situs
├── requirements.txt  # dependensi (Flask)
├── pyproject.toml    # metadata proyek + versi Python
├── static/css/       # stylesheet
└── templates/        # halaman HTML
```
