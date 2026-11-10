"""Trusted subject breakdown for the verified 100-question Ibad Arrahman exams.

Never infer categories by evenly dividing questions: the difficult exam
interleaves subject areas and the intermediate exam has three level sections.
"""
from cbt_legacy_bridge import KNOWN

SUBJECT_CODES = {
    "P": "PAI",
    "I": "Bahasa Indonesia",
    "M": "Matematika",
    "S": "IPA",
    "E": "Bahasa Inggris",
    "T": "Psikotes",
}
SUBJECT_ORDER = list(SUBJECT_CODES.values())
KNOWN_PATTERNS = {
    "Dasar": "P"*15 + "I"*15 + "M"*20 + "S"*20 + "E"*20 + "T"*10,
    "Bertahap": "PPPPPPPPIIIIIIIIMMMMMMMMMMSSSSSSSSSSEEEEEEEEEETTTTPPPPIIIIMMMMMMSSSSSSEEEEEETTTTPPPIIIMMMMSSSSEEEETT",
    "Sulit": "PIMSETPIMSETPIMSETPIMSETPIMSETPIMSETPIMSETPIMSETPIMSETPIMSETPIMSEPIMSEPIMSEPIMSEPIMSEMSEMSEMSEMSEMSE",
}
KNOWN_SUBJECTS = {
    keys: [SUBJECT_CODES[c] for c in KNOWN_PATTERNS[level]]
    for level, keys in (value for value in KNOWN.values())
}

def get_subjects(manifest):
    """Use validated categories or verified legacy answer-key fingerprints."""
    if not isinstance(manifest, dict):
        return None
    keys = manifest.get("answer_keys")
    if not isinstance(keys, list):
        return None
    declared = manifest.get("question_subjects")
    if (isinstance(declared, list) and len(declared) == len(keys)
            and all(x in SUBJECT_ORDER for x in declared)):
        return declared
    return KNOWN_SUBJECTS.get("".join(keys))


def ensure_subject_table(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS cbt_subject_scores (
            result_id INTEGER NOT NULL REFERENCES learning_results(id) ON DELETE CASCADE,
            subject TEXT NOT NULL,
            correct_count INTEGER NOT NULL,
            total_questions INTEGER NOT NULL,
            PRIMARY KEY(result_id, subject)
        )
    """)
