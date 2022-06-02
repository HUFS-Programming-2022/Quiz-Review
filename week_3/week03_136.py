#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 
import nltk
from nltk.book import *


# In[2]:


[word for word in text6 if 'pt' in word]


# In[7]:


#3


# In[9]:


a = int(input("팩토리얼을 입럭하세요: "))
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
        
print(f'0의 개수는 {zero}개 입니다.')


# In[3]:


#6


# In[6]:


star = int(input('숫자를 입력하세요: '))
for i in range(n,0,-1): 
    print(" "*(star-i)+"*"*(i*2-1))


# In[ ]:





# In[ ]:




