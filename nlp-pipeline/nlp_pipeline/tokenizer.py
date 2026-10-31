"""Step 4: Tokenization.  (Owner: Person B)

Everything in steps 1-3 must happen BEFORE this, because tokenizers
split on characters, and un-normalized text produces inconsistent tokens.
"""
import re

# Words (with internal apostrophes/hyphens kept: don't, state-of-the-art),
# numbers (with decimals/commas), or any single non-space symbol.
_TOKEN_RE = re.compile(
    r"""
    \d+(?:[.,]\d+)*              # numbers: 3.14, 1,000
    | \w+(?:['’\-]\w+)*          # words incl. don't, well-known
    | [^\w\s]                    # single punctuation / symbol
    """,
    re.VERBOSE | re.UNICODE,
)


def tokenize(text: str, keep_punct: bool = False) -> list[str]:
    """Split `text` into tokens.

    Args:
        text: normalized text.
        keep_punct: if False (default), punctuation-only tokens are dropped.
    """
    tokens = _TOKEN_RE.findall(text)
    if not keep_punct:
        tokens = [t for t in tokens if any(ch.isalnum() for ch in t)]
    return tokens


def whitespace_tokenize(text: str) -> list[str]:
    """Simplest baseline tokenizer: split on whitespace only."""
    return text.split()
