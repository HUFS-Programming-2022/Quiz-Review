#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk 
from nltk.book import *
nltk.download('book', quiet = True)


# In[3]:


#1. pt를 포함한 단어 출력하기
pt_word = [word for word in text6 if word.isalpha() and 'pt' in word.lower()]
print(pt_word)


# In[5]:


#3. 팩토리얼 0의 개수 구하기

result = 1
n = int(input('숫자를 입력하세요:'))
for i in range(1, n+1):
    result *= i
    ogresult = result
    
count = 0
while result %10 ==0:
    result /= 10
    count += 1 
    
print(count)


# In[20]:


#6.별찍기 
n = int(input('숫자를 입력하세요:'))
index = 1 
blank = 0 
for i in range(n):
    print(' '*blank,end = ' ') 
    print('*'*(2*n - index), end = ' ') 
    print(' ') 
    index += 2
    blank += 1


# In[ ]:




