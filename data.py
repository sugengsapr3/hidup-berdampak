"""
Konten statis untuk website brand "HIDUP. BERDAMPAK".
Ecosystem edukasi, pengembangan diri, kepemimpinan, dan dampak.

Semua konten ditarik dari file ini agar mudah dikembangkan menjadi CMS.
"""

SITE = {
    "name": "HIDUP BERDAMPAK",
    "brand": "HIDUP. BERDAMPAK",
    "tagline": "Live with Purpose. Create Impact.",
    "owner": "Abi Albarra",
    # Hero utama beranda
    "hero_title_1": "Hidup bukan hanya tentang apa yang kita capai.",
    "hero_title_2": "Tetapi tentang apa yang tertinggal karena kita pernah ada.",
    "hero_sub": (
        "Belajar, bertumbuh, membangun kehidupan yang bermakna, dan memberi "
        "manfaat yang terus hidup melampaui diri kita."
    ),
    # Baris makna singkat di hero (menjelaskan arti brand)
    "hero_meaning": "Sebuah ruang belajar, bertumbuh, dan menciptakan dampak yang bertahan.",
    "email": "hidup.berdampak.media@gmail.com",
    "youtube_url": "#",
    # Newsletter (dipakai di beranda & footer)
    "newsletter": {
        "headline": "Satu Refleksi. Satu Pelajaran. Satu Dampak.",
        "desc": "Dapatkan tulisan, video, dan ide pilihan dari HIDUP BERDAMPAK.",
        "note": "No spam. Hanya sesuatu yang layak dibaca.",
    },
    "socials": [
        {"label": "YouTube", "url": "#"},
        {"label": "Instagram", "url": "#"},
        {"label": "LinkedIn", "url": "#"},
        {"label": "TikTok", "url": "#"},
    ],
}

