import re
from collections import defaultdict
with open("sample_.txt", "r") as file:
    text = file.read()
words = text.split()
word_freq = defaultdict(int)
for word in words:
    word = re.sub(r'[^\w\s]', '', word).lower()
    if word:
        word_freq[word] += 1
sorted_word_freq = dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True))
for word, freq in sorted_word_freq.items():
    print(f"{word}: {freq}")
