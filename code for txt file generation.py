#to make a new text file without the stop words or punctuation 


filtered_text = " ".join(filtered_words_without_punct)

with open("filtered_random_paragraphs.txt", "w") as outfile:
    outfile.write(filtered_text)
