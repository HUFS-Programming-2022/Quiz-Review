'''
Quiz01_1.
'''
VIYOTT = (1300 - 480)*3
GIMBAP = ((2500 - 900)*5)*0.85
COKE = ((800 - 380)*6)*0.85
BANANA = (3200-1050)*2
HOMERUNBALL = (1500 - 770)*4

print(int(VIYOTT + GIMBAP + COKE + BANANA + HOMERUNBALL))

'''
Quiz01_3.
'''
HEIGHT = 0
DAYS = 0

while 1 :
    HEIGHT = HEIGHT + 5
    DAYS = DAYS + 1
    
    if HEIGHT >= 350 :
        print (DAYS)
        break
    else :
        HEIGHT = HEIGHT - 2

'''
Quiz01_4.
'''
A = int(input("첫 번째 수를 입력하세요"))
B = int(input("두 번째 수를 입력하세요"))
C = int(input("세 번째 수를 입력하세요"))

if A > B and A > C:
  print(A)
elif B > C: 
  print(B)
else:
  print(C)
