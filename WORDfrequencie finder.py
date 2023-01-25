import re
import numpy as np
import matplotlib.pyplot as plt


frequency = {}
document_text = open('test.txt', 'r')
textinstring = document_text.read().lower()
findwords = re.findall(r'\b[a-z]{3,15}\b', textinstring)

for word in findwords:
    count = frequency.get(word, 0)
    frequency[word] = count + 1
most_frequent = dict(sorted(frequency.items(), key=lambda elem: elem[1], reverse=True))
most_frequent_count = most_frequent.keys()

plt.bar(list(most_frequent.keys()), most_frequent.values(), color='g')
plt.show()

for words in most_frequent_count:
    print(words, most_frequent[words])
