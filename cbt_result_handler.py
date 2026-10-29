"""Server-side scoring for uploaded CBT files. Never accept browser scores."""
import uuid

from flask import current_app, request
from itsdangerous import URLSafeTimedSerializer, BadSignature
from db import _conn


def signer():
    return URLSafeTimedSerializer(current_app.secret_key, salt="cbt-html-result-v1")


def save_result(exam_id, is_admin):
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return {"error": "Data JSON tidak valid"}, 400
    try:
        ticket = signer().loads(str(payload.get("token", "")), max_age=14400)
        if ticket.get("exam") != str(exam_id):
            return {"error": "Token ujian tidak cocok"}, 403
        attempt_id = uuid.UUID(str(payload.get("attempt_id")))
    except (BadSignature, ValueError, TypeError, AttributeError):
        return {"error": "Token atau ID ujian tidak valid"}, 403

    answers = payload.get("answers")
    if not isinstance(answers, list) or len(answers) > 200:
        return {"error": "Format jawaban tidak valid"}, 400

    with _conn() as conn, conn.cursor() as cur:
        cur.execute(
            "SELECT title,child_slug,published,answer_keys FROM cbt_html_packages WHERE id=%s",
            (exam_id,),
        )
        exam = cur.fetchone()
        if not exam or (not exam[2] and not is_admin):
            return {"error": "Ujian tidak tersedia"}, 404
        title, child, published, manifest = exam
        if not isinstance(manifest, dict) or "answer_keys" not in manifest:
            return {"error": "CBT ini belum memakai standar integrasi nilai"}, 422
        keys = manifest["answer_keys"]
        if len(answers) != len(keys):
            return {"error": "Jumlah jawaban tidak sesuai soal"}, 400
        if any(a is not None and a not in ("A", "B", "C", "D", "E") for a in answers):
            return {"error": "Pilihan jawaban tidak valid"}, 400
        correct = sum(a == k for a, k in zip(answers, keys))
        score = round(correct * 100 / len(keys), 2)
        cur.execute(
            """INSERT INTO learning_results
               (attempt_id,child_slug,quiz_title,subject,score,correct_count,total_questions)
               VALUES (%s,%s,%s,%s,%s,%s,%s)
               ON CONFLICT (attempt_id) DO NOTHING""",
            (attempt_id, child, title, manifest.get("subject", "CBT"),
             score, correct, len(keys)),
        )
        inserted = cur.rowcount == 1
        conn.commit()
    return {"status": "saved" if inserted else "already_received",
            "score": score, "correct_count": correct,
            "total_questions": len(keys)}, 200
