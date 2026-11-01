"""Step 1: Unicode normalization.  (Owner: Person A)

Goal: make identical-looking text identical in memory.
Example: "é" can be one code point (U+00E9) or "e" + combining accent (U+0065 U+0301).
"""
import unicodedata

VALID_FORMS = {"NFC", "NFD", "NFKC", "NFKD"}

# Invisible characters that break string equality but are invisible to the eye.
INVISIBLE_CHARS = {
    "​",  # zero width space
    "‌",  # zero width non-joiner (see note in script_norm.py for Persian/Urdu)
    "‍",  # zero width joiner
    "⁠",  # word joiner
    "﻿",  # BOM / zero width no-break space
}


def unicode_normalize(text: str, form: str = "NFKC", strip_invisible: bool = False) -> str:
    """Normalize `text` to the given Unicode form.

    NFKC is the default: it composes characters AND maps compatibility
    variants (e.g. fullwidth 'Ａ' -> 'A', 'ﬁ' ligature -> 'fi', '²' -> '2').

    Args:
        text: input string.
        form: one of NFC, NFD, NFKC, NFKD.
        strip_invisible: also remove zero-width characters.
    """
    if form not in VALID_FORMS:
        raise ValueError(f"form must be one of {sorted(VALID_FORMS)}, got {form!r}")
    text = unicodedata.normalize(form, text)
    if strip_invisible:
        text = "".join(ch for ch in text if ch not in INVISIBLE_CHARS)
    return text


def collapse_whitespace(text: str) -> str:
    """Replace any run of whitespace (tabs, newlines, NBSP...) with one space."""
    return " ".join(text.split())
