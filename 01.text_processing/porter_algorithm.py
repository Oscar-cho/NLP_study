from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer

porter_stemmer = PorterStemmer()
lancaster_stemmer = LancasterStemmer()

words = ['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']

print('어간 추출 전  : ', words)
print('포터 스테머의 어간 추출 후 : ', [porter_stemmer.stem(w) for w in words])
print('랭커스터 스테머의 어간 추출 후 : ', [lancaster_stemmer.stem(w) for w in words])

