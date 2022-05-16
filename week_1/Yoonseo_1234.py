# 1. 편의점 매출 계산하기


#total = (retail_price - prime_cost)*5

# 비요뜨 매출
viyott = (1300 - 480) * 3

# 삼각김밥 매출(15% 할인)
gimbap = ((2500 - 900) * 5) * 0.85

# 콜라 매출(15% 할인)
coke = ((800 - 380) * 6) * 0.85

# 바나나 매출
banana = (3200 - 1050) * 2

# 홈런볼 매출
homerunball = (1500 - 770) *4

total = int(viyott + gimbap + coke + banana + homerunball)
print(total)





#2. 흙을 나르는 마이클


import random
n = random.randint(10, 100)
print('n은 랜덤으로 주어진다. :', n)

five = n // 5
three = (n % 5)//3

if ((5 * five) + (3 * three)) != n:
    cycle = True
    i = 0
    if n % 5 != 0 and n % 5 < 3:
        five -= 1
        three += 2        
    while cycle:
        if ((5 * five) + (3 * three)) == n:
            break
            
        elif ((5 * five) + (3 * three)) != n:
            i += 1
            five -= 1
            three = three + i + 1
            
print(f'(3kg = {three}번, 5kg = {five}번)')






# 3. 달팽이


height = 350
snail = 0
day = 0
while snail < height:
    day += 1
    snail += 5
    if snail < height:
        snail -= 2
        continue
    if snail >= height:
        break
print(f'{day}일')







# 4. 큰 수 찾기


num1 = int(input('첫번째 수 : '))
num2 = int(input('두번째 수 : '))
num3 = int(input('세번째 수 : '))

if num1 < num3 and num2 < num3:
    print('가장 큰 수 : ', num3)
elif num3 < num2 and num1 < num2:
    print('가장 큰 수 : ', num2)
elif num2 < num1 and num3 < num1:
    print('가장 큰 수 : ', num1)
