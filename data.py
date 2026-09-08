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

# Kategori di dalam dropdown "Tutorial".
# Tiap topik punya artikel lengkap (intro + beberapa bagian).
TUTORIAL_TOPICS = [
    {
        "emoji": "⚡",
        "title": "Produktivitas",
        "desc": "Kelola waktu dan energi dengan lebih baik.",
        "slug": "produktivitas",
        "read_time": "6 menit",
        "intro": (
            "Produktivitas sejati bukan soal melakukan lebih banyak hal, tapi "
            "melakukan hal yang tepat dengan tenang. Panduan ini merangkum prinsip "
            "dan langkah praktis untuk mengelola waktu serta energimu."
        ),
        "sections": [
            {"heading": "Mulai dari prioritas, bukan daftar tugas", "text": (
                "Sebelum menyusun to-do list, tanyakan: dari semua ini, mana yang "
                "paling penting hari ini? Satu atau dua tugas utama lebih berharga "
                "daripada sepuluh tugas kecil yang tidak menggerakkan apa-apa.")},
            {"heading": "Lindungi energi, bukan hanya waktu", "text": (
                "Waktu terbaik untuk kerja yang menuntut fokus adalah saat energimu "
                "paling tinggi. Kenali ritme harianmu dan tempatkan pekerjaan berat "
                "di jam tersebut.")},
            {"heading": "Kurangi gesekan untuk kebiasaan baik", "text": (
                "Semakin mudah sebuah kebiasaan dimulai, semakin besar peluang kamu "
                "menjalankannya. Siapkan lingkungan agar pilihan yang baik menjadi "
                "pilihan yang paling gampang.")},
        ],
    },
    {
        "emoji": "💰",
        "title": "Keuangan",
        "desc": "Bangun kebebasan finansial yang sehat.",
        "slug": "keuangan",
        "read_time": "7 menit",
        "intro": (
            "Mengatur keuangan tidak harus rumit. Dengan beberapa prinsip dasar, "
            "kamu bisa lebih tenang menghadapi masa depan tanpa melupakan bekal "
            "jangka panjang."
        ),
        "sections": [
            {"heading": "Kenali ke mana uangmu pergi", "text": (
                "Langkah pertama selalu kesadaran. Catat pemasukan dan pengeluaran "
                "selama sebulan. Angka yang jujur sering mengejutkan, dan dari situ "
                "perubahan dimulai.")},
            {"heading": "Bangun dana darurat lebih dulu", "text": (
                "Sebelum berinvestasi, siapkan dana darurat setara beberapa bulan "
                "pengeluaran. Ini bantalan yang membuatmu tidak panik saat keadaan "
                "tak terduga datang.")},
            {"heading": "Investasi terbaik melampaui dunia", "text": (
                "Selain menumbuhkan aset, sisihkan untuk memberi. Sebagian investasi "
                "terbaik justru tidak memberi return di dunia, tapi menjadi bekal "
                "yang jauh lebih berharga.")},
        ],
    },
    {
        "emoji": "🌱",
        "title": "Pengembangan Diri",
        "desc": "Tumbuh jadi versi terbaik dirimu.",
        "slug": "pengembangan-diri",
        "read_time": "5 menit",
        "intro": (
            "Pertumbuhan besar jarang terjadi dalam semalam. Ia lahir dari langkah "
            "kecil yang diulang dengan konsisten. Panduan ini soal cara tumbuh "
            "sedikit demi sedikit, tanpa membakar diri."
        ),
        "sections": [
            {"heading": "Fokus pada sistem, bukan hasil", "text": (
                "Hasil datang dan pergi, tapi sistem harian yang kamu jalankan "
                "menentukan arah jangka panjang. Perbaiki prosesnya, hasil akan "
                "menyusul.")},
            {"heading": "Rangkul ketidaknyamanan yang sehat", "text": (
                "Pertumbuhan terjadi di tepi zona nyaman. Cari tantangan kecil yang "
                "sedikit di atas kemampuanmu saat ini, lalu naik bertahap.")},
            {"heading": "Refleksi rutin", "text": (
                "Luangkan waktu tiap pekan untuk merenung: apa yang berjalan baik, "
                "apa yang perlu diubah. Refleksi mengubah pengalaman menjadi "
                "pelajaran.")},
        ],
    },
    {
        "emoji": "🎥",
        "title": "Membuat Konten",
        "desc": "Berbagi ide lewat video dan tulisan.",
        "slug": "konten",
        "read_time": "6 menit",
        "intro": (
            "Membuat konten adalah cara berbagi nilai sekaligus tumbuh bersama "
            "orang lain. Kamu tidak butuh peralatan mahal untuk memulai, cukup "
            "sesuatu yang ingin kamu sampaikan."
        ),
        "sections": [
            {"heading": "Mulai dengan satu ide jelas", "text": (
                "Konten terbaik lahir dari satu pesan yang ingin kamu sampaikan. "
                "Tentukan idenya dulu, baru pikirkan bentuknya, video, tulisan, "
                "atau audio.")},
            {"heading": "Selesai lebih baik daripada sempurna", "text": (
                "Karya pertamamu tidak akan sempurna, dan itu wajar. Yang penting "
                "kamu menyelesaikan dan mempublikasikannya, lalu belajar dari "
                "sana.")},
            {"heading": "Konsistensi mengalahkan intensitas", "text": (
                "Membuat satu konten sederhana secara rutin jauh lebih berdampak "
                "daripada satu karya besar yang jarang. Bangun ritme yang "
                "sanggup kamu jaga.")},
        ],
    },
]

