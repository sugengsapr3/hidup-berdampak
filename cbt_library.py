"""Admin-only HTML CBT library, isolated from the site's origin."""
import hmac
import re
import secrets
import uuid
import json

from flask import Blueprint, abort, current_app, make_response, redirect, render_template_string, render_template, request, session, url_for

from db import _conn, db_enabled
from cbt_result_handler import signer, save_result

bp = Blueprint("cbt_library", __name__, url_prefix="/generasi-berdampak/learninghub")

CHILDREN = {"dzaky": "Dzaky", "hadziq": "Hadziq", "fiori": "Fiori", "hazel": "Hazel"}
MAX_HTML_BYTES = 350_000

def _manifest(html):
    # Manifest is an exact marker emitted by the standard ChatGPT CBT template.
    marker = '<script id="hb-cbt-manifest" type="application/json">'
    if marker not in html or '</script>' not in html.split(marker, 1)[1]:
        return None
    raw = html.split(marker, 1)[1].split('</script>', 1)[0]
    try:
        value = json.loads(raw)
        keys = value.get("answer_keys")
        if not isinstance(keys, list) or not (1 <= len(keys) <= 200):
            return None
        if any(key not in ("A", "B", "C", "D", "E") for key in keys):
            return None
        return {"answer_keys": keys, "subject": str(value.get("subject", "CBT"))[:100]}
    except (ValueError, TypeError, AttributeError):
        return None