# =====================================================================
# BELAJAR — enam jalur utama ("Temukan Jalanmu")
# =====================================================================
LEARN_TOPICS = [
    {
        "slug": "manusia-dan-lobang",
        "emoji": "🕳️",
        "title": "Manusia & Lobang",
        "desc": "Refleksi tentang jatuh, bangkit, pilihan hidup, dan makna perjalanan manusia.",
        "intro": (
            "Setiap manusia pernah jatuh ke dalam lobangnya masing-masing. Yang "
            "membedakan bukan seberapa dalam kita jatuh, tapi seberapa kita mau "
            "belajar untuk bangkit dan memahami kenapa kita ada di sana."
        ),
        "sections": [
            {"heading": "Jatuh adalah bagian dari perjalanan", "text": (
                "Tidak ada kehidupan yang lurus tanpa lubang. Menerima bahwa jatuh "
                "adalah bagian dari proses membuat kita lebih lapang menghadapinya.")},
            {"heading": "Pilihan untuk tidak tinggal di sana", "text": (
                "Sebagian jatuh karena keadaan, sebagian karena pilihan. Tapi tidak "
                "semua orang memilih untuk tetap tinggal di dalam lobang.")},
            {"heading": "Makna di balik luka", "text": (
                "Luka yang dimaknai menjadi pelajaran. Perjalanan ini tentang "
                "menerima, memaknai kegagalan, dan tumbuh darinya.")},
        ],
    },
    {
        "slug": "financial-freedom",
        "emoji": "💰",
        "title": "Financial Freedom",
        "desc": "Bangun kebebasan finansial tanpa kehilangan arah dan tujuan hidup.",
        "intro": (
            "Kebebasan finansial bukan tujuan akhir, tapi alat untuk hidup lebih "
            "bermakna dan memberi lebih banyak, tanpa membuat kita lupa pada arah "
            "dan tujuan hidup."
        ),
        "sections": [
            {"heading": "Uang sebagai alat, bukan tujuan", "text": (
                "Ketika uang menjadi tujuan, ia tidak pernah cukup. Ketika ia menjadi "
                "alat, ia membantu kita hidup dan memberi lebih leluasa.")},
            {"heading": "Kelola dengan sadar", "text": (
                "Sadari ke mana uang pergi, bangun dana darurat, dan tumbuhkan aset "
                "secara bertahap dengan pemahaman, bukan ikut-ikutan.")},
            {"heading": "Jangan lupa bekal jangka panjang", "text": (
                "Sebagian rezeki terbaik justru yang kita berikan. Kebebasan sejati "
                "adalah ketika kita mampu memberi tanpa merasa kekurangan.")},
        ],
    },
    {
        "slug": "pengembangan-diri",
        "emoji": "🌱",
        "title": "Pengembangan Diri",
        "desc": "Menjadi pribadi yang lebih kuat, sadar, disiplin, dan bertumbuh.",
        "intro": (
            "Perubahan besar lahir dari langkah-langkah kecil yang konsisten. "
            "Pengembangan diri adalah proses menjadi pribadi yang lebih kuat, "
            "sadar, dan disiplin, sedikit demi sedikit."
        ),
        "sections": [
            {"heading": "Fokus pada sistem, bukan hasil", "text": (
                "Hasil datang dan pergi, tapi sistem harian yang kita jalankan "
                "menentukan arah jangka panjang. Perbaiki prosesnya.")},
            {"heading": "Disiplin melampaui motivasi", "text": (
                "Motivasi naik-turun. Disiplin yang dibangun lewat kebiasaan kecil "
                "membuat kita tetap bergerak bahkan di hari yang berat.")},
            {"heading": "Kesadaran diri", "text": (
                "Bertumbuh dimulai dari mengenali diri sendiri: kekuatan, "
                "kelemahan, dan pola yang perlu diperbaiki.")},
        ],
    },
    {
        "slug": "islam-bekal-akhirat",
        "emoji": "🕌",
        "title": "Islam & Bekal Akhirat",
        "desc": "Karena investasi terbaik bukan hanya untuk kehidupan hari ini.",
        "intro": (
            "Ada investasi yang hasilnya tidak kita nikmati di dunia, tapi menjadi "
            "bekal yang paling berharga kelak. Karena investasi terbaik bukan hanya "
            "untuk kehidupan hari ini."
        ),
        "sections": [
            {"heading": "Amal yang mengalir", "text": (
                "Sebagian amal terus mengalir pahalanya meski kita telah tiada. "
                "Itulah salah satu warisan paling berharga.")},
            {"heading": "Ilmu yang bermanfaat", "text": (
                "Ilmu yang diajarkan dan diamalkan orang lain menjadi bekal yang "
                "tidak terputus. Berbagi ilmu adalah bentuk dampak yang abadi.")},
            {"heading": "Niat yang lurus", "text": (
                "Nilai sebuah amal bergantung pada niatnya. Meluruskan niat membuat "
                "hal biasa menjadi bernilai di sisi-Nya.")},
        ],
    },
    {
        "slug": "keluarga-legacy",
        "emoji": "👨‍👩‍👧‍👦",
        "title": "Keluarga & Legacy",
        "desc": "Tentang keluarga, pendidikan, nilai, dan apa yang kita wariskan.",
        "intro": (
            "Warisan terbesar bukan harta, tapi nilai, teladan, dan cinta. "
            "Perjalanan ini tentang keluarga, pendidikan, dan apa yang kita "
            "wariskan kepada anak-anak kita."
        ),
        "sections": [
            {"heading": "Nilai lebih tahan lama dari harta", "text": (
                "Harta bisa habis, tapi nilai yang tertanam akan diteruskan lintas "
                "generasi. Wariskan prinsip, bukan sekadar materi.")},
            {"heading": "Pendidikan dimulai dari rumah", "text": (
                "Teladan orang tua adalah kurikulum pertama anak. Apa yang kita "
                "lakukan lebih berbicara daripada apa yang kita katakan.")},
            {"heading": "Membangun legacy", "text": (
                "Legacy adalah apa yang tetap hidup setelah kita pergi. Bangun "
                "keluarga yang menjadi sumber kebaikan yang terus mengalir.")},
        ],
    },
    {
        "slug": "urat-malu",
        "emoji": "😶",
        "title": "URAT MALU?",
        "desc": "Melihat fenomena sosial dengan refleksi, satire, dan pelajaran moral.",
        "intro": (
            "Ada masa ketika hal yang keliru perlahan dianggap wajar, dan rasa malu "
            "menghilang. Kolom ini melihat fenomena sosial dengan refleksi, satire, "
            "dan pelajaran moral."
        ),
        "sections": [
            {"heading": "Ketika yang salah dianggap biasa", "text": (
                "Normalisasi hal keliru terjadi perlahan, hampir tak terasa. "
                "Menyadarinya adalah langkah pertama untuk tidak ikut hanyut.")},
            {"heading": "Menjaga hati nurani", "text": (
                "Rasa malu yang sehat adalah penjaga. Ia mengingatkan kita pada "
                "batas antara yang pantas dan tidak.")},
            {"heading": "Berani berbeda", "text": (
                "Tidak semua yang populer itu benar. Keberanian untuk berbeda "
                "menjaga integritas di tengah arus.")},
        ],
    },
]

