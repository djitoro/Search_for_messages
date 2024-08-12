import pandas as pd
import numpy as np

with open('corpus.txt', 'r', encoding='utf-8') as file:
    data: str = file.read()

print(data[1:100:1])
