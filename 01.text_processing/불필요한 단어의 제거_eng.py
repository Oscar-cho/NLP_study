import re
text = "I was wondering if anyone out there could enlighten me on this car."

# 길이가 1~2인 단어들을 정규 표현식을 이용하여 삭제한다.
shortword = re.compile(r'\W*\b\w{1,2}\b')
print(shortword.sub('', text))

# 이건 길이가 2~3인 단어들을 삭제
shortword = re.compile(r'\W*\b\w{2,3}\b')
print(shortword.sub('', text))