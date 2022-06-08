# 1. [NLTK] text6에서 pt를 포함하는 단어 리스트를 출력하는 코드를 작성하세요.

import nltk
from nltk.book import *
nltk.download('book', quiet=True)

text = nltk.book.text6.tokens
text_pt = sorted([i for i in text if 'pt' in i.lower()])
print(text_pt)


# 3. 팩토리얼을 구한 뒤, 결과값의 맨 마지막 자리에서 시작해서 처음으로 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 함수를 만드시오.

n = int(input('팩토리얼을 구할 정수: '))

start = 1
for i in range(1, n+1):
    start *= i
print(f'{n}! =', start)
# ---- 여기까지 팩토리얼 구하기 ----

# 결과값의 맨 마지막 자리에서 시작해서 처음으로 0이 아닌 숫자가 나올 때까지 0의 개수 구하기
# '자리' -> 인덱스화 하기
    # 먼저 문자열로 만들기
start = str(start)
zero = 0 #0의 개수
for z in range(1, len(start)):
    if start[-z] == '0':
        zero += 1
    else:
        break
print('0의 개수:', zero)



#5. 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.


n = int(input('사이클을 구할 정수(0 <= n <= 99): '))

first = int(n / 10) # 10의자리 수
second = n % 10
output = first + second #각 자릿수를 합한 값
cycle = 1
if output != n:
    flag = True
    while flag:
        first = second #'주어진 수의 가장 오른쪽 자리 수'
        second = output%10 #'앞에서 구한 합의 가장 오른쪽 자리 수'
        m = first*10 + second # ~를 이어 붙여서 만든 '새로운 수'
        print(m) #사이클이 어떻게 돌아가고 있는지 알아보기 위해 새로운 수 출력
        output = first + second #새로운 수를 만들기 위해 필요
        if n == m : #새로 만들어진 수가 원래 수와 같다면
            flag = False
        else:
            cycle += 1
            
print(f'총 사이클: {cycle}번')
