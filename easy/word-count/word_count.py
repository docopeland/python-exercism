import re
import collections

def count_words(sentence):
    words = re.sub("[^0-9A-Za-z']+"," ",sentence).lower().split()
    counts = dict()
    for word in words:
        if word.startswith("'") and word.endswith("'"):
            word = word[1:-1]
            if word.startswith("'") and word.endswith("'"):
                word = word[1:-1]
        counts[word] = counts.get(word,0)+1
    return counts