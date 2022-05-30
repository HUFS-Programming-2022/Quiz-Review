# 1. [NLTK] text6에서 pt를 포함하는 단어 리스트를 출력하는 코드를 작성하세요.
import nltk
from nltk.book import *
nltk.download('book', quiet=True)

text = book.text6.tokens
text_pt = sorted(set([i.lower() for i in text if 'pt' in i]))
print(text_pt)




#3. 팩토리얼과 결과값 마지막 자리에서부터 0이 아닌 숫자가 나올때까지의 0의 개수 구하기

a = int(input("팩토리얼 입력값: "))
result = 1
for i in range(1, a+1):
    result *= i
print(f'{a}! =', result)

factorial = list(str(result))
factorial.reverse()
zero = 0
for i in factorial:
    if i == '0':
        zero += 1
    else:
        break
print('0의 개수:', zero)


#6. 별 찍기 프로그램

n = int(input('별 찍기 줄 수:'))
for i in range(n):
    for j in range(i):
        print(' ',end="")
    for j in range(n*2, 1+i*2, -1):
        print('*',end="")
    print('')
