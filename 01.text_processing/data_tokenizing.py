from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import TreebankWordDetokenizer
from nltk.tokenize import sent_tokenize
from nltk.tag import pos_tag
from tensorflow.keras.preprocessing.text import text_to_word_sequence

import kss

tokenizer = TreebankWordDetokenizer()

text1 = "Don't be fooled by the dark sounding name, Mr.Jone's Orphange is as cheery as cheery goes for a pastry shop."
text2 = "Starting a home-based restaurant may be an ideal.it doesn't have a food chain or restaurant of their own."
text3 = "His barber kept his word. But keeping such a huge secret to himself was driving him crazy.\
        Finally, the barber went up a mountain and almost to the edge of a cliff.\
        He dug a hole in the midst of some reeds.He looked about, to make sure no one was near"
text4 = "I am actively looking for Ph.D. students and you are a Ph.D student."
text5 = "딥 러닝 자연어 처리가 재미있기는 합니다.그런데 영어보다 한국어로 할 때 너무 어렵습니다.이제 해보면 알겠죠!"

tokenized_sentence = word_tokenize(text4)

print('단어 토큰화 1 : ', word_tokenize(text1))

print('단어 토근화 2: ', WordPunctTokenizer().tokenize(text1))

print('단어 토큰화 3: ', text_to_word_sequence(text1))

print('트리뱅크 워드토크나이저 : ', tokenizer.tokenize(text2))

print('문장 토큰화1 :', sent_tokenize(text3))

print('문장 토큰화2 :', sent_tokenize(text4))

print('한국어 문장 토큰화1 : ', kss.split_sentences(text5))

print('단어 토큰화 : ', tokenized_sentence)

print('품사 태깅 : ', pos_tag(tokenized_sentence))