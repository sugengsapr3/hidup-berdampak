"""Upgrade only verified, known Hadziq CBT HTML files to server-scored submissions.

The exact SHA-256 digest gates this migration; do not infer answer keys from
arbitrary user-uploaded JavaScript. The keys below were verified against the
three original 100-question files and are used solely on the server.
"""
import hashlib

KNOWN = {
    "8bf1b8622e308e7f67b3cdfaa8f823dcb12fb46688a809cb1e10667a5e939805": (
        "Dasar",
        "BCDACBADBACBDACBCADBCADBCADBCABCADBCADBCADBCADBCADBCADBCADBCADBCADBCADBCADBCADBCADBCADBCADBCADBCADBC",
    ),
    "2906a15289f9b2e9350ff1a50afa7271a68d7360de80ec0032a4657572047b13": (
        "Bertahap",
        "BCDACBADBCADBCADBCADBCADBCBCADBCADBCBCADBCADBCBCADBBCBCBCACBBBBCBCBCBBBAACBCCBBCCBCBCBCBCBBDBBBABBCC",
    ),
    "254dd91a127684c0972ca57f68fac7e1b4776e0eddb6425c8cd7b68ff5c60a6b": (
        "Sulit",
        "DBDDDCDAACADBBDCABDCBBCCCCCABDCACCCCABBDABDAADBBBBDDCCCADDDCDABABBCCABADDBDBDBBDCACCCAAABDDABBAAAACA",
    ),
}

NEEDLE = "function results(){show('result');"

# Submitted answers are graded on the server. The iframe never sends a score.
SUBMISSION = """if(!state.attempt_id){state.attempt_id='xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g,function(c){var r=Math.floor(Math.random()*16);return(c==='x'?r:(r&3|8)).toString(16);});save();}
try{window.parent.postMessage({type:'hb-cbt-submit-v1',attempt_id:state.attempt_id,answers:state.answers},'*');}catch(_e){}"""

def upgrade(html):
    """Return (patched_html, manifest) for an exact recognized original file."""
    digest = hashlib.sha256(html.encode("utf-8")).hexdigest()
    verified = KNOWN.get(digest)
    if verified is None:
        return None
    level, keys = verified
    if len(keys) != 100 or any(c not in "ABCD" for c in keys):
        return None
    if html.count(NEEDLE) != 1:
        return None
    patched = html.replace(NEEDLE, NEEDLE + SUBMISSION, 1)
    return patched, {"answer_keys": list(keys), "subject": "PAI, Bahasa Indonesia, Matematika, IPA, Bahasa Inggris, Psikotes"}
