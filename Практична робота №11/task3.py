import nltk
from nltk.corpus import gutenberg, stopwords
from nltk.probability import FreqDist
import string
import matplotlib.pyplot as plt

nltk.download('gutenberg', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

words = gutenberg.words('shakespeare-macbeth.txt')
print("Загальна кількість слів:", len(words))

words_lower =[w.lower() for w in words]
top_10_raw = FreqDist(words_lower).most_common(10)
print("Топ-10 (до фільтрації):", top_10_raw)

w_raw, c_raw = zip(*top_10_raw)
plt.figure(figsize=(8, 4))
plt.bar(w_raw, c_raw, color='skyblue')
plt.savefig('task3_plot1.png')
plt.show()

stop_w = set(stopwords.words('english'))
punct = set(string.punctuation)

filtered =[w.lower() for w in words if w.lower() not in stop_w and w.lower() not in punct and w.isalpha()]
top_10_clean = FreqDist(filtered).most_common(10)
print("Топ-10 (після фільтрації):", top_10_clean)

w_cl, c_cl = zip(*top_10_clean)
plt.figure(figsize=(8, 4))
plt.bar(w_cl, c_cl, color='lightgreen')
plt.savefig('task3_plot2.png')
plt.show()