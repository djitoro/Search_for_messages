# Hypotheses:
# 1. Use words as toxins and count the scalar product

# import pandas as pd
# import numpy as np
from gensim.models import Word2Vec
import re


with open('corpus.txt', 'r', encoding='utf-8') as f:
    sentences = f.readlines()


def tokenize(text):
    return re.findall(r'\w+|[^\w\s]', text, re.UNICODE)


sentences_tokenized = [tokenize(sentence) for sentence in sentences]

model = Word2Vec(sentences=sentences_tokenized,
                 vector_size=300,
                 window=5,
                 min_count=5,
                 workers=4)
