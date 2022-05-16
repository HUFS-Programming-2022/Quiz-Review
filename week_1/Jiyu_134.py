#!/usr/bin/env python
# coding: utf-8

# In[9]:


# 편의점 매출 문제
sale = 0.85
biyot_price = 480
biyot_consumerPrice = 1300
biyot_count = 3
biyot_profit = (biyot_consumerPrice - biyot_price) * biyot_count

kimbob_price= 900
kimbob_consumerPrice = 2500
kimbob_count = 5
kimbob_profit = (kimbob_consumerPrice - kimbob_price) * kimbob_count * sale

coke_price = 380
coke_consumerPrice = 800
coke_count = 6
coke_profit = (coke_consumerPrice - coke_price) * coke_count * sale

banana_price = 1050
banana_consumerPrice = 3200
banana_count = 2
banana_profit = (banana_consumerPrice - banana_price) * banana_count

homerun_price = 770
homerun_consumerPrice = 1500
homerun_count = 4
homerun_profit = (homerun_consumerPrice - homerun_price) * homerun_count

profit = biyot_profit + kimbob_profit + coke_profit + banana_profit + homerun_profit

print('총 매출액입니다.')
print(int(profit))


# In[8]:


#달팽이 
height = 350
snail_up = 5
snail_down = 2
snailMove = snail_up - snail_down

day = height / snailMove

print(f'{int(day)}일이 걸립니다. ')


# In[3]:


#큰 수 찾기 
firstNum = int(input('첫 번째 값을 입력하세요:'))
secondNum = int(input('두 번째 값을 입력하세요:'))
thirdNum = int(input('세 번째 값을 입력하세요:'))


if firstNum < secondNum:
    maxNum = secondNum
    if maxNum > thirdNum:
        maxNum = maxNum
    else:
        maxNum = thirdNum
else:
    maxNum = firstNum
    if maxNum > thirdNum:
        maxNum = maxNum
    else:
        maxNum = thirdNum
    

print(f'최댓값은 {maxNum}입니다.')

