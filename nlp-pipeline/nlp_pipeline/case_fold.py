"""Step 3: Case folding.  (Owner: Person B)

Optional and task-dependent. Keep case for NER or POS tagging; fold for search / bag-of-words.
"""


def case_fold(text: str) -> str:
    """Aggressive, Unicode-aware lowercasing.

    str.casefold() is stronger than str.lower(): 'Straße'.casefold() == 'strasse'.
    Note: Turkish dotted/dotless I needs locale-specific handling and is not covered.
    """
    return text.casefold()
