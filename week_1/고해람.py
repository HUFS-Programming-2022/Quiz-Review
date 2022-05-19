#!/usr/bin/env python
# coding: utf-8

# # Quiz review week 1 

# ### 1. 편의점 매출 계산하기

# In[1]:


byotte = (1300 - 480) * 3
kimbap = ((2500 - 900) * 5) * 0.15
coke = ((800 - 380) * 6) * 0.15
banana = (3200 - 1050) * 2
homerunball = (1500 - 770) * 4

total = int(byotte + coke + banana + homerunball)

print(f"편의점의 총 매출은 {total}원 입니다.") 


# ### 3. 달팽이

# In[ ]:


# 변수 선언
top = 350 
day = 0
move = 0

# 무한 루프
while 1:
    move += 3
    day += 1
    
    if move >= top:
        print(day)
        break
    else:
        move += 3


# ### 4. 큰 수 찾기

# In[ ]:


#숫자 입력 받기
num1 = int(input("숫자를 입력하세요:"))
num2 = int(input("숫자를 입력하세요:"))
num3 = int(input("숫자를 입력하세요:"))

#조건문으로 입력받은 수의 크기 비교하기
if num1 > num2 and num1 > num3 :
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
elif num3 > num1 and num3 > num2:
    print(num3)
else:
    print("숫자를 잘못 입력하셨습니다.")

