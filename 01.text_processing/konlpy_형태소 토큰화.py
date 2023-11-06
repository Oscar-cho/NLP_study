from konlpy.tag import Okt
from konlpy.tag import Kkma

okt = Okt()
kkma = Kkma()

text = "열심히 코딩한 당신, 연휴에는 여행을 가봐요"
print('Okt 형태소 분석: ', okt.morphs(text))
print('Okt 품사 태깅 : ', okt.pos(text))
print('Okt 명사 추출 : ', okt.nouns(text))

print('꼬꼬마 형태소 분석: ', kkma.morphs(text))
print('꼬꼬마 품사 태깅: ', kkma.pos(text))
print('꼬꼬마 명사 추출: ', kkma.nouns(text))