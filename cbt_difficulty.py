"""Server-owned per-difficulty breakdown for 30-item SPLDV CBTs.

Older attempts lack answer-level data and are deliberately not backfilled.
"""
LEVELS = ("Mudah", "Sedang", "Sulit")
TOPIC = "Matematika - SPLDV"
PASSING_GRADE = 75

def levels_for_manifest(manifest):
    if not isinstance(manifest, dict):
        return None
    keys = manifest.get("answer_keys")
    if not isinstance(keys, list):
        return None
    declared = manifest.get("question_levels")
    if isinstance(declared, list) and len(declared) == len(keys):
        if all(level in LEVELS for level in declared):
            return declared
        return None
    # Compatibility only for previously published 30-item SPLDV packages.
    if manifest.get("subject") == TOPIC and len(keys) == 30:
        return ["Mudah"] * 10 + ["Sedang"] * 10 + ["Sulit"] * 10
    return None

def ensure_table(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS cbt_difficulty_scores (
            result_id INTEGER NOT NULL
                REFERENCES learning_results(id) ON DELETE CASCADE,
            difficulty TEXT NOT NULL CHECK (difficulty IN ('Mudah','Sedang','Sulit')),
            correct_count INTEGER NOT NULL CHECK (correct_count >= 0),
            total_questions INTEGER NOT NULL CHECK (total_questions > 0),
            PRIMARY KEY (result_id, difficulty)
        )
    """)

def insert_scores(cur, result_id, manifest, answers):
    """Only server-calculated answers are accepted. Idempotent on result_id."""
    levels = levels_for_manifest(manifest)
    if levels is None:
        return False
    keys = manifest["answer_keys"]
    if len(answers) != len(keys):
        return False
    counts = {level: [0, 0] for level in LEVELS}
    for level, answer, key in zip(levels, answers, keys):
        counts[level][1] += 1
        if answer == key:
            counts[level][0] += 1
    ensure_table(cur)
    for level in LEVELS:
        correct, total = counts[level]
        if total:
            cur.execute("""
                INSERT INTO cbt_difficulty_scores
                  (result_id, difficulty, correct_count, total_questions)
                VALUES (%s,%s,%s,%s)
                ON CONFLICT (result_id,difficulty) DO NOTHING
            """, (result_id, level, correct, total))
    return True

def recommendation(level, percent):
    """Instructional guidance, not a claim about a formal passing grade."""
    if level == "Mudah":
        if percent < PASSING_GRADE:
            return "Ulangi konsep variabel, pasangan solusi, dan eliminasi sederhana; kerjakan 10 latihan dasar."
        return "Pertahankan akurasi persamaan dan pemeriksaan substitusi."
    if level == "Sedang":
        if percent < 70:
            return "Latih eliminasi-substitusi dan operasi bilangan; kerjakan 10 latihan bertahap."
        return "Lanjutkan latihan kombinasi eliminasi dan substitusi."
    if percent < 70:
        return "Berlatih mengubah soal cerita menjadi dua persamaan, lalu periksa satuan dan hasil."
    return "Coba soal cerita SPLDV dengan konteks baru dan batas waktu."