# =====================================================================
# BUKU
# =====================================================================
BOOKS = [
    {
        "slug": "manusia-dan-lobang",
        "title": "Manusia dan Lobang",
        "status": "available",
        "tagline": "Setiap manusia pernah jatuh ke dalam \u201clobang\u201d.",
        "blurb": (
            "Sebagian jatuh karena keadaan. Sebagian karena pilihan. Tetapi tidak "
            "semua orang memilih untuk tetap tinggal di sana."
        ),
        "desc": (
            "Sebuah buku refleksi tentang jatuh, bangkit, dan menemukan makna di "
            "balik perjalanan hidup manusia. Ditulis untuk menemani siapa pun yang "
            "sedang berada di titik terendah, dan ingin menemukan jalan keluar."
        ),
        "excerpt": (
            "Kita semua punya lobang. Ada yang menganga di siang hari, ada yang "
            "hanya terlihat saat malam sunyi. Pertanyaannya bukan bagaimana caranya "
            "tidak pernah jatuh, tapi bagaimana kita memilih untuk tidak tinggal di "
            "dasar terlalu lama."
        ),
    },
    {
        "slug": "coming-soon",
        "title": "Buku Berikutnya",
        "status": "coming_soon",
        "tagline": "Sedang dalam proses penulisan.",
        "blurb": "Karya berikutnya sedang disiapkan. Nantikan kabarnya.",
        "desc": "",
        "excerpt": "",
    },
]

# =====================================================================
# UNTUK BISNIS
# =====================================================================
BUSINESS_HERO = {
    "title_1": "Bangun Tim yang Produktif,",
    "title_2": "Bertumbuh, dan Berdampak.",
    "sub": (
        "Program workshop, leadership, dan pengembangan budaya kerja untuk "
        "membantu organisasi bertumbuh tanpa kehilangan makna."
    ),
}

BUSINESS_SERVICES = [
    {
        "slug": "corporate-workshop",
        "emoji": "🎤",
        "title": "Corporate Workshop",
        "desc": (
            "Sesi inspiratif dan praktis untuk meningkatkan produktivitas, "
            "leadership, komunikasi, ownership, dan makna kerja."
        ),
    },
    {
        "slug": "team-development",
        "emoji": "🤝",
        "title": "Team Development Program",
        "desc": (
            "Program pendampingan berkelanjutan untuk membangun tim yang lebih "
            "sehat, kuat, dan kolaboratif."
        ),
    },
    {
        "slug": "leadership-advisory",
        "emoji": "🧭",
        "title": "Leadership & Culture Advisory",
        "desc": (
            "Pendampingan bagi organisasi dan leaders dalam membangun budaya kerja "
            "yang sehat, produktif, dan berdampak."
        ),
    },
]

BUSINESS_CAPABILITIES = [
    "Leadership Development",
    "Productivity",
    "Communication",
    "Ownership",
    "Culture",
    "Employee Engagement",
    "Personal Effectiveness",
    "Team Collaboration",
]

# =====================================================================
# TENTANG — filosofi
# =====================================================================
PHILOSOPHY = [
    {"step": "Learn", "title": "Belajar", "desc": "Belajar dari ilmu, pengalaman, sejarah, dan kehidupan."},
    {"step": "Grow", "title": "Bertumbuh", "desc": "Mengubah pengetahuan menjadi pertumbuhan pribadi."},
    {"step": "Impact", "title": "Berdampak", "desc": "Mengubah pertumbuhan menjadi manfaat untuk orang lain."},
]

# =====================================================================
# SUMBER DAYA
# =====================================================================
RESOURCES = [
    {"emoji": "📝", "title": "Artikel", "desc": "Tulisan reflektif dan praktis untuk menemani perjalananmu."},
    {"emoji": "🎬", "title": "Video", "desc": "Konten video dari kanal HIDUP BERDAMPAK."},
    {"emoji": "🛠️", "title": "Tools", "desc": "Alat sederhana untuk membantu keseharianmu."},
    {"emoji": "📄", "title": "Worksheet", "desc": "Lembar kerja untuk merefleksikan dan menata langkah."},
    {"emoji": "⬇️", "title": "Download Gratis", "desc": "Sumber daya pilihan yang bisa kamu unduh cuma-cuma."},
    {"emoji": "✉️", "title": "Newsletter", "desc": "Satu refleksi pilihan langsung ke inbox-mu."},
]

# =====================================================================
# PILIHAN MINGGU INI (featured content editorial)
# =====================================================================
FEATURED = [
    {"kind": "Artikel", "emoji": "📝", "title": "Ketika Yang Salah Dianggap Biasa", "desc": "Refleksi soal normalisasi hal keliru di sekitar kita.", "endpoint": "learn_detail", "slug": "urat-malu"},
    {"kind": "Video", "emoji": "🎬", "title": "Keluar dari Lobang", "desc": "Percakapan tentang bangkit dari titik terendah.", "endpoint": "learn_detail", "slug": "manusia-dan-lobang"},
    {"kind": "Buku", "emoji": "📖", "title": "Manusia dan Lobang", "desc": "Buku refleksi tentang jatuh, bangkit, dan makna.", "endpoint": "book_detail", "slug": "manusia-dan-lobang"},
    {"kind": "Sumber Daya", "emoji": "📄", "title": "Worksheet Refleksi Pekanan", "desc": "Lembar kerja untuk menata langkah tiap pekan.", "endpoint": "resources", "slug": None},
]

# =====================================================================
# LOGIN — penyedia social login (UI; OAuth diaktifkan nanti)
# "key" dipakai untuk styling ikon di CSS/SVG.
# =====================================================================
AUTH_PROVIDERS = [
    {"key": "google", "label": "Google"},
    {"key": "facebook", "label": "Facebook"},
    {"key": "tiktok", "label": "TikTok"},
    {"key": "apple", "label": "Apple"},
]

