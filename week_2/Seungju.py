#!/usr/bin/env python
# coding: utf-8

# In[123]:


""" import 해야할 것들 몰아서 import 해주기 """

import nltk
from nltk.book import *
nltk.download('book',quiet =True)
from nltk import FreqDist


# In[124]:


#1.
"""
text5의 FreqDist를 fdist_5 라는 변수로 설정한다.
text5에 있는 단어들을 lower을 이용해 소문자와 해주고 isalpha를 이용해 
문자만을 걸러내여 clean_text5라는 변수에 저장한다.
list comprehension 을 이용하여 text5의 단어들을 순회하여
fdist_5를 이용해 4번 등장하는 단어만을 출력한다.
이때 중복을 제거하기 위해 set으로 바꾸고 sorted 를 이용해 정렬한다.
"""
fdist_5 = FreqDist(text5)
clean_text5 = [word.lower() for word in text5 if word.isalpha()]
print(sorted(set([word for word in clean_text5 if fdist_5[word] == 4])))


# In[125]:


#2-1.
"""
count를 이용해 text4에서 democracy가 몇 번 나오는지 센다.
"""
print(text4.count('democracy'))


# In[126]:


#2-2.
"""
text4와 text3를 각각 FreqDist 한 것을 fdist_4 와 fdist_3 이라는 변수로 설정한다.
이때 첫번째 조건에 따라 text4의 단어들을 순회하면서 text4에서 1번 나타나는 단어들을
fdist_4를 이용해 찾아 first_condition이라는 변수에 저장한다.
첫번째 조건을 만족하는 first condition이라는 리스트안에 있는 단어들을 순회하여
text3에 2번 이상 나타나는 단어들을 fdist_3를 이용해 찾아 출력한다.
"""
fdist_4 = FreqDist(text4)
fdist_3 = FreqDist(text3)
first_condition = [word for word in text4 if fdist_4[word] == 1]
print(len([word for word in first_condition if fdist_3[word] >1]))


# In[101]:


#4.
"""
list comprehension을 이용하여 text4에 있는 단어들을 순회하여
길이가 4인 단어들만 출력한다.
"""
print([word for word in text4 if len(word) == 4] [:100])


# In[105]:


#5.
"""
list comprehension을 이용하여 text7에서 단어들의 길이를 len_word 라는 변수에 저장한다.
len_word라는 변수에 저장된 단어의 길이를 reverse = True을 이용해 내림차순으로 정렬하여 
가장 큰 단어의 길이만을 인덱싱을 이용해 출력한다.
"""
len_word = ([len(word) for word in text7])
sorted(len_word, reverse = True) [0]


# In[106]:


#6.
""" 큰따옴표 3개를 이용하여 긴 문자열을 동일하게 출력한다. """
print(
"""과목명: 고급 파이썬 프로그래밍\Advanced Python programming
    "이 수업은 금요일에 진행됩니다."

수업은 실시간 강의로 진행됩니다.
    - 질의사항은 조교에게 메일로 보내주세요
""")

