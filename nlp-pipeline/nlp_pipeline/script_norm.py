"""Step 2: Script-specific normalization.  (Owner: Person A)

Language rules that Unicode normalization does NOT cover.
Implemented here: Arabic-script (Arabic / Urdu / Persian).
Add more scripts by writing another function and registering it in SCRIPT_NORMALIZERS.
"""
import re

# --- Arabic-script rules -------------------------------------------------

TATWEEL = "ـ"  # kashida, purely decorative stretching
# Harakat / diacritics: fathatan..sukun, superscript alef
ARABIC_DIACRITICS = re.compile(r"[ً-ْٰ]")

# Characters that look alike / are used interchangeably across Arabic, Urdu, Persian.
ARABIC_CHAR_MAP = {
    "آ": "ا",  # آ  -> ا   (alef with madda)
    "أ": "ا",  # أ  -> ا
    "إ": "ا",  # إ  -> ا
    "ى": "ی",  # ى  -> ی   (alef maksura -> Farsi/Urdu yeh)
    "ي": "ی",  # ي  -> ی   (Arabic yeh -> Farsi/Urdu yeh)
    "ك": "ک",  # ك  -> ک   (Arabic kaf -> Urdu/Persian kaf)
    "ۀ": "ہ",  # ۀ  -> ہ   (heh with yeh above -> heh goal)
}
_ARABIC_TABLE = str.maketrans(ARABIC_CHAR_MAP)

# Arabic-Indic and Extended Arabic-Indic digits -> ASCII digits
_DIGIT_TABLE = {ord(c): str(i) for i, c in enumerate("٠١٢٣٤٥٦٧٨٩")}
_DIGIT_TABLE.update({ord(c): str(i) for i, c in enumerate("۰۱۲۳۴۵۶۷۸۹")})


def normalize_arabic_script(text: str, remove_diacritics: bool = True,
                            normalize_digits: bool = True) -> str:
    """Normalize Arabic / Urdu / Persian text."""
    text = text.replace(TATWEEL, "")
    if remove_diacritics:
        text = ARABIC_DIACRITICS.sub("", text)
    text = text.translate(_ARABIC_TABLE)
    if normalize_digits:
        text = text.translate(_DIGIT_TABLE)
    return text


# --- Registry ------------------------------------------------------------

SCRIPT_NORMALIZERS = {
    "arabic": normalize_arabic_script,  # also use for "urdu", "persian"
    "urdu": normalize_arabic_script,
    "persian": normalize_arabic_script,
}


def script_normalize(text: str, language: str | None = None) -> str:
    """Apply the script-specific normalizer for `language`.

    If `language` is None or has no registered normalizer, text is returned unchanged
    (e.g. plain English needs no script-specific step).
    """
    if language is None:
        return text
    fn = SCRIPT_NORMALIZERS.get(language.lower())
    return fn(text) if fn else text
