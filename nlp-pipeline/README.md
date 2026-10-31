# NLP Text Cleaning & Normalization Pipeline

Runs in this fixed order:

| # | Step | Required? | File | Owner |
|---|------|-----------|------|-------|
| 1 | Unicode normalization | yes | `nlp_pipeline/unicode_norm.py` | **Person A** |
| 2 | Script-specific normalization | per language | `nlp_pipeline/script_norm.py` | **Person A** |
| 3 | Case folding | optional | `nlp_pipeline/case_fold.py` | **Person B** |
| 4 | Tokenization | yes | `nlp_pipeline/tokenizer.py` | **Person B** |
| 5 | Stop-word removal | optional (usually a mistake) | `nlp_pipeline/stopwords.py` | **Person C** |
| 6 | Stemming **or** lemmatization | optional, never both | `nlp_pipeline/stemming.py` | **Person C** |
| - | Pipeline glue + `__init__.py` | - | `nlp_pipeline/pipeline.py` | **Person C** |

## Interface contract (so everyone's code plugs together)

- Steps 1-3: `str -> str`
- Step 4: `str -> list[str]`
- Steps 5-6: `list[str] -> list[str]`

## Setup

```bash
pip install -r requirements.txt
pytest            # all tests
python main.py    # demo
```

## Usage

```python
from nlp_pipeline import NLPPipeline, PipelineConfig

pipe = NLPPipeline(PipelineConfig(remove_stopwords=True, normalizer="stem"))
pipe.run("The cats are running")   # ['cat', 'run']
```

## Git workflow

1. One person (e.g. Person C) creates the repo, pushes this skeleton to `main`.
2. Each person creates a branch: `feature/person-a-normalization`, `feature/person-b-tokenization`, `feature/person-c-pipeline`.
3. Only edit your own files and your own `tests/test_person_x.py`.
4. Open a Pull Request into `main`; at least one teammate reviews.
5. Merge, then `git pull` before starting new work.
