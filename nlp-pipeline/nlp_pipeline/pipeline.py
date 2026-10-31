"""Glue: runs steps 1-6 in the required order.  (Owner: Person C)

Order is fixed on purpose; flags only switch OPTIONAL steps on or off.
"""
from dataclasses import dataclass
from typing import Literal

from .unicode_norm import unicode_normalize, collapse_whitespace   # step 1  (A)
from .script_norm import script_normalize                           # step 2  (A)
from .case_fold import case_fold                                    # step 3  (B)
from .tokenizer import tokenize                                     # step 4  (B)
from .stopwords import remove_stopwords                             # step 5  (C)
from .stemming import stem, lemmatize                               # step 6  (C)


@dataclass
class PipelineConfig:
    unicode_form: str = "NFKC"
    language: str | None = None                  # e.g. "urdu", "arabic"; None = skip step 2
    lowercase: bool = True                       # step 3 (optional)
    keep_punct: bool = False                     # step 4
    remove_stopwords: bool = False               # step 5 (optional, usually a mistake)
    normalizer: Literal["none", "stem", "lemma"] = "none"   # step 6: pick one, never both


class NLPPipeline:
    def __init__(self, config: PipelineConfig | None = None):
        self.config = config or PipelineConfig()

    def run(self, text: str) -> list[str]:
        c = self.config
        text = unicode_normalize(text, c.unicode_form, strip_invisible=False)  # 1
        text = collapse_whitespace(text)
        text = script_normalize(text, c.language)                              # 2
        if c.lowercase:                                                        # 3
            text = case_fold(text)
        tokens = tokenize(text, keep_punct=c.keep_punct)                       # 4
        if c.remove_stopwords:                                                 # 5
            tokens = remove_stopwords(tokens)
        if c.normalizer == "stem":                                             # 6
            tokens = stem(tokens)
        elif c.normalizer == "lemma":
            tokens = lemmatize(tokens)
        return tokens

    def run_many(self, texts: list[str]) -> list[list[str]]:
        return [self.run(t) for t in texts]
