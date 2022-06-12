#!/usr/bin/env python
# coding: utf-8

# In[41]:


#import 하기
import os
import string
import nltk
import matplotlib.pyplot as plt


# In[124]:


#파일 불러오기
with open ('HarryPotter.txt', 'r', encoding = 'UTF-8') as f:
    data = f.read()
    
    
#문장 분절하기
text = ' '.join([word.replace('Mrs.','Mrs').replace('Mr.', 'Mr').replace('...', ' ') 
        for word in data.split(' ')])
text = text.replace('!','. ').replace('?', '. ')
text_sent = [sent for sent in text.split('. ')]


# 단어 분절하기
text_word = [word.split() for word in text_sent]
text_word


# 불필요한 토큰 제거
punct = list(string.punctuation)
my_punct = set([word[0]
                for sent in text_word for word in sent
               if (not word[0].isalnum()) and (word not in punct)])
punct.extend(my_punct)

hypen = '-'
apostro = "’s"

word_list = []
for word1 in text_word:
    temp = []
    for word in word1:
        if word in punct:
            if hypen in word:
                non_punct = word.split(hypen)
            elif apostro in word:
                non_punct = word.split(apostro)
        else:
            non_punct = word
        if word and word[0].isalnum():
            temp.append(non_punct)
    word_list.append(temp)



#불용어 제거
stopwords = nltk.corpus.stopwords.words('english')
refine_words = [[word for word in text
               if word.lower() not in stopwords]
               for text in text_word]



#uncasing 하기
uncasing_tokens = [word.lower() for sent in refine_words for word in sent]




#상위 50단어 출력
fdist = nltk.FreqDist(uncasing_tokens)
top_50 = {key:value for key, value in fdist.most_common(50)}
plt.plot(top_50.keys(),top_50.values())




#uncasing 단어 개수
print(len(uncasing_tokens))


# In[ ]:




