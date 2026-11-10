"""Single source of truth for editable Learning Hub subject choices.

The first rollout covers familiar school subjects and early-childhood topics.
Existing Mathematics content stays valid.
"""
CHILDREN = {
    "dzaky": ("Dzaky Albarra", "SMA Kelas 10"),
    "hadziq": ("Hadziq Dizhwar", "SMP Kelas 9"),
    "fiori": ("Fiori Ghania Albina", "SD Kelas 5"),
    "hazel": ("Hazel Aghnia Dinara", "PAUD"),
}
SUBJECTS = {
    "dzaky": ("Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika",
              "Kimia", "Biologi", "Ekonomi", "Geografi", "Sejarah",
              "Sosiologi", "PAI", "Bahasa Arab", "Bahasa Mandarin"),
    "hadziq": ("Matematika", "Bahasa Indonesia", "Bahasa Inggris", "IPA",
               "IPS", "PAI", "Bahasa Arab", "Psikotes"),
    "fiori": ("Matematika", "Bahasa Indonesia", "Bahasa Inggris", "IPAS",
              "PAI", "Bahasa Arab"),
    "hazel": ("Matematika", "Pra-Membaca", "Pra-Menulis", "Bahasa Indonesia",
              "Bahasa Inggris", "Mengenal Warna dan Bentuk"),
}

def allowed(child, subject):
    return child in SUBJECTS and subject in SUBJECTS[child]