# =====================================================================
# GENERASI BERDAMPAK (bagian dari Keluarga & Legacy)
# Portofolio perjalanan anak: journey, projects, leadership, achievements,
# learning, reflections, impact. Semua modular & mudah ditambah.
#
# CARA EDIT:
# - Tambah anak baru  : tambahkan satu dict ke list CHILDREN.
# - Tambah project     : tambahkan dict ke "projects" milik anak.
# - Tambah achievement : tambahkan dict ke "achievements".
# - Tambah reflection  : tambahkan dict ke "reflections".
# Field yang belum ada faktanya: biarkan list-nya kosong ([]) -> tampil
# empty-state yang rapi. JANGAN mengisi data fiktif.
#
# PRIVASI: jangan menaruh tanggal lahir lengkap, alamat, no. HP, no. induk
# siswa, atau data pribadi sensitif anak di sini.
# =====================================================================
CHILDREN = [
    {
        "slug": "dzaky",
        "owner_email": "dzaky.albarra101@gmail.com",
        "name": "Dzaky Albarra",
        "status": "active",  # "active" | "coming_soon"
        "focus": "Business, Communication & Global Perspective",
        "short": (
            "Mengeksplorasi komunikasi, bisnis, bahasa, kepemimpinan, dan "
            "perspektif global melalui berbagai pengalaman dan project."
        ),
        "intro": (
            "A collection of experiences, projects, leadership moments and "
            "reflections that shape his journey of learning and contribution."
        ),
        "journey": (
            "Dzaky tertarik pada dunia komunikasi, bisnis, dan bahasa. Saat ini "
            "ia sedang mengembangkan kemampuan bahasa Inggris dan Mandarin, serta "
            "belajar dari pengalaman berorganisasi di sekolah. Arah perkembangannya "
            "adalah memperkuat kemampuan berkomunikasi dan memahami perspektif global."
        ),
        "projects": [
            {
                "title": "Arabic & English Dictionary Project",
                "challenge": (
                    "Banyak teman kesulitan menghubungkan kosakata Arab dan Inggris "
                    "dalam satu rujukan yang sederhana dan mudah dipakai."
                ),
                "idea": (
                    "Menyusun kamus dwibahasa Arab-Inggris yang ringkas untuk "
                    "membantu proses belajar sehari-hari."
                ),
                "process": (
                    "Mengumpulkan kosakata, menyusunnya secara rapi, dan merapikan "
                    "formatnya agar mudah dibaca."
                ),
                "role": "Penggagas dan penyusun.",
                "learned": (
                    "Belajar menyusun informasi secara terstruktur dan pentingnya "
                    "ketekunan dalam menyelesaikan sebuah karya."
                ),
                "impact": "Impact details will be added later.",
            },
        ],
        "leadership": [
            {
                "title": "Komunikasi Organisasi Sekolah",
                "role": "Bagian komunikasi",
                "organization": "Organisasi sekolah",
                "year": "",
                "description": (
                    "Terlibat dalam area komunikasi kegiatan organisasi di sekolah."
                ),
                "responsibility": "Membantu menyampaikan informasi kegiatan.",
                "learning": "Belajar menyampaikan pesan dengan jelas kepada banyak orang.",
            },
        ],
        "achievements": [],
        "learning": [
            {"area": "English", "note": "Sedang dikembangkan secara aktif."},
            {"area": "Mandarin", "note": "Sedang dipelajari."},
            {"area": "Communication", "note": "Diasah lewat pengalaman berorganisasi."},
        ],
        "reflections": [],
        "impact": [],
    },
    {
        "slug": "hadziq",
        "owner_email": "hdizhwar@gmail.com",
        "name": "Hadziq Dizhwar",
        "status": "active",
        "focus": "Science, Health & Leadership",
        "short": (
            "Membangun rasa ingin tahu terhadap sains dan kesehatan sambil "
            "mengembangkan leadership, communication, dan kontribusi sosial."
        ),
        "intro": (
            "A journey of curiosity in science and health, alongside growing "
            "leadership, communication, and contribution."
        ),
        "journey": (
            "Hadziq memiliki ketertarikan pada bidang sains dan kesehatan. Ia "
            "pernah mendapat tanggung jawab (PIC) dalam kegiatan sekolah dan "
            "memiliki pengalaman public speaking. Saat ini ia sedang mengembangkan "
            "kemampuan bahasa Inggris."
        ),
        "projects": [],
        "leadership": [
            {
                "title": "PIC Kegiatan Sekolah",
                "role": "Penanggung jawab kegiatan",
                "organization": "Kegiatan sekolah",
                "year": "",
                "description": "Mendapatkan tanggung jawab sebagai PIC dalam kegiatan sekolah.",
                "responsibility": "Mengoordinasikan bagian dari kegiatan.",
                "learning": "Belajar tanggung jawab dan mengelola tugas.",
            },
        ],
        "achievements": [],
        "learning": [
            {"area": "English", "note": "Sedang dikembangkan."},
            {"area": "Public Speaking", "note": "Diasah lewat kegiatan/event."},
        ],
        "reflections": [],
        "impact": [],
    },
    {
        "slug": "fiori",
        "owner_email": "fiorighanialbina@gmail.com",
        "name": "Fiori Ghania Albina",
        "status": "coming_soon",
        "focus": "Curiosity, Science & Creativity",
        "short": (
            "Belajar memahami dunia melalui rasa ingin tahu, project sederhana, "
            "membaca, bereksperimen, dan berbagi pengetahuan."
        ),
        "intro": "",
        "journey": "",
        "projects": [],
        "leadership": [],
        "achievements": [],
        "learning": [],
        "reflections": [],
        "impact": [],
    },
    {
        "slug": "hazel",
        "owner_email": "hazel.dinara@gmail.com",
        "name": "Hazel Aghnia Dinara",
        "status": "coming_soon",
        "focus": "Learning, Exploration & Creativity",
        "short": (
            "Membangun fondasi belajar melalui eksplorasi, kreativitas, kebiasaan "
            "baik, dan pengalaman sehari-hari."
        ),
        "intro": "",
        "journey": "",
        "projects": [],
        "leadership": [],
        "achievements": [],
        "learning": [],
        "reflections": [],
        "impact": [],
    },
]


