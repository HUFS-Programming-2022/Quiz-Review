"""
 1. 편의점 매출 계산하기
- 총 매출 = (소비자 가격 - 원가) * 개수
- 조건: 5개 이상 구매 시 전체 물품의 15% 할인
한 고객이 다음과 같이 물건을 구입했다고 할 때, 편의점의 매출을 계산하시오. - 최대한 모든 리터럴을 변수에 담을 것 - 출력값은 총 매출액 (int)

        원가  소비자가  개수
비요뜨  480     1300    3  
삼각김밥 900    2500    5
콜라    380     800     6
바나나  1050    3200    2
홈런볼  770     1500    4
""" 

viyott_num = 3
kimbap_num = 5
coke_num = 6
banana_num = 2
homerun_num = 4

total_num = viyott_num+kimbap_num+coke_num+banana_num+homerun_num

viyott_sales = (1300-480)*viyott_num
kimbap_sales = (2500-900)*kimbap_num
coke_sales = (800-380)*coke_num
banana_sales = (3200-1050)*banana_num
homerun_sales = (1500-770)*homerun_num

total_sales = viyott_sales+kimbap_sales+coke_sales+banana_sales+homerun_sales

if total_num>5:
        print(f'편의점의 총 매출은 {int(total_sales-(total_sales*0.15))}원입니다.')
else :
        print(f'편의점의 총 매출은 {int(total_sales)}원입니다.')

# 혹은 

viyott = (1300-480)*3
kimbap = (2500-900)*5
coke = (800-380)*6
banana = (3200-1050)*2
homerun = (1500-770)*4
all_sales = viyott + kimbap + coke + banana + homerun

if total_num>5:
        print(f'편의점의 총 매출은 {int(all_sales - (all_sales*0.15))}원입니다.')
else:
        print(f'편의점의 총 매출은 {int(all_sales)}원입니다.')

"""
3. 달팽이
달팽이가 높이 350미터인 나무 막대를 올라간다.

달팽이는 낮에 5미터 올라간다.
밤에는 2미터 미끄러진다.
정상에 올라간 후에는 미끄러지지 않는다.
달팽이가 막대기 정상에 올라가려면 며칠이 걸리는지 코드를 짜서 프린트하시오.
"""

snail = 3
stick = 350

if (stick-5)%snail == 0 :
    print(f'걸린 일수는 {stick//snail}일이다.')
elif (stick-5)%snail == 1 :
    print(f'걸린 일수는 {stick//snail+1}일이다.')
else : 
    print(f'걸린 일수는 {stick//snail+1}일이다.')

"""
4. 큰 수 찾기
세 수를 입력받고 가장 큰 수를 찾는 코드를 작성하세요. (max 함수 이용하지 말 것)

예: 12, 14, 15 입력 받았다면 15
"""

first = int(input('첫 번째 숫자를 입력하세요 : '))
second = int(input('두 번째 숫자를 입력하세요 : '))
third = int(input('세 번째 숫자를 입력하세요 : '))

if first>second:
        large_num = first
else:
        large_num = second
if large_num<third:
        large_num = third

print(f'입력 받은 세 수 중 가장 큰 수는 {large_num}입니다.')
