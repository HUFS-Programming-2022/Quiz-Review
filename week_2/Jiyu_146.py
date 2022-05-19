#!/usr/bin/env python
# coding: utf-8

# In[1]:


#0.nltk import 하기
import nltk 
from nltk.book import *
nltk.download('book', quiet = True)


# In[4]:


#1.text에서 4번 출현하는 단어들을 중복되지 않게 오름차순으로 출력
text_5 = sorted(text5)
set([word for word in text_5 if text_5.count(word) == 4 and word.isalpha()])


# In[21]:


#4.NLTK import하고, text4에서 4자리 단어만 출력하세요. 
import nltk 
from nltk.book import *
nltk.download('book', quiet = True)
print([word for word in text4 if len(word) == 4 and word.isalpha()])


# In[25]:


#6. 지문을 똑같이 출력하는 프로그램을 작성하시오. 
print("""과목명: 고급 파이썬 프로그래밍 \Advanced Python programming
    "이 수업은 금요일에 진행됩니다."
    
수업은 실시간 강의로 진행됩니다.
    - 질의사항은 조교에게 메일로 보내주세요.""")


# In[ ]:




