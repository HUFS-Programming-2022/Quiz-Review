#!/usr/bin/env python
# coding: utf-8

# In[91]:


#1.

""" import 해야할 것들 몰아서 import 해주기 """

import nltk
from nltk.book import * 
nltk.download('book',quiet =True) 

""" 
text6에 있는 단어들을 순회하여 알파벳으로 이루어진 단어인 동시에 
소문자화했을 때 문자열 'pt'를 포함하는 단어들을 모아 정렬하여 
pt_word 라는 변수에 담는다.
pt_word를 출력한다.
"""

pt_word = sorted([word for word in text6 if word.isalpha() and 'pt' in word.lower()])
print(pt_word)


# In[93]:


#2.

"""
text1부터 text9까지를 texts라는 하나의 리스트에 담는다.
text를 출력할 때 사용할 번호를 지정해주기 위해 text_num = 1 로 둔다.
texts에 있는 text들을 순회하여 
    text에 있는 단어들을 소문자화하여 words라는 리스트에 담는다.
    
    'what'의 개수를 세서 word_what이라는 변수에 저장한다. 
    'when'의 개수를 세서 word_when이라는 변수에 저장한다. 
    'where'의 개수를 세서 word_where이라는 변수에 저장한다. 
    'who'의 개수를 세서 word_who이라는 변수에 저장한다. 
    'why'의 개수를 세서 word_why이라는 변수에 저장한다. 
    'which'의 개수를 세서 word_which이라는 변수에 저장한다. 
    
    아까 지정해두었던 text_num을 이용하여 각각의 코퍼스에서 빈도수를 출력한다.
    text_num을 1씩 증가시켜 text9까지 출력되게 한다.
"""

texts = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
text_num = 1
for text in texts:
    words = [word.lower() for word in text]
    
    word_what = words.count('what')
    word_when = words.count('when')
    word_where = words.count('where')
    word_who = words.count('who')
    word_why = words.count('why')
    word_which = words.count('which')
    
    print(f"text{text_num}: what={word_what}번, when={word_when}번, where={word_where}번, who={word_who}번, why={word_why}번, which={word_which}번")
    text_num += 1


# In[105]:


#4.

"""
첫번째 숫자를 first_num이란 변수로 입력받는다.
두번째 숫자를 second_num이란 변수로 입력받는다.

1부터 first_num까지 순회하며
    첫번째 숫자와 두번째 숫자를 나눈 값이 모두 0이 되게 하는 i가 있다면
    그 i를 gcd(최대공약수)로 저장한다.
    
두수의 곱을 최대공약수로 나눈 값을 lcm(최소공배수)에 저장한다.

최대공약수와 최소공배수를 각각 출력한다.
"""

first_num = int(input("첫번째 숫자를 입력하세요 : "))
second_num = int(input("두번째 숫자를 입력하세요 : "))

for i in range(1, first_num + 1):
    if (first_num % i == 0) and (second_num % i == 0):
        gcd = i 
        
lcm = int((first_num*second_num)/gcd)

print(f'{first_num}과 {second_num}의 최대공약수는 {gcd}입니다.')
print(f'{first_num}과 {second_num}의 최소공배수는 {lcm}입니다.')


# In[87]:


#6.
"""
input 함수를 이용하여 별 찍기 숫자를 입력받는다.
*을 star라는 변수에 저장한다.
공백을 blank라는 변수에 저장한다. 

1부터 n까지 순회하여
    별의 개수를 나타내는 (2*n)-(2*i-1) 식을 star_num 변수에 저장한다.
    한 쪽의 공백의 개수를 나타내는 i-1 식을 blank_num 변수에 저장한다.
    
    공백의 개수, 별의 개수, 공백의 개수를 한 줄에 출력한다.
"""
n = int(input('별 찍기 숫자를 입력하세요: '))
star = '*'
blank = ' '

for i in range(1, n+1):
    star_num = (2*n)-(2*i-1)
    blank_num = i-1
    
    print(blank*blank_num, star_num*star, blank*blank_num)

