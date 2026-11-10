"""Supported subjects for all four children's Learning Hubs.

Historical subjects remain readable in existing records; this list controls
which subjects can be selected for newly uploaded material and new exam drafts.
"""
CHILDREN = {
    "dzaky": ("Dzaky Albarra", "SMA Kelas 10"),
    "hadziq": ("Hadziq Dizhwar", "SMP Kelas 9"),
    "fiori": ("Fiori Ghania Albina", "SD Kelas 5"),
    "hazel": ("Hazel Aghnia Dinara", "PAUD"),
}
CORE_SUBJECTS = ("Matematika", "IPA", "Bahasa Inggris",
                 "Agama Islam", "Tajwid", "Psikotes")
SUBJECTS = {slug: CORE_SUBJECTS for slug in CHILDREN}

def allowed(child, subject):
    return child in SUBJECTS and subject in SUBJECTS[child]
