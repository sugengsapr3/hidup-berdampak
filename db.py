"""
Lapisan database (PostgreSQL via Neon) untuk HIDUP. BERDAMPAK.

Menyimpan:
- users        : pengguna yang login (dari Google)
- courses      : daftar kelas + harga
- enrollments  : catatan siapa punya akses kelas apa (setelah bayar)

Desain:
- Koneksi dibuat per-operasi (cocok untuk serverless Vercel).
- Semua query pakai parameter (aman dari SQL injection).
- init_db() membuat tabel bila belum ada, dan mengisi kelas awal (seed).
"""
import os

import psycopg

DATABASE_URL = os.environ.get("DATABASE_URL")


def _conn():
    """Buka koneksi baru ke database."""
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL belum di-set.")
    return psycopg.connect(DATABASE_URL)


def db_enabled():
    return bool(DATABASE_URL)


def init_db():
    """Buat tabel bila belum ada, lalu seed kelas awal. Aman dipanggil berulang."""
    with _conn() as conn, conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id          SERIAL PRIMARY KEY,
                email       TEXT UNIQUE NOT NULL,
                name        TEXT NOT NULL,
                picture     TEXT DEFAULT '',
                created_at  TIMESTAMPTZ DEFAULT now()
            );
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS courses (
                id          SERIAL PRIMARY KEY,
                slug        TEXT UNIQUE NOT NULL,
                title       TEXT NOT NULL,
                description TEXT DEFAULT '',
                price       INTEGER NOT NULL DEFAULT 0,
                created_at  TIMESTAMPTZ DEFAULT now()
            );
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS enrollments (
                id          SERIAL PRIMARY KEY,
                user_id     INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                course_id   INTEGER NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
                status      TEXT NOT NULL DEFAULT 'pending',
                created_at  TIMESTAMPTZ DEFAULT now(),
                UNIQUE (user_id, course_id)
            );
            """
        )
        # Pesanan/transaksi pembayaran (Midtrans).
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (
                id           SERIAL PRIMARY KEY,
                order_id     TEXT UNIQUE NOT NULL,
                email        TEXT NOT NULL,
                course_slug  TEXT NOT NULL,
                amount       INTEGER NOT NULL,
                status       TEXT NOT NULL DEFAULT 'pending',
                created_at   TIMESTAMPTZ DEFAULT now()
            );
            """
        )
        conn.commit()
    _seed_courses()


def _seed_courses():
    """Isi kelas awal bila tabel courses masih kosong."""
    seed = [
        ("dasar-hidup-berdampak", "Dasar Hidup Berdampak",
         "Fondasi membangun hidup yang bermakna: tujuan, kebiasaan, dan dampak.", 149000),
        ("financial-freedom-berkah", "Financial Freedom yang Berkah",
         "Mengelola keuangan, membangun aset, tanpa melupakan bekal akhirat.", 249000),
        ("keluarga-legacy", "Membangun Keluarga & Legacy",
         "Mewariskan nilai, mendidik anak, dan membangun warisan yang bertahan.", 199000),
    ]
    with _conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM courses;")
        count = cur.fetchone()[0]
        if count == 0:
            cur.executemany(
                "INSERT INTO courses (slug, title, description, price) VALUES (%s, %s, %s, %s);",
                seed,
            )
            conn.commit()


# ------------------------------------------------------------------ Users
def upsert_user(email, name, picture=""):
    """Simpan/update user saat login. Kembalikan id user."""
    with _conn() as conn, conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO users (email, name, picture)
            VALUES (%s, %s, %s)
            ON CONFLICT (email) DO UPDATE SET name = EXCLUDED.name, picture = EXCLUDED.picture
            RETURNING id;
            """,
            (email, name, picture),
        )
        user_id = cur.fetchone()[0]
        conn.commit()
        return user_id


# ------------------------------------------------------------------ Courses
def list_courses():
    with _conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT slug, title, description, price FROM courses ORDER BY id;")
        rows = cur.fetchall()
    return [
        {"slug": r[0], "title": r[1], "description": r[2], "price": r[3]}
        for r in rows
    ]


def get_course(slug):
    with _conn() as conn, conn.cursor() as cur:
        cur.execute(
            "SELECT slug, title, description, price FROM courses WHERE slug = %s;",
            (slug,),
        )
        r = cur.fetchone()
    if not r:
        return None
    return {"slug": r[0], "title": r[1], "description": r[2], "price": r[3]}


# ------------------------------------------------------------------ Enrollments
def enroll(email, course_slug, status="paid"):
    """Beri user akses ke kelas (status 'paid' setelah pembayaran)."""
    with _conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT id FROM users WHERE email = %s;", (email,))
        u = cur.fetchone()
        cur.execute("SELECT id FROM courses WHERE slug = %s;", (course_slug,))
        c = cur.fetchone()
        if not u or not c:
            return False
        cur.execute(
            """
            INSERT INTO enrollments (user_id, course_id, status)
            VALUES (%s, %s, %s)
            ON CONFLICT (user_id, course_id) DO UPDATE SET status = EXCLUDED.status;
            """,
            (u[0], c[0], status),
        )
        conn.commit()
        return True


def has_access(email, course_slug):
    """Cek apakah user sudah punya akses (status paid) ke sebuah kelas."""
    if not email:
        return False
    with _conn() as conn, conn.cursor() as cur:
        cur.execute(
            """
            SELECT e.status
            FROM enrollments e
            JOIN users u ON u.id = e.user_id
            JOIN courses c ON c.id = e.course_id
            WHERE u.email = %s AND c.slug = %s;
            """,
            (email, course_slug),
        )
        r = cur.fetchone()
    return bool(r and r[0] == "paid")


# ------------------------------------------------------------------ Orders
def create_order(order_id, email, course_slug, amount, status="pending"):
    """Catat pesanan baru sebelum diarahkan ke pembayaran."""
    with _conn() as conn, conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO orders (order_id, email, course_slug, amount, status)
            VALUES (%s, %s, %s, %s, %s);
            """,
            (order_id, email, course_slug, amount, status),
        )
        conn.commit()


def get_order(order_id):
    with _conn() as conn, conn.cursor() as cur:
        cur.execute(
            "SELECT order_id, email, course_slug, amount, status FROM orders WHERE order_id = %s;",
            (order_id,),
        )
        r = cur.fetchone()
    if not r:
        return None
    return {"order_id": r[0], "email": r[1], "course_slug": r[2], "amount": r[3], "status": r[4]}


def set_order_status(order_id, status):
    with _conn() as conn, conn.cursor() as cur:
        cur.execute(
            "UPDATE orders SET status = %s WHERE order_id = %s;",
            (status, order_id),
        )
        conn.commit()


def my_courses(email):
    """Daftar kelas yang sudah dimiliki user."""
    if not email:
        return []
    with _conn() as conn, conn.cursor() as cur:
        cur.execute(
            """
            SELECT c.slug, c.title, e.status
            FROM enrollments e
            JOIN users u ON u.id = e.user_id
            JOIN courses c ON c.id = e.course_id
            WHERE u.email = %s
            ORDER BY e.created_at DESC;
            """,
            (email,),
        )
        rows = cur.fetchall()
    return [{"slug": r[0], "title": r[1], "status": r[2]} for r in rows]