# =====================================================================
# PROPERTI / RUMAH DIJUAL (data awal; selanjutnya dikelola lewat /admin)
# Di-seed ke tabel 'properties' saat /admin/init bila tabel masih kosong.
# =====================================================================
PROPERTIES = [
    {
        "slug": "asana-residence-cikeas-bhimala",
        "title": "Rumah 2 Lantai Siap Huni – Asana Residence Cikeas (Type Bhimala)",
        "price": 1345000000,
        "address": "Asana Residence Blok E26, Cikeas, Kabupaten Bogor",
        "maps_url": "https://maps.app.goo.gl/Q4vmQmnFhWikHaLS6",
        "status": "available",
        "photos": [
            "https://i.postimg.cc/T1vV8P4G/Gambar-Rumah-1.jpg",
            "https://i.postimg.cc/90Hd3fn2/Gambar-Rumah-2.jpg",
            "https://i.postimg.cc/2yNQp5KR/Gambar-Rumah-3.jpg",
            "https://i.postimg.cc/3NQXMwcM/Gambar-Rumah-4.jpg",
            "https://i.postimg.cc/1tqGYFJy/Gambar-Rumah-5.jpg",
            "https://i.postimg.cc/3RvXbGnY/Gambar-Rumah-6.jpg",
            "https://i.postimg.cc/hjdL3mpB/Gambar-Rumah-7.jpg",
            "https://i.postimg.cc/9M7dN9J2/Gambar-Rumah-8.jpg",
            "https://i.postimg.cc/PxwWFD2G/Gambar-Rumah-9.jpg",
            "https://i.postimg.cc/FRLynSGw/Gambar-Rumah-10.jpg",
            "https://i.postimg.cc/LX1t0PvW/Gambar-Rumah-11.jpg",
            "https://i.postimg.cc/vBVrSnXj/Gambar-Rumah-12.jpg",
        ],  # foto pertama = sampul; tambah/ubah lewat /admin kapan saja
        "description": (
            "🔥 HOT DEAL – DIJUAL CEPAT 🔥\n"
            "🏡 RUMAH 2 LANTAI SIAP HUNI\n"
            "ASANA RESIDENCE CIKEAS – TYPE BHIMALA\n\n"
            "⭐ SHM • Siap Huni • Cash/KPR • Bebas Banjir • Hadap Utara ⭐\n\n"
            "📢 DIJUAL KARENA PINDAH DOMISILI\n"
            "Kesempatan memiliki rumah di salah satu kawasan hunian favorit di Cikeas. "
            "Rumah dirawat dengan baik, siap ditempati, dan tidak memerlukan renovasi besar. "
            "Cocok untuk keluarga yang menginginkan lingkungan nyaman, aman, dengan akses "
            "mudah ke berbagai fasilitas.\n\n"
            "✨ KEUNGGULAN\n"
            "✅ Siap huni, tinggal bawa koper\n"
            "✅ Sertifikat Hak Milik (SHM)\n"
            "✅ Bisa dibeli Cash maupun KPR\n"
            "✅ Legalitas lengkap, siap dibantu hingga proses akad\n"
            "✅ Bebas banjir\n"
            "✅ Hadap Utara — lebih sejuk, tidak terkena matahari sore langsung\n"
            "✅ Kanopi untuk 2 mobil\n"
            "✅ Toren air sudah terpasang\n"
            "✅ Row jalan ±7–8 meter, dua mobil dapat berpapasan dengan nyaman\n"
            "✅ Dekat Clubhouse, Swimming Pool, Gym, Playground, dan Taman\n\n"
            "📐 SPESIFIKASI\n"
            "🏡 Luas Tanah: 84 m²\n"
            "🏡 Luas Bangunan: 69 m²\n"
            "🛏️ 3 Kamar Tidur\n"
            "🚿 2 Kamar Mandi\n"
            "⚡ Listrik 2.200 Watt\n"
            "💧 Air Jet Pump\n"
            "📄 Sertifikat Hak Milik (SHM)\n\n"
            "🏘️ FASILITAS PREMIUM\n"
            "✔️ One Gate System\n"
            "✔️ Security 24 Jam\n"
            "✔️ Swimming Pool\n"
            "✔️ Gym Center\n"
            "✔️ Clubhouse\n"
            "✔️ Playground\n"
            "✔️ Taman Hijau\n"
            "✔️ Lingkungan bersih, aman, dan nyaman\n\n"
            "📍 LOKASI STRATEGIS\n"
            "🚉 ±15 menit ke Stasiun LRT Cibubur\n"
            "🛣️ ±10 menit ke Tol JORR Cimanggis–Cibitung\n"
            "🛣️ ±15 menit ke Tol Cibubur\n"
            "🛣️ ±10 menit ke Tol Cimanggis\n"
            "🚗 Dekat Jalan Raya Transyogi\n"
            "🏫 Dekat sekolah\n"
            "🏥 Dekat rumah sakit\n"
            "🛍️ Dekat pusat perbelanjaan\n"
            "🕌 Dekat tempat ibadah\n"
            "☕ Dekat pusat kuliner\n\n"
            "💰 HARGA SPESIAL\n"
            "Rp1.345.000.000 (nego untuk pembeli serius)\n\n"
            "💎 VALUE YANG ANDA DAPATKAN\n"
            "Rumah siap huni • SHM • Bebas banjir • Hadap utara • Kanopi 2 mobil • "
            "Toren air terpasang • Dekat clubhouse • Fasilitas premium • Lokasi strategis.\n"
            "Dibandingkan rumah sejenis di kawasan Asana Residence, harga ini sangat "
            "kompetitif untuk kondisi rumah yang sudah siap ditempati.\n\n"
            "🤝 PEMBELIAN MUDAH & AMAN\n"
            "✅ Bisa Cash\n"
            "✅ Bisa KPR (sesuai persetujuan bank)\n"
            "✅ Legalitas lengkap\n"
            "✅ Siap dibantu hingga proses akad\n"
            "✅ PBB tertib\n"
            "✅ Tidak dalam sengketa\n"
            "✅ Serah terima setelah transaksi selesai\n\n"
            "❤️ COCOK UNTUK\n"
            "👨‍👩‍👧‍👦 Keluarga muda\n"
            "🏡 Rumah pertama\n"
            "💼 Investasi jangka panjang\n"
            "💰 Disewakan kembali\n\n"
            "📞 JADWALKAN SURVEI SEKARANG\n"
            "Dijual karena pemilik pindah domisili — siap menjadi milik pemilik baru "
            "tanpa perlu renovasi besar.\n"
            "Hubungi untuk: informasi lengkap, video house tour, jadwal survei, dan "
            "simulasi KPR.\n\n"
            "Rumah yang nyaman bukan hanya soal bangunannya, tetapi juga lingkungan dan "
            "kualitas hidup yang ditawarkan. Datang, lihat langsung, dan rasakan sendiri "
            "kenyamanannya. Siapa cepat, dia dapat!"
        ),
    },
]


