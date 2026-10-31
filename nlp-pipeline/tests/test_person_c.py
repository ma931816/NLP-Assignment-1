import pytest
from nlp_pipeline import remove_stopwords, stem, NLPPipeline, PipelineConfig


def test_remove_stopwords_basic():
    assert remove_stopwords(["The", "cat", "is", "on", "the", "mat"]) == ["cat", "mat"]


def test_negation_is_kept():
    assert remove_stopwords(["not", "good"]) == ["not", "good"]


def test_custom_stopwords():
    assert remove_stopwords(["a", "b"], stopwords={"a"}) == ["b"]


def test_stem():
    assert stem(["running", "studies", "cats"]) == ["run", "studi", "cat"]


def test_pipeline_default():
    assert NLPPipeline().run("Hello, World!") == ["hello", "world"]


def test_pipeline_equal_for_unicode_variants():
    p = NLPPipeline()
    assert p.run("café") == p.run("café")


def test_pipeline_full_english():
    cfg = PipelineConfig(remove_stopwords=True, normalizer="stem")
    assert NLPPipeline(cfg).run("The cats are running") == ["cat", "run"]


def test_pipeline_urdu():
    cfg = PipelineConfig(language="urdu")
    assert NLPPipeline(cfg).run("كتاب ٢٠٢٥") == ["کتاب", "2025"]


def test_pipeline_keeps_case_when_disabled():
    cfg = PipelineConfig(lowercase=False)
    assert NLPPipeline(cfg).run("Ali Khan") == ["Ali", "Khan"]
