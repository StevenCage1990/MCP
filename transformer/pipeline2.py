from transformers import pipeline
generator = pipeline('text-generation')
res = generator('Where is the capital of China?')
print(res)