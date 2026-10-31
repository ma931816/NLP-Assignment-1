from nlp_pipeline import NLPPipeline, PipelineConfig

samples = [
    "The Ｃats are running, and the café is open!",
    "Hello World"
]

print("English, full pipeline:")
cfg = PipelineConfig(remove_stopwords=True, normalizer="stem")
print(NLPPipeline(cfg).run(samples[0]))

print("\nEnglish script:")
print(NLPPipeline(PipelineConfig(language="English")).run(samples[1]))