# Daftar kelas untuk halaman "Kelas"
COURSES = [
    {
        "slug": "sistem-produktif-30-hari",
        "emoji": "⚡",
        "title": "Sistem Produktif 30 Hari",
        "desc": "Bangun kebiasaan produktif yang bertahan, langkah demi langkah.",
        "level": "Pemula",
        "duration": "4 minggu",
        "lessons": 24,
        "price": "Rp 349.000",
        "intro": (
            "Kebanyakan sistem produktivitas gagal karena terlalu rumit dan "
            "mengandalkan motivasi. Kelas ini mengajarkan pendekatan yang berbeda: "
            "membangun sistem sederhana yang berjalan otomatis, bahkan di hari-hari "
            "ketika semangatmu sedang turun. Dalam 30 hari, kamu akan memasang "
            "fondasi kebiasaan yang bertahan jauh setelah kelas selesai."
        ),
        "outcomes": [
            "Merancang rutinitas harian di sekitar hal yang benar-benar penting",
            "Menguasai teknik fokus mendalam tanpa kelelahan",
            "Membangun sistem pencatatan tugas yang tidak berantakan",
            "Menjaga konsistensi lewat kebiasaan mikro yang mudah dijalankan",
        ],
        "curriculum": [
            {"week": "Minggu 1", "title": "Fondasi", "topics": ["Menemukan prioritas sejati", "Audit waktu dan energi", "Menyiapkan lingkungan kerja"]},
            {"week": "Minggu 2", "title": "Fokus", "topics": ["Deep work untuk pemula", "Mengelola distraksi digital", "Teknik time-blocking"]},
            {"week": "Minggu 3", "title": "Sistem", "topics": ["Menata daftar tugas", "Review mingguan", "Otomatisasi hal kecil"]},
            {"week": "Minggu 4", "title": "Konsistensi", "topics": ["Kebiasaan mikro", "Bangkit setelah gagal", "Rencana 90 hari ke depan"]},
        ],
    },
    {
        "slug": "dasar-kebebasan-finansial",
        "emoji": "💰",
        "title": "Dasar Kebebasan Finansial",
        "desc": "Kelola uang, menabung, dan berinvestasi dengan bijak.",
        "level": "Pemula",
        "duration": "6 minggu",
        "lessons": 30,
        "price": "Rp 499.000",
        "intro": (
            "Kebebasan finansial bukan soal menjadi kaya raya, tapi soal memiliki "
            "kendali atas uangmu sehingga bisa hidup lebih tenang dan memberi lebih "
            "banyak. Kelas ini membongkar dasar-dasar keuangan pribadi dengan bahasa "
            "sederhana, dari mengatur arus kas sampai memulai investasi pertama, "
            "tanpa melupakan nilai dan bekal jangka panjang."
        ),
        "outcomes": [
            "Menyusun anggaran yang realistis dan mudah dijaga",
            "Membangun dana darurat yang menenangkan",
            "Memahami dasar investasi dan risikonya",
            "Menyeimbangkan tujuan dunia dan bekal akhirat",
        ],
        "curriculum": [
            {"week": "Minggu 1-2", "title": "Fondasi Keuangan", "topics": ["Mindset uang yang sehat", "Mencatat dan mengatur arus kas", "Membedakan kebutuhan dan keinginan"]},
            {"week": "Minggu 3-4", "title": "Menabung & Melindungi", "topics": ["Dana darurat", "Mengelola utang dengan bijak", "Proteksi dasar"]},
            {"week": "Minggu 5-6", "title": "Menumbuhkan", "topics": ["Dasar investasi", "Instrumen untuk pemula", "Rencana keuangan jangka panjang"]},
        ],
    },
    {
        "slug": "mulai-channel-youtube",
        "emoji": "🎥",
        "title": "Mulai Channel YouTube",
        "desc": "Dari ide pertama sampai video yang konsisten.",
        "level": "Menengah",
        "duration": "5 minggu",
        "lessons": 27,
        "price": "Rp 449.000",
        "intro": (
            "Berbagi ide lewat video adalah salah satu cara paling berdampak untuk "
            "menjangkau orang. Kelas ini menemanimu dari nol: menemukan sudut pandang "
            "yang khas, membuat video pertama tanpa peralatan mahal, sampai menjaga "
            "ritme unggah yang berkelanjutan tanpa kehabisan ide."
        ),
        "outcomes": [
            "Menemukan niche dan sudut pandang yang otentik",
            "Membuat video dengan alat sederhana yang sudah kamu punya",
            "Menyusun naskah dan struktur cerita yang menarik",
            "Menjaga konsistensi unggah tanpa kelelahan kreatif",
        ],
        "curriculum": [
            {"week": "Minggu 1", "title": "Arah", "topics": ["Menemukan niche", "Riset audiens", "Menyusun ide konten"]},
            {"week": "Minggu 2", "title": "Produksi", "topics": ["Peralatan minimal", "Dasar pengambilan gambar", "Menulis naskah"]},
            {"week": "Minggu 3", "title": "Editing", "topics": ["Alur cerita", "Editing dasar", "Thumbnail dan judul"]},
            {"week": "Minggu 4-5", "title": "Bertumbuh", "topics": ["Konsistensi unggah", "Membaca analitik", "Membangun komunitas"]},
        ],
    },
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