# =====================================================================
# MATERI KELAS (modul yang tampil setelah user punya akses)
# Di-keyed berdasarkan slug kelas. Tiap modul: judul, video (YouTube embed
# opsional), dan catatan/isi teks. Ganti "video" dengan ID video YouTube kamu.
# =====================================================================
COURSE_MATERIALS = {
    "dasar-hidup-berdampak": [
        {
            "title": "Modul 1 — Menemukan Tujuan Hidup",
            "video": "",  # contoh isi nanti: "dQw4w9WgXcQ" (ID video YouTube)
            "notes": (
                "Kita mulai dari pertanyaan paling mendasar: untuk apa kita hidup? "
                "Modul ini membantumu menemukan alasan yang lebih besar dari sekadar "
                "rutinitas harian."
            ),
        },
        {
            "title": "Modul 2 — Membangun Kebiasaan yang Berdampak",
            "video": "",
            "notes": (
                "Perubahan besar lahir dari kebiasaan kecil yang konsisten. Pelajari "
                "cara merancang kebiasaan yang bertahan dan selaras dengan tujuanmu."
            ),
        },
        {
            "title": "Modul 3 — Meninggalkan Jejak yang Berarti",
            "video": "",
            "notes": (
                "Bagaimana memastikan hidup kita memberi manfaat yang terus mengalir, "
                "bahkan setelah kita tiada."
            ),
        },
    ],
    "financial-freedom-berkah": [
        {
            "title": "Modul 1 — Mindset Uang yang Sehat",
            "video": "",
            "notes": "Meluruskan cara pandang terhadap uang: alat, bukan tujuan.",
        },
        {
            "title": "Modul 2 — Mengatur Arus Kas & Menabung",
            "video": "",
            "notes": "Langkah praktis mencatat, mengatur, dan menyisihkan penghasilan.",
        },
        {
            "title": "Modul 3 — Investasi & Bekal Akhirat",
            "video": "",
            "notes": "Menumbuhkan aset dunia sambil menyiapkan bekal yang abadi.",
        },
    ],
    "keluarga-legacy": [
        {
            "title": "Modul 1 — Fondasi Keluarga yang Kuat",
            "video": "",
            "notes": "Nilai dan komunikasi sebagai pondasi keluarga.",
        },
        {
            "title": "Modul 2 — Mendidik dengan Teladan",
            "video": "",
            "notes": "Anak belajar dari apa yang kita lakukan, bukan yang kita katakan.",
        },
        {
            "title": "Modul 3 — Mewariskan Legacy",
            "video": "",
            "notes": "Membangun warisan nilai yang bertahan lintas generasi.",
        },
    ],
}


