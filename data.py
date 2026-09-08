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
    # Konten halaman berlangganan (newsletter)
    "newsletter": {
        "name": "Catatan Berdampak",
        "desc": (
            "Setiap pekan, aku berbagi tips produktivitas yang bisa langsung "
            "dipraktikkan, refleksi hidup, dan sorotan dari buku-buku favoritku, "
            "langsung ke inbox-mu. Gratis, dan akan selalu gratis."
        ),
        "readers": "12.000+",
        "reviews": "200+ ulasan",
        "disclaimer": (
            "Dengan mengirim formulir ini, kamu akan berlangganan newsletter "
            "gratisku, yang sesekali memuat info soal buku, aplikasi, dan kelasku. "
            "Kamu bisa berhenti berlangganan kapan saja tanpa masalah."
        ),
    },
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

# Kategori di dalam dropdown "Tutorial"
TUTORIAL_TOPICS = [
    {"emoji": "⚡", "title": "Produktivitas", "desc": "Kelola waktu dan energi dengan lebih baik.", "slug": "produktivitas"},
    {"emoji": "💰", "title": "Keuangan", "desc": "Bangun kebebasan finansial yang sehat.", "slug": "keuangan"},
    {"emoji": "🌱", "title": "Pengembangan Diri", "desc": "Tumbuh jadi versi terbaik dirimu.", "slug": "pengembangan-diri"},
    {"emoji": "🎥", "title": "Membuat Konten", "desc": "Berbagi ide lewat video dan tulisan.", "slug": "konten"},
]

# Daftar kelas untuk halaman "Kelas"
COURSES = [
    {"emoji": "⚡", "title": "Sistem Produktif 30 Hari", "desc": "Bangun kebiasaan produktif yang bertahan, langkah demi langkah.", "level": "Pemula", "duration": "4 minggu"},
    {"emoji": "💰", "title": "Dasar Kebebasan Finansial", "desc": "Kelola uang, menabung, dan berinvestasi dengan bijak.", "level": "Pemula", "duration": "6 minggu"},
    {"emoji": "🎥", "title": "Mulai Channel YouTube", "desc": "Dari ide pertama sampai video yang konsisten.", "level": "Menengah", "duration": "5 minggu"},
]

# Sumber daya gratis untuk halaman "Sumber Daya"
RESOURCES = [
    {"emoji": "📄", "title": "Template Perencana Harian", "desc": "Rencanakan harimu di sekitar hal yang benar-benar penting."},
    {"emoji": "📚", "title": "Daftar Buku Pilihan", "desc": "Rekomendasi buku tentang hidup, produktivitas, dan makna."},
    {"emoji": "🎧", "title": "Rekomendasi Podcast", "desc": "Teman belajar di perjalanan dan waktu senggang."},
    {"emoji": "🧭", "title": "Panduan Memulai", "desc": "Langkah awal membangun hidup yang lebih berdampak."},
]

# Nilai jual untuk halaman "Untuk Bisnis"
BUSINESS_OFFERS = [
    {"emoji": "🎤", "title": "Sesi & Workshop", "desc": "Sesi inspiratif soal produktivitas dan makna kerja untuk tim."},
    {"emoji": "🤝", "title": "Program Tim", "desc": "Pendampingan berkelanjutan untuk budaya kerja yang lebih sehat."},
    {"emoji": "📈", "title": "Konsultasi", "desc": "Bantu organisasi tumbuh dengan nilai yang berdampak."},
]

# Menu navigasi utama.
# type "link"     -> tautan biasa
# type "dropdown" -> punya submenu (items)
NAV = [
    {"type": "link", "endpoint": "courses", "label": "Kelas"},
    {"type": "link", "endpoint": "business", "label": "Untuk Bisnis"},
    {"type": "dropdown", "endpoint": "tutorials", "label": "Tutorial"},
    {"type": "link", "endpoint": "resources", "label": "Sumber Daya"},
    {"type": "link", "endpoint": "about", "label": "Tentang"},
]
