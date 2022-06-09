#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. CFD를 이용하여 nltk.book의 텍스트별 빈도수를 만들고, wh-words 빈도수 출력


# In[15]:


import nltk 
from nltk.book import * 
nltk.download('book', quiet = True)
from nltk import FreqDist

text_list = [getattr(nltk.book, f'text{i}') for i in range(1, 10)]
cfd = nltk.ConditionalFreqDist(
(text, word.lower())for text in text_list for word in text)

for text in text_list:
    print(text)
    for wh_words in ['what', 'why', 'when', 'where', 'which']:
        print(f'{wh_words}:{cfd[text][wh_words]}개')
    print('================================')


# In[2]:


#2. gutenberg에서 모음으로 시작하는 파일 + 단어(숫자, 문장부호 제거) + 하나의 스트링으로 출력


# In[23]:


import nltk 
from nltk.corpus import gutenberg
nltk.download('gutenberg', quiet = True)

vowel = ['a','e','i','o','u']

for file in gutenberg.fileids():
    if file[0] in vowel: 
        word = [word for word in gutenberg.words(file) if word.isalpha()]
        print_string = ' '.join(word)
print(print_string)


# In[3]:


#3. 브라운에서 각 장르별 hapax의 개수를 cfd를 이용하여 구하기


# In[29]:


import nltk
nltk.download('brown')
brown = nltk.corpus.brown
cfd = nltk.ConditionalFreqDist(
    (genre, word)

for genre in brown.categories()
for word in brown.words(categories = genre))

for genre in brown.categories():
    print(genre, len(cfd[genre].hapaxes()))


# In[ ]:




