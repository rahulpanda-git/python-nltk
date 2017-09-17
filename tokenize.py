from nltk.tokenize import word_tokenize, sent_tokenize
# word_tokenize is used to tokenize the string into different words
# sent_tokenize is used to tokenize string into different sentences
example = "Hello World. This is a String with many words and sentences. Let's see, how the NLTK tokenization works."
print(sent_tokenize(example))
# This will display all the different sentences in the String
print(word_tokenize(example))
# This will display all the different words in the string