# =====================================================================
# NAVIGASI
# type "link"     -> tautan biasa
# type "dropdown" -> punya submenu (items: label + endpoint + optional slug)
# =====================================================================
NAV = [
    {"type": "link", "endpoint": "home", "label": "Home"},
    {"type": "dropdown", "endpoint": "learn", "label": "Belajar", "menu": "learn"},
    {"type": "link", "endpoint": "courses", "label": "Kelas"},
    {"type": "dropdown", "endpoint": "business", "label": "Untuk Bisnis", "menu": "business"},
    {"type": "link", "endpoint": "books", "label": "Buku"},
    {"type": "link", "endpoint": "properties", "label": "Rumah"},
    {"type": "dropdown", "endpoint": "resources", "label": "Sumber Daya", "menu": "resources"},
    {"type": "link", "endpoint": "about", "label": "Tentang"},
]

# Item submenu untuk tiap dropdown (dibangun sebagian dari list di atas)
NAV_BUSINESS_ITEMS = [
    {"label": "Corporate Workshop", "endpoint": "business"},
    {"label": "Team Development Program", "endpoint": "business"},
    {"label": "Leadership & Culture Advisory", "endpoint": "business"},
    {"label": "Custom Corporate Program", "endpoint": "business"},
]

NAV_RESOURCES_ITEMS = [
    {"label": "Artikel", "endpoint": "resources"},
    {"label": "Video", "endpoint": "resources"},
    {"label": "Tools", "endpoint": "resources"},
    {"label": "Worksheet", "endpoint": "resources"},
    {"label": "Download Gratis", "endpoint": "resources"},
    {"label": "Newsletter", "endpoint": "join"},
]

# =====================================================================
# FOOTER
# =====================================================================
FOOTER_COLUMNS = [
    {
        "title": "Belajar",
        "links": [
            {"label": "Manusia & Lobang", "endpoint": "learn_detail", "slug": "manusia-dan-lobang"},
            {"label": "Financial Freedom", "endpoint": "learn_detail", "slug": "financial-freedom"},
            {"label": "Pengembangan Diri", "endpoint": "learn_detail", "slug": "pengembangan-diri"},
            {"label": "Islam & Bekal Akhirat", "endpoint": "learn_detail", "slug": "islam-bekal-akhirat"},
            {"label": "Keluarga & Legacy", "endpoint": "learn_detail", "slug": "keluarga-legacy"},
        ],
    },
    {
        "title": "Explore",
        "links": [
            {"label": "Artikel", "endpoint": "learn", "slug": None},
            {"label": "Video", "endpoint": "resources", "slug": None},
            {"label": "Buku", "endpoint": "books", "slug": None},
            {"label": "Resources", "endpoint": "resources", "slug": None},
        ],
    },
    {
        "title": "Business",
        "links": [
            {"label": "Workshop", "endpoint": "business", "slug": None},
            {"label": "Team Program", "endpoint": "business", "slug": None},
            {"label": "Consulting", "endpoint": "business", "slug": None},
            {"label": "Partnership", "endpoint": "business", "slug": None},
        ],
    },
    {
        "title": "About",
        "links": [
            {"label": "Tentang", "endpoint": "about", "slug": None},
            {"label": "Contact", "endpoint": "join", "slug": None},
            {"label": "Privacy", "endpoint": "about", "slug": None},
            {"label": "Terms", "endpoint": "about", "slug": None},
        ],
    },
]
