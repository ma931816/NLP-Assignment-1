"""Step 5: Stop-word removal.  (Owner: Person C)

Optional, and usually a mistake: stop words carry meaning for modern models
("not good" -> "good" flips sentiment). Use only for classic bag-of-words / search tasks.
"""

# Deliberately small built-in list so there is no download step.
# NOTE: negations (not, no, nor) are intentionally EXCLUDED to avoid flipping meaning.
ENGLISH_STOPWORDS = frozenset("""
a about above after again against all am an and any are as at be because been before
being below between both but by can did do does doing down during each few for from
further had has have having he her here hers herself him himself his how i if in into
is it its itself just me more most my myself of off on once only or other our ours
ourselves out over own same she should so some such than that the their theirs them
themselves then there these they this those through to too under until up very was we
were what when where which while who whom why will with you your yours yourself
yourselves
""".split())


def remove_stopwords(tokens: list[str], stopwords: frozenset[str] | set[str] | None = None) -> list[str]:
    """Drop tokens that are in `stopwords` (default: ENGLISH_STOPWORDS).

    Comparison is case-insensitive; original token casing is preserved in the output.
    """
    sw = ENGLISH_STOPWORDS if stopwords is None else stopwords
    return [t for t in tokens if t.casefold() not in sw]