def _table():
    with _conn() as conn, conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS cbt_html_packages (
                id UUID PRIMARY KEY,
                title VARCHAR(160) NOT NULL,
                child_slug VARCHAR(30) NOT NULL,
                html_content TEXT NOT NULL,
                published BOOLEAN NOT NULL DEFAULT FALSE,
                created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                answer_keys JSONB
            )
        """)
        cur.execute("ALTER TABLE cbt_html_packages ADD COLUMN IF NOT EXISTS answer_keys JSONB")
        conn.commit()

def _admin():
    from flask import session
    user = session.get("user") or {}
    email = (user.get("email") or "").strip().lower()
    from os import environ
    admins = [x.strip().lower() for x in environ.get("ADMIN_EMAILS", "sugengsapr3@gmail.com").split(",")]
    return bool(email) and email in admins

def _token():
    if "cbt_upload_csrf" not in session:
        session["cbt_upload_csrf"] = secrets.token_urlsafe(24)
    return session["cbt_upload_csrf"]

def _verify_token():
    return hmac.compare_digest(str(request.form.get("csrf", "")), _token())

MANAGER = """
<!doctype html><html lang="id"><meta charset="utf-8"><meta name="viewport" content="width=device-width">
<title>Kelola CBT HTML | Hidup Berdampak</title>
<style>body{background:#0d1420;color:#f6f8fd;font:16px system-ui;margin:0;padding:28px}main{max-width:850px;margin:auto}h1{margin-bottom:8px}a{color:#ffd17b}p,small{color:#bdc8db}form,article{background:#1a2538;border:1px solid #38445b;border-radius:12px;padding:20px;margin:20px 0}input,select,button{font:inherit;padding:10px;border-radius:7px;border:0;margin:5px 0}input[type=text]{width:min(96%,600px)}button{cursor:pointer;background:#f5b94c;font-weight:700}li{margin:12px 0}label{display:block;margin:12px 0} .danger{color:#ffd2d2}</style>
<main><p><a href="/generasi-berdampak/learninghub/dashboard">← Parent Dashboard</a></p><h1>Kelola CBT HTML</h1><p>Upload file HTML hasil ChatGPT. Hanya Admin bisa mengunggah atau menerbitkan. Semua CBT baru diawali sebagai Draft.</p>
{% if error %}<p class="danger">{{error}}</p>{% endif %}
<form method="post" enctype="multipart/form-data">
<input type="hidden" name="csrf" value="{{csrf}}">
<label>Judul ujian <input type="text" name="title" maxlength="160" required placeholder="Contoh: Tryout Trensains 2"></label>
<label>Untuk anak <select name="child_slug">{% for slug,name in children.items() %}<option value="{{slug}}">{{name}}</option>{% endfor %}</select></label>
<label>File HTML (.html, maksimal 350 KB) <input type="file" name="html_file" accept=".html,text/html" required></label>
<button type="submit">Upload sebagai Draft</button>
</form>
<h2>Daftar CBT ({{items|length}})</h2>
{% if not items %}<p>Belum ada CBT baru yang diunggah.</p>{% endif %}
{% for item in items %}
<article><strong>{{item.title}}</strong> — {{children.get(item.child_slug,item.child_slug)}} <small>({{"Aktif" if item.published else "Draft"}} · {{"Nilai terintegrasi" if item.integrated else "Belum integrasi nilai"}})</small>
<p><a href="{{url_for('cbt_library.view',exam_id=item.id)}}" target="_blank" rel="noopener">Pratinjau CBT</a>{% if item.published %} · <a href="{{url_for('cbt_library.view',exam_id=item.id)}}">Link siswa</a>{% endif %}</p>
<form method="post" action="{{url_for('cbt_library.toggle',exam_id=item.id)}}" style="padding:0;border:0;background:none;margin:0">
<input type="hidden" name="csrf" value="{{csrf}}"><button type="submit">{{"Nonaktifkan" if item.published else "Publish CBT"}}</button></form>
</article>{% endfor %}
<p><small>File HTML ditampilkan terisolasi. Nilai otomatis hanya untuk HTML dengan manifest standar integrasi. HTML lama tetap dapat dijalankan.</small></p>
</main></html>
"""

def _list_items():
    with _conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, title, child_slug, published, answer_keys IS NOT NULL FROM cbt_html_packages ORDER BY created_at DESC")
        rows = cur.fetchall()
    return [dict(id=str(r[0]), title=r[1], child_slug=r[2], published=r[3], integrated=r[4]) for r in rows]

@bp.route("/cbt-manager", methods=["GET", "POST"])
def manager():
    if not _admin():
        abort(403)
    if not db_enabled():
        return "Database belum diaktifkan", 503
    _table()
    error = None
    if request.method == "POST":
        if not _verify_token():
            abort(400)
        title = request.form.get("title", "").strip()
        slug = request.form.get("child_slug", "")
        f = request.files.get("html_file")
        if not title or len(title) > 160 or slug not in CHILDREN or not f or not f.filename.lower().endswith(".html"):
            error = "Isi judul, pilih anak, dan upload file .html."
        else:
            raw = f.stream.read(MAX_HTML_BYTES + 1)
            if len(raw) > MAX_HTML_BYTES:
                error = "HTML terlalu besar (maksimal 350 KB)."
            else:
                try:
                    html = raw.decode("utf-8-sig")
                except UnicodeDecodeError:
                    error = "Simpan HTML dalam encoding UTF-8."
                else:
                    if not re.search(r"<html\b|<!doctype\s+html", html, re.I):
                        error = "File tidak tampak seperti dokumen HTML lengkap."
                    else:
                        with _conn() as conn, conn.cursor() as cur:
                            cur.execute("INSERT INTO cbt_html_packages (id,title,child_slug,html_content,answer_keys) VALUES (%s,%s,%s,%s,%s)",
                                        (uuid.uuid4(), title, slug, html, json.dumps(_manifest(html)) if _manifest(html) else None))
                            conn.commit()
                        return redirect(url_for("cbt_library.manager"))
    response = make_response(render_template_string(MANAGER, csrf=_token(), children=CHILDREN, items=_list_items(), error=error))
    response.headers["Cache-Control"] = "private, no-store"
    return response

@bp.post("/cbt-manager/<uuid:exam_id>/publish")
def toggle(exam_id):
    if not _admin():
        abort(403)
    if not _verify_token():
        abort(400)
    _table()
    with _conn() as conn, conn.cursor() as cur:
        cur.execute("UPDATE cbt_html_packages SET published=NOT published WHERE id=%s", (exam_id,))
        conn.commit()
    return redirect(url_for("cbt_library.manager"))

@bp.get("/cbt/<uuid:exam_id>")
def view(exam_id):
    if not db_enabled():
        abort(503)
    _table()
    with _conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT title, child_slug, published, answer_keys IS NOT NULL FROM cbt_html_packages WHERE id=%s", (exam_id,))
        exam = cur.fetchone()
    if not exam or (not exam[2] and not _admin()):
        abort(404)
    resp = make_response(render_template(
        "LeaningHub/cbt_shell.html",
        title=exam[0], child=CHILDREN.get(exam[1], exam[1]),
        exam_id=exam_id, integrated=exam[3],
        token=signer().dumps({"exam": str(exam_id)}),
    ))
    resp.headers["Cache-Control"] = "private, no-store"
    resp.headers["X-Robots-Tag"] = "noindex, nofollow"
    return resp


@bp.post("/cbt/<uuid:exam_id>/result")
def result(exam_id):
    if not db_enabled():
        return {"error": "Database tidak tersedia"}, 503
    _table()
    return save_result(exam_id, _admin())


@bp.get("/cbt/<uuid:exam_id>/content")
def content(exam_id):
    if not db_enabled():
        abort(503)
    _table()
    with _conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT html_content, published FROM cbt_html_packages WHERE id=%s", (exam_id,))
        record = cur.fetchone()
    if record is None or (not record[1] and not _admin()):
        abort(404)
    # HTML remains inside a CSP-enforced unique sandbox origin. Uploaded scripts
    # cannot access website cookies, localStorage, forms or API endpoints.
    resp = make_response(record[0])
    resp.headers["Content-Type"] = "text/html; charset=utf-8"
    resp.headers["Content-Security-Policy"] = (
        "sandbox allow-scripts; default-src 'none'; script-src 'unsafe-inline'; "
        "style-src 'unsafe-inline'; img-src data: https:; font-src data:; "
        "connect-src 'none'; form-action 'none'; base-uri 'none'"
    )
    resp.headers["Cache-Control"] = "no-store"
    resp.headers["X-Content-Type-Options"] = "nosniff"
    resp.headers["X-Robots-Tag"] = "noindex, nofollow"
    return resp
