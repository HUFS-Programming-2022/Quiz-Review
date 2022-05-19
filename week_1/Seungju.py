#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. 편의점 매출 계산하기

# 매출을 구하는 함수 작성
def sales(cost, price, count):
    """ 편의점 매출을 계산해주는 프로그램. """
    
    if count >= 5: # 5개 이상 구매하는 제품은 15% 할인 적용
        sales = int(((price - cost) * count) * 0.85)
    else:
        sales = int(((price - cost) * count))
        
    return sales

# 각 변수마다 sales 함수를 이용하여 매출 구하기
yogurt = sales(480, 1300, 3)
triangle_gimbap = sales(900, 2500, 5)
coke = sales(380, 800, 6)
banana = sales(1050, 3200, 2)
homerunball = sales(770, 1500, 4)

# 총 매출액 출력하기
total_sales = print(f'매출은 총 {yogurt + triangle_gimbap + coke + banana + homerunball}원 입니다.')


# In[5]:


#2. 흙을 나르는 마이클

import random
n = random.randint(10,100)
""" 최대한 적은 노력으로 모든 흙을 나를 수 있게 하는 프로그램 """

moving_5kg = n // 5 #5kg 옮기는 횟수 = n을 5로 나눈 몫
moving_3kg = int((n % 5) / 3) #3kg 옮기는 횟수 = n을 5로 나눈 나머지를 3으로 나눈 것
# 이때 총량을 넘으면 안되므로 소수점을 버리기 위해 int 사용
result = (moving_3kg, moving_5kg)

print(f'옮겨야 할 흙은 {n}kg 입니다.')
print(f'(3kg 나르는 횟수, 5kg 나르는 횟수) = {result}')


# In[3]:


#3. 달팽이

def climb_tree(height, day_moving, night_slipping):
    """ 달팽이가 막대기 정상에 올라가려면 며칠이 걸리는지 알려주는 함수 """
    
    climb_tree = (height / (day_moving + night_slipping))
    
    if climb_tree > int(climb_tree):
        climb_tree = int(climb_tree) + 1 # 소수로 나오면 1일 더해주기
    else:
        climb_tree = int(climb_tree) # 정수로 나오면 그대로
    
    return climb_tree

total = climb_tree(350, 5, -2) # 함수 이용해서 며칠 걸리는지 계산

# 총 며칠 걸리는지 출력    
print('달팽이가 350m 정상에 올라가려면 며칠이 걸리나요?')
print(f'{total}일이 걸립니다.')


# In[4]:


#4. 큰 수 찾기

print('숫자 3개를 입력하시면 가장 큰 수를 알려드립니다.')
""" 세 수 중에 가장 큰 수를 찾아주는 프로그램 """

# 먼저 숫자 int 형태로 3개 입력받기
first_num = int(input ('첫 번째 숫자를 입력하세요: '))
second_num = int(input ('두 번째 숫자를 입력하세요: '))
third_num = int(input ('세 번째 숫자를 입력하세요: '))

# if문을 이용하여 3가지 경우로 가장 큰 수 찾기
if first_num > (second_num and third_num) :
    print(f'가장 큰 수는 {first_num}입니다.')
elif second_num > (first_num and third_num) :
    print(f'가장 큰 수는 {second_num}입니다.')
else :
    print(f'가장 큰 수는 {third_num}입니다.')

