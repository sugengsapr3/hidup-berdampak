"""
Integrasi pembayaran Midtrans (Snap) untuk HIDUP. BERDAMPAK.

- create_snap_transaction(): buat transaksi, kembalikan redirect_url ke halaman bayar.
- verify_signature(): verifikasi keaslian notifikasi webhook dari Midtrans.

Konfigurasi via environment:
- MIDTRANS_SERVER_KEY : kunci rahasia server (dari dashboard Midtrans)
- MIDTRANS_IS_PRODUCTION : "1" untuk produksi, selain itu sandbox (default sandbox)

Aman dipanggil walau key belum di-set: is_enabled() mengembalikan False.
"""
import os
import hashlib
import base64

import requests

MIDTRANS_SERVER_KEY = os.environ.get("MIDTRANS_SERVER_KEY", "").strip()
IS_PRODUCTION = os.environ.get("MIDTRANS_IS_PRODUCTION", "").strip() == "1"

_SNAP_BASE = (
    "https://app.midtrans.com/snap/v1/transactions"
    if IS_PRODUCTION
    else "https://app.sandbox.midtrans.com/snap/v1/transactions"
)


def is_enabled():
    return bool(MIDTRANS_SERVER_KEY)


def _auth_header():
    # Midtrans pakai HTTP Basic: server_key sebagai username, password kosong.
    token = base64.b64encode(f"{MIDTRANS_SERVER_KEY}:".encode()).decode()
    return {"Authorization": f"Basic {token}", "Content-Type": "application/json", "Accept": "application/json"}


def create_snap_transaction(order_id, amount, item_name, email, name):
    """Buat transaksi Snap. Kembalikan (redirect_url, error)."""
    if not is_enabled():
        return None, "Pembayaran belum dikonfigurasi."
    payload = {
        "transaction_details": {"order_id": order_id, "gross_amount": amount},
        "item_details": [
            {"id": order_id, "price": amount, "quantity": 1, "name": item_name[:50]}
        ],
        "customer_details": {"first_name": name[:50], "email": email},
        "credit_card": {"secure": True},
    }
    try:
        resp = requests.post(_SNAP_BASE, json=payload, headers=_auth_header(), timeout=20)
        if resp.status_code not in (200, 201):
            return None, f"Midtrans error {resp.status_code}: {resp.text}"
        return resp.json().get("redirect_url"), None
    except Exception as e:
        return None, repr(e)


def verify_signature(order_id, status_code, gross_amount, signature_key):
    """Verifikasi signature notifikasi Midtrans.

    Rumus: SHA512(order_id + status_code + gross_amount + server_key)
    """
    if not MIDTRANS_SERVER_KEY:
        return False
    raw = f"{order_id}{status_code}{gross_amount}{MIDTRANS_SERVER_KEY}"
    expected = hashlib.sha512(raw.encode()).hexdigest()
    return expected == signature_key
