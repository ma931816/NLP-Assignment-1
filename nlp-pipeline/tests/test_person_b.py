from nlp_pipeline import case_fold, tokenize, whitespace_tokenize


def test_casefold_beats_lower():
    assert case_fold("Straße") == "strasse"
    assert "Straße".lower() != "strasse"


def test_tokenize_basic():
    assert tokenize("Hello, world!") == ["Hello", "world"]


def test_tokenize_keeps_punct_when_asked():
    assert tokenize("Hi!", keep_punct=True) == ["Hi", "!"]


def test_tokenize_contractions_and_hyphens():
    assert tokenize("don't use state-of-the-art") == ["don't", "use", "state-of-the-art"]


def test_tokenize_numbers():
    assert tokenize("pi is 3.14 and 1,000") == ["pi", "is", "3.14", "and", "1,000"]


def test_tokenize_non_latin():
    assert tokenize("یہ ایک جملہ ہے۔") == ["یہ", "ایک", "جملہ", "ہے"]


def test_whitespace_tokenize():
    assert whitespace_tokenize("a  b\tc") == ["a", "b", "c"]
