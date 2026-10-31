from nlp_pipeline import NLPPipeline, PipelineConfig

samples = """The quick brown fox jumps over the lazy dog. The dog, however, wasn't impressed and kept sleeping under the old oak tree.
Natural Language Processing (NLP) helps computers understand human language. It is used in search engines, chatbots, translation, and spam filters.
I don't think this movie is good. The plot was boring, the acting was terrible, and the ending made no sense at all!
I absolutely loved this movie! The acting was brilliant, the soundtrack was beautiful, and I would happily watch it again.
Dr. Smith paid $1,250.75 for 3 tickets on 12/05/2025. The flight leaves at 6:30 PM from Terminal 2.
State-of-the-art models are trained on billions of words, yet well-known problems like sarcasm and ambiguity remain unsolved.
Students were studying hard; the studies showed that running, jumping, and swimming improve memory and focus.
The cats are running faster than the dogs, and the children were playing happily in the beautiful gardens.
Please email support@example.com or visit https://www.example.com/help for more information. Prices rose 15% in 2024.
She said, "Machine learning is not magic; it's mathematics, data, and a lot of patience." Everyone agreed.
Café society loves naïve résumé jokes. The café on Straße 5 serves crème brûlée every morning.
Decomposed: café and résumé look identical to café and résumé, but they are different in memory until normalized.
Fullwidth text: ＮＬＰ ＩＳ ＦＵＮ １２３. Ligatures: ofﬁce, eﬃcient, ﬂow, ﬁnal.
Spaces that are non-breaking,   multiple    spaces,	and	tabs	should all collapse into single spaces.
Superscripts like m² and H₂O, fractions like ½ and ¾, and the symbol ™ are compatibility characters.
Apple released a new phone in California. Google and Microsoft announced updates to their cloud platforms in London and Tokyo.
The market was bullish today. Investors were buying stocks, selling bonds, and watching interest rates very carefully.
Reading books improves vocabulary. Readers who read daily have read more pages than those who rarely read anything.
It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness.
Can't, won't, shouldn't, they're, we've, I'm, it's, and y'all are all common English contractions worth testing.
Climate change is affecting weather patterns worldwide. Scientists warn that rising temperatures could change agriculture forever.
Python is a popular programming language. Developers write functions, classes, and tests to build reliable software quickly.
Hospitals are using AI to analyze scans. Doctors say these tools are helpful, but they must never replace human judgment.
Running late, he quickly ran to the station, but the train had already left. Frustrated, he walked home slowly.
Better, best, worse, worst, good, bad: irregular forms are where stemmers and lemmatizers behave very differently.
The mice ate the cheese while the geese flew over the feet of the sleeping men and women.
Education is the most powerful weapon which you can use to change the world, and it begins with curiosity."""

# One document per line
docs = [line for line in samples.splitlines() if line.strip()]

print("1) Default (normalize, lowercase, tokenize)")
print(NLPPipeline().run_many(docs)[:3])

print("\n2) Stop-word removal + stemming")
cfg = PipelineConfig(remove_stopwords=True, normalizer="stem")
print(NLPPipeline(cfg).run_many(docs)[:3])

print("\n3) Lemmatization (needs internet the first time)")
cfg = PipelineConfig(normalizer="lemma")
print(NLPPipeline(cfg).run_many(docs)[:3])
