"""Step 6: Stemming OR lemmatization.  (Owner: Person C)

Optional. Pick one, never both.
  - stem:  fast, crude suffix chopping      ("studies" -> "studi")
  - lemma: dictionary based, real words     ("studies" -> "study")
"""
from nltk.stem import PorterStemmer

_stemmer = PorterStemmer()
_lemmatizer = None


def stem(tokens: list[str]) -> list[str]:
    """Porter-stem every token."""
    return [_stemmer.stem(t) for t in tokens]


def _get_lemmatizer():
    """Lazily build the WordNet lemmatizer, downloading the data on first use."""
    global _lemmatizer
    if _lemmatizer is None:
        import nltk
        from nltk.stem import WordNetLemmatizer
        try:
            nltk.data.find("corpora/wordnet")
        except LookupError:
            nltk.download("wordnet", quiet=True)
        _lemmatizer = WordNetLemmatizer()
    return _lemmatizer


def lemmatize(tokens: list[str], pos: str = "n") -> list[str]:
    """WordNet-lemmatize every token (pos: 'n' noun, 'v' verb, 'a' adj, 'r' adv)."""
    lem = _get_lemmatizer()
    return [lem.lemmatize(t, pos=pos) for t in tokens]
