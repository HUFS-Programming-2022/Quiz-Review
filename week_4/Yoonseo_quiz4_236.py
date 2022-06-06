# 2.

import nltk
from nltk.corpus import gutenberg
nltk.download(['brown', 'gutenberg'], quiet=True)

vowel = 'a', 'e', 'i', 'o', 'u'
text = [i for i in gutenberg.fileids() if i.startswith(vowel)] #모음으로 시작하는 파일 고르기

for i in text:
    sent = gutenberg.words(i)[:500] # 너무 길어서 각 텍스트 당 500단어까지만
    texts = ' '.join([w for w in sent if w.isalpha()])
           #join() = 모든 단어를 하나의 스트링으로
            #isalpha() = 숫자, 문장부호 제외 순수 알파벳만 있는 단어들 # 구텐버그는 리스트 단어분절 속에 'early,' 와 같이 알파벳과 숫자/문장부호가 붙어있는 경우가 없으므로 이걸로 충분    
    print(texts) 
    print(' ') # 각 텍스트 구분하기 위한 줄바꿈



#3

#이 풀이가 cfd를 사용한 것인지는 잘 모르겠습니다.
#cfd.tabulate()나 .plot()을 사용해보려고 여러 시도를 해보았지만
#세로줄엔 각 카테고리 이름 나열하고,
#가로줄엔 hapax라고 한 칸만 있고 그 아래 각 카테고리의 hapax 개수를 순서대로 쓰는 표 모양을 생각해봤으나 그렇게 가로줄을 한 칸만 구현하는 법을 모르겠습니다..
#     123  222  345
#c1   0    1    0
#c2   1    0    0
#c3   0    0    1      이런 식으로 tabulate() 결과가 나온 적 있었는데 이건 아닌 것 같아서 아래처럼 작성했습니다.

brown = nltk.corpus.brown
category = brown.categories()
print('<브라운에서 각 장르별 hapax의 개수>')
for c in category:
    fdist = nltk.FreqDist([w.lower() for w in brown.words(categories = c)])
    hapax = fdist.hapaxes()
    print(f'{c} = {len(hapax)}')



#6

import random
n = random.randint(1, 300)
print('n =', n) #n의 값 확인

i = 2
numlist = [1] #소인수 목록은 기본적으로 1포함
while n != 1:
    if n % i == 0 :
        n = n//i
        numlist.append(i)
    else :
        i += 1
soinsu = set(numlist) #중복 제거 소인수 리스트
print(f"= {'*'.join(map(str, numlist))}") # n의 값을 소인수분해하면 나오는 식
print(f'입력값의 소인수: {soinsu}')

