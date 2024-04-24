import nltk
from nltk.corpus import stopwords
from string import punctuation
from collections import Counter

with open("random_paragraphs.txt", "r") as file:
    text = file.read()

words = nltk.word_tokenize(text)

stop_words = set(stopwords.words('english'))

filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
filtered_words_without_punct = [word for word in filtered_words if word not in punctuation]

word_freq = Counter(filtered_words_without_punct)
for word, freq in word_freq.items():
    print(f"{word}: {freq}")

#to make a new text file without the stop words or punctuation 
#filtered_text = " ".join(filtered_words_without_punct)

#with open("filtered_random_paragraphs.txt", "w") as outfile:
    outfile.write(filtered_text)
    

