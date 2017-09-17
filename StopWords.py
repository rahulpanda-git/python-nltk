from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example = "Hello, we will be separating out some meaningful words from this text using the nltk stop words."

words = word_tokenize(example)
# Tokenizing the String according to words

filtered_words = []
stop_words = set(stopwords.words("english"))
# stop_words will now contain a list of common words in English Language

for w in words:
    for w not in stop_words:
        filtered_words.append(w)
#Filtered Words will now contain those English words from the string which are not common

print(filtered_words) #Print the important (un-common) words
