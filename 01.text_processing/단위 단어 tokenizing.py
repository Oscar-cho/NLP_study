import nltk
from nltk.tokenize import word_tokenize

sentence = "Natural Language Processing (NLP) is a subfield of computer science,\
    information engineering and artificial intelligence concerned between computers and human (natural)languages"

print(word_tokenize(sentence))