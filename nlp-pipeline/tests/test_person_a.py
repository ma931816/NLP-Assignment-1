from nlp_pipeline import unicode_normalize, collapse_whitespace, script_normalize


def test_composed_and_decomposed_become_equal():
    composed = "café"
    decomposed = "café"
    assert composed != decomposed
    assert unicode_normalize(composed) == unicode_normalize(decomposed)


def test_nfkc_maps_compatibility_chars():
    assert unicode_normalize("ＡＢＣ") == "ABC"   # fullwidth
    assert unicode_normalize("ﬁ") == "fi"                 # ligature


def test_strip_invisible():
    assert unicode_normalize("a​b", strip_invisible=True) == "ab"


def test_bad_form_raises():
    import pytest
    with pytest.raises(ValueError):
        unicode_normalize("x", form="BOGUS")


def test_collapse_whitespace():
    assert collapse_whitespace("a \t\n  b c") == "a b c"


def test_arabic_yeh_kaf_and_diacritics():
    assert script_normalize("كتاب", "urdu") == "کتاب"          # Arabic kaf -> Urdu kaf
    assert script_normalize("مُحَمَّد", "arabic") == "محمد"    # diacritics removed


def test_arabic_digits():
    assert script_normalize("٢٠٢٥ ۲۰۲۵", "urdu") == "2025 2025"


def test_tatweel_removed():
    assert script_normalize("اللـــه", "arabic") == "الله"


def test_unknown_language_is_noop():
    assert script_normalize("Hello", "english") == "Hello"
    assert script_normalize("Hello", None) == "Hello"
