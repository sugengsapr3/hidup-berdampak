"""
Konten statis untuk website brand "HIDUP. BERDAMPAK".
Tema reflektif tentang makna hidup, warisan, dan pengembangan diri.
"""

SITE = {
    "name": "hidup.berdampak.id",
    "brand": "HIDUP. BERDAMPAK",
    "owner": "Abi Albarra",
    "first_name": "Abi",
    "role": "Gerakan tentang hidup yang bermakna dan berdampak",
    "hero_title": "HIDUP. BERDAMPAK",
    "hero_sub": (
        "Karena pada akhirnya, bukan berapa lama kita hidup yang penting. "
        "Tapi apa yang kita tinggalkan setelah kita pergi."
    ),
    # Manifesto penutup
    "closing": [
        "Suatu hari kita semua akan pergi.",
        "Pertanyaannya bukan apakah kita akan meninggalkan dunia.",
        "Pertanyaannya: apa yang kita tinggalkan?",
    ],
    "email": "hidup.berdampak.media@gmail.com",
    "youtube_url": "#",
    "socials": [
        {"label": "YouTube", "url": "#"},
        {"label": "Instagram", "url": "#"},
        {"label": "TikTok", "url": "#"},
        {"label": "X/Twitter", "url": "#"},
    ],
}

# Enam "Pilihan Perjalanan" di beranda
JOURNEYS = [
    {
        "slug": "manusia-dan-lobang",
        "emoji": "🕳️",
        "title": "MANUSIA DAN LOBANG",
        "desc": "Tentang jatuh, bangkit, dan memahami hidup.",
        "body": (
            "Setiap orang pernah terjatuh ke dalam lubangnya masing-masing. "
            "Yang membedakan bukan seberapa dalam kita jatuh, tapi seberapa "
            "kita mau belajar untuk bangkit dan memahami kenapa kita ada di "
            "sana. Perjalanan ini tentang menerima luka, memaknai kegagalan, "
            "dan tumbuh darinya."
        ),
    },
    {
        "slug": "financial-freedom",
        "emoji": "💰",
        "title": "FINANCIAL FREEDOM",
        "desc": "Membangun kebebasan finansial tanpa melupakan bekal akhirat.",
        "body": (
            "Kebebasan finansial bukan tujuan akhir, tapi alat untuk hidup "
            "lebih bermakna dan memberi lebih banyak. Perjalanan ini tentang "
            "mengelola harta dengan bijak, membangun sumber penghasilan, dan "
            "memastikan dunia tidak membuat kita lupa pada akhirat."
        ),
    },
    {
        "slug": "bekal-akhirat",
        "emoji": "🕌",
        "title": "BEKAL AKHIRAT",
        "desc": "Karena investasi terbaik tidak semuanya memberikan return di dunia.",
        "body": (
            "Ada investasi yang hasilnya tidak kita nikmati di dunia, tapi "
            "menjadi bekal yang paling berharga kelak. Perjalanan ini tentang "
            "amal yang mengalir, ilmu yang bermanfaat, dan niat yang lurus."
        ),
    },
    {
        "slug": "keluarga-legacy",
        "emoji": "👨‍👩‍👧‍👦",
        "title": "KELUARGA & LEGACY",
        "desc": "Apa yang akan kita wariskan kepada anak-anak kita?",
        "body": (
            "Warisan terbesar bukan harta, tapi nilai, teladan, dan cinta. "
            "Perjalanan ini tentang membangun keluarga yang kuat dan "
            "mewariskan sesuatu yang bertahan lebih lama dari diri kita."
        ),
    },
    {
        "slug": "urat-malu",
        "emoji": "😶",
        "title": "URAT MALU?",
        "desc": "Ketika sesuatu yang salah mulai dianggap biasa.",
        "body": (
            "Ada masa ketika hal yang keliru perlahan dianggap wajar, dan rasa "
            "malu menghilang. Perjalanan ini tentang menjaga hati nurani, "
            "berani berbeda, dan tidak ikut arus hanya karena semua orang "
            "melakukannya."
        ),
    },
    {
        "slug": "pengembangan-diri",
        "emoji": "🌱",
        "title": "PENGEMBANGAN DIRI",
        "desc": "Menjadi manusia yang lebih baik, sedikit demi sedikit.",
        "body": (
            "Perubahan besar lahir dari langkah-langkah kecil yang konsisten. "
            "Perjalanan ini tentang kebiasaan, disiplin, dan proses menjadi "
            "versi diri yang lebih baik setiap hari."
        ),
    },
]

# Arah pengembangan brand jangka panjang (10-20 tahun)
PILLARS = [
    {"emoji": "📺", "title": "Media", "desc": "Konten video dan tulisan yang menginspirasi."},
    {"emoji": "📚", "title": "Penerbitan Buku", "desc": "Karya yang bertahan lintas generasi."},
    {"emoji": "🤝", "title": "Komunitas", "desc": "Ruang tumbuh bersama orang-orang sevisi."},
    {"emoji": "🎓", "title": "Kelas Online", "desc": "Belajar terstruktur untuk berkembang."},
    {"emoji": "👕", "title": "Merchandise", "desc": "Pengingat nilai dalam keseharian."},
    {"emoji": "❤️", "title": "Social Impact", "desc": "Dampak nyata bagi sesama."},
]

NAV = [
    {"endpoint": "home", "label": "Beranda"},
    {"endpoint": "journeys", "label": "Perjalanan"},
    {"endpoint": "about", "label": "Tentang"},
    {"endpoint": "join", "label": "Bergabung"},
]
