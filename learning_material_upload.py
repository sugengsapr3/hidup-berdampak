"""Bounded text extraction for Admin-uploaded learning material.

Raw uploads are processed in memory and not persisted. Only extracted text is
saved in question_bank_drafts.source_material.
"""
import io
from pathlib import Path

MAX_UPLOAD_BYTES = 3 * 1024 * 1024
MAX_EXTRACT_CHARS = 24000
MAX_PDF_PAGES = 35
ALLOWED = (".pdf", ".docx", ".txt")

def extract_material(file_storage):
    if not file_storage or not file_storage.filename:
        raise ValueError("Pilih file materi PDF, DOCX, atau TXT.")
    name = Path(file_storage.filename.replace("\\", "/")).name[:120]
    ext = Path(name).suffix.lower()
    if ext not in ALLOWED:
        raise ValueError("Format harus PDF, DOCX, atau TXT.")
    raw = file_storage.stream.read(MAX_UPLOAD_BYTES + 1)
    if not raw or len(raw) > MAX_UPLOAD_BYTES:
        raise ValueError("Ukuran file harus 1 byte sampai 3 MB.")
    try:
        if ext == ".txt":
            text = raw.decode("utf-8-sig")
        elif ext == ".pdf":
            if not raw.startswith(b"%PDF-"):
                raise ValueError("File bukan PDF yang valid.")
            from pypdf import PdfReader
            reader = PdfReader(io.BytesIO(raw), strict=False)
            if reader.is_encrypted:
                raise ValueError("PDF terkunci; unggah PDF tanpa kata sandi.")
            if len(reader.pages) > MAX_PDF_PAGES:
                raise ValueError("PDF melebihi batas 35 halaman.")
            text = "\n".join(page.extract_text() or "" for page in reader.pages)
        else:
            if not raw.startswith(b"PK"):
                raise ValueError("File bukan DOCX yang valid.")
            from docx import Document
            doc = Document(io.BytesIO(raw))
            chunks = [p.text for p in doc.paragraphs]
            for table in doc.tables:
                for row in table.rows:
                    chunks.append(" | ".join(c.text for c in row.cells))
            text = "\n".join(chunks)
    except (UnicodeDecodeError, OSError, KeyError, RuntimeError) as exc:
        raise ValueError("Gagal membaca file materi. Periksa apakah file rusak.") from exc
    text = "\n".join(line.strip() for line in text.splitlines() if line.strip()).strip()
    if len(text) < 100:
        raise ValueError("Teks materi terlalu sedikit atau berupa scan/gambar. Gunakan PDF berbasis teks, DOCX, atau tempel materi.")
    if len(text) > MAX_EXTRACT_CHARS:
        raise ValueError("Materi terlalu panjang (maksimal 24.000 karakter ekstraksi). Pisahkan menjadi beberapa bab.")
    return name, text
