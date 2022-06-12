#!/usr/bin/env python
# coding: utf-8

# In[27]:


import nltk
#파일 불러오기
with open ('HarryPotter.txt', 'r', encoding = 'UTF-8') as f:
    data = f.read()
    
    
#문장 분절하기
text = ' '.join([word.replace('Mrs.','Mrs').replace('Mr.', 'Mr').replace('...', ' ') 
        for word in data.split(' ')])
text = text.replace('!','. ').replace('?', '. ')
text_sent = [sent for sent in text.split('. ')]


# 단어 분절하기해서 불필요한 요소 없애기
text_word = [word.split() for word in text_sent]
text_word

hypen = '-'
aphostro = "’s"


#문장 내에서 정제된 단어만 출력하기
word_list = []
for word1 in text_word:
    temp = []
    for word in word1:
        if word in punct:
            if hypen in word:
                non_punct = word.split(hypen)
            elif apostro in word:
                non_punct = word.split(aphostro)
        else:
            non_punct = word
        if word and word[0].isalnum():
            temp.append(non_punct)
    word_list.append(temp)
    
print(word_list)


# In[ ]:




