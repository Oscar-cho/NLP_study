from konlpy.tag import Okt
okt = Okt()

text = "한글 자연어 처리는 재밌다.이제부터 열심히 해야지 ㅎㅎㅎ"

print("문장 추출입니다 : " , okt.morphs(text))
print("문장에서 형태소 단위로 나눈 후 어간 추출입니다 : ", okt.morphs(text, stem = True))  # 형태소 단위로 나눈 후 어간을 추출
print("문장에서 명사를 추출했습니다 : " , okt.nouns(text))
print("문장에서 어절 추출입니다 : " , okt.phrases(text))