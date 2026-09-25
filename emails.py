"""
Pengiriman email notifikasi via Resend (HTTP API, cocok untuk serverless Vercel).

Dipakai saat pembayaran kelas berhasil:
- Email ke PEMBELI  : konfirmasi akses kelas.
- Email ke ADMIN    : info ada pembelian (email pembeli, kelas, jumlah).

Konfigurasi via environment:
- RESEND_API_KEY : API key dari resend.com (wajib agar email terkirim)
- EMAIL_FROM      : alamat pengirim (default onboarding@resend.dev sebelum domain sendiri)
- ADMIN_EMAIL     : tujuan notifikasi admin (default hidup.berdampak.media@gmail.com)

Aman: bila RESEND_API_KEY belum di-set, fungsi tidak error, hanya melewati kirim.
"""
import os

import requests

RESEND_API_KEY = os.environ.get("RESEND_API_KEY", "").strip()
EMAIL_FROM = os.environ.get("EMAIL_FROM", "HIDUP BERDAMPAK <onboarding@resend.dev>").strip()
ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL", "hidup.berdampak.media@gmail.com").strip()

_RESEND_ENDPOINT = "https://api.resend.com/emails"


def emails_enabled():
    return bool(RESEND_API_KEY)


def _rupiah(amount):
    try:
        return "Rp " + f"{int(amount):,}".replace(",", ".")
    except Exception:
        return f"Rp {amount}"


def _send(to, subject, html):
    """Kirim satu email. Kembalikan (ok, error). Tidak melempar exception."""
    if not RESEND_API_KEY:
        return False, "RESEND_API_KEY belum di-set."
    try:
        resp = requests.post(
            _RESEND_ENDPOINT,
            headers={
                "Authorization": f"Bearer {RESEND_API_KEY}",
                "Content-Type": "application/json",
            },
            json={"from": EMAIL_FROM, "to": [to], "subject": subject, "html": html},
            timeout=15,
        )
        if resp.status_code in (200, 201):
            return True, None
        return False, f"Resend {resp.status_code}: {resp.text}"
    except Exception as e:
        return False, repr(e)


def send_purchase_emails(buyer_email, buyer_name, course_title, amount):
    """Kirim email ke pembeli & admin setelah pembayaran berhasil.

    Mengembalikan dict berisi status masing-masing (untuk logging).
    Tidak pernah melempar exception agar tidak mengganggu alur webhook.
    """
    result = {"buyer": None, "admin": None}
    if not RESEND_API_KEY:
        return result

    nama = buyer_name or buyer_email.split("@")[0]
    harga = _rupiah(amount)

    # --- Email ke PEMBELI ---
    buyer_html = f"""
    <div style="font-family:Arial,sans-serif;max-width:520px;margin:auto;color:#1d1d1f">
      <h2 style="color:#0f1115">Pembayaran Berhasil 🌱</h2>
      <p>Halo {nama},</p>
      <p>Terima kasih. Pembayaranmu untuk kelas
         <strong>{course_title}</strong> sebesar <strong>{harga}</strong>
         telah kami terima.</p>
      <p>Kamu sekarang sudah punya akses penuh ke kelas ini. Buka lewat halaman
         Akun kamu:</p>
      <p>
        <a href="https://hidupberdampak.vercel.app/akun"
           style="background:#D9A441;color:#17130A;padding:12px 22px;border-radius:10px;
                  text-decoration:none;font-weight:bold">Buka Kelas Saya</a>
      </p>
      <p style="color:#6b7280;font-size:13px;margin-top:24px">
        HIDUP. BERDAMPAK — Live with Purpose. Create Impact.
      </p>
    </div>
    """
    ok, err = _send(buyer_email, f"Pembayaran berhasil — {course_title}", buyer_html)
    result["buyer"] = "ok" if ok else f"gagal: {err}"

    # --- Email ke ADMIN ---
    admin_html = f"""
    <div style="font-family:Arial,sans-serif;max-width:520px;margin:auto;color:#1d1d1f">
      <h2 style="color:#0f1115">Pembelian Kelas Baru 💰</h2>
      <p>Ada pembayaran kelas yang berhasil:</p>
      <table style="border-collapse:collapse;width:100%">
        <tr><td style="padding:6px 0;color:#6b7280">Kelas</td>
            <td style="padding:6px 0"><strong>{course_title}</strong></td></tr>
        <tr><td style="padding:6px 0;color:#6b7280">Pembeli</td>
            <td style="padding:6px 0">{nama} ({buyer_email})</td></tr>
        <tr><td style="padding:6px 0;color:#6b7280">Jumlah</td>
            <td style="padding:6px 0"><strong>{harga}</strong></td></tr>
      </table>
      <p style="color:#6b7280;font-size:13px;margin-top:24px">
        Notifikasi otomatis dari hidupberdampak.vercel.app
      </p>
    </div>
    """
    ok2, err2 = _send(ADMIN_EMAIL, f"[Pembelian] {course_title} — {harga}", admin_html)
    result["admin"] = "ok" if ok2 else f"gagal: {err2}"

    return result
