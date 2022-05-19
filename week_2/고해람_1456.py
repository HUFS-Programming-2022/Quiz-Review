#!/usr/bin/env python
# coding: utf-8

# ### 1.  text5에서 4번 출현하는 단어들을 중복되지 않게 오름차순으로 출력하기

# In[1]:


#nltk 설치
get_ipython().system(' pip install nltk')


# In[3]:


#nltk로 book 가져오기
import nltk
from nltk.book import *
nltk.download('book', quiet=True)


# In[ ]:


#리스트 컴프리헨션으로 중복 제거하고 단어가 알파벳으로 이뤄진 경우만 센다
moby = book.text5
moby_tokens=sorted(moby.tokens)
set([word for word in moby_tokens if moby_tokens.count(word) == 4 and word.isalpha])


# ### 4. nltk 임포트하고, text4에서 4자리 단어만 출력하기

# In[9]:


#nltk에서 book을 import한다
import nltk
from nltk.book import *
nltk.download('book', quiet=True)


# In[44]:



print([word for word in text4 if len(word)==4])


# In[34]:


#중복 없애기 + 오름차순 정렬하기
print(sorted(set([word for word in text4 if len(word)==4])))


# ### 5. text7에서 가장 긴 단어는 몇 자인가

# In[47]:


#nltk 임포트하기
import nltk
from nltk.book import *
nltk.download('book', quiet=True)


# In[64]:


#단어의 길이 출력하기
[len(word) for word in text7]


# In[65]:


#단어의 길이를 내림차순으로 정렬하여 첫번째 값 출력하기
sorted([len(word) for word in text7], reverse=True)[0]


# ### 6. 문장 출력하기

# In[73]:


#이스케이프 문자 활용하기
notice = "과목명: 고급 파이썬 프로그래밍\\Advanced Python programming\n\t\'이 수업은 금요일에 진행됩니다.\'\n\n수업은 실시간 강의로 진행됩니다.\n\t- 질의사항은 조교에게 메일로 보내주세요"

print(notice)

