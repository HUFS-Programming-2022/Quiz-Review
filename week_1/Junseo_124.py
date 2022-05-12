
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "37d8e090-08ca-439f-99e2-4e67795c7204",
   "metadata": {},
   "source": [
    "### 1. 편의점 매출 계산하기\n",
    "- 총 매출 = (소비자 가격 - 원가) * 개수\n",
    "- 조건: 5개 이상 구매 시 전체 물품의 15% 할인\n",
    "\n",
    "한 고객이 다음과 같이 물건을 구입했다고 할 때, 편의점의 매출을 계산하시오. - 최대한 모든 리터럴을 변수에 담을 것 - 출력값은 총 매출액 (int)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1cbf10da",
   "metadata": {},
   "source": [
    "### 2. 흙을 나르는 마이클\n",
    "- 옮겨야 할 흙은 총 n킬로그램이고, 마이클은 3kg씩 혹은 5kg씩 나를 수 있다. 최대한 적은 노력으로 모든 흙을 나를 수 있는 코드를 작성하라. 단, 나르는 흙의 양을 넘기지 않는다.\n",
    "\n",
    "- 예: n = 18일 때, 3kg 6번보다 5kg 3번 + 3kg 1번이 (=4번) 더 나은 방법이다.\n",
    "- 예: n = 19일 때, 3kg을 1번 더 옮겨야 함.\n",
    "- n은 랜덤으로 주어진다\n",
    "\n",
    "- import random\n",
    "- n = random.randint(10, 100)\n",
    "- 출력값 = (3kg 횟수, 5kg 횟수)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "546dc489",
   "metadata": {},
   "source": [
    "### 4. 큰 수 찾기\n",
    "세 수를 입력받고 가장 큰 수를 찾는 코드를 작성하세요. (max 함수 이용하지 말 것)\n",
    "\n",
    "예: 12, 14, 15 입력 받았다면 15"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e143f48c-6764-4326-9335-1381436f64bd",
   "metadata": {},
   "source": [
    "#1\n",
    "물건: 비요뜨 삼각김밥 콜라 바나나 홈런볼\n",
    "소비: 1300   2500    800  3200   1500\n",
    "원가: 480    900     380  1050   770\n",
    "개수: 3       5       6     2      4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "cbf52135",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "18622"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#1\n",
    "bi_customer = 1300\n",
    "bi_origin = 480\n",
    "bi_quantity = 3\n",
    "\n",
    "tri_customer = 2500\n",
    "tri_origin = 900\n",
    "tri_quantity = 5\n",
    "\n",
    "coke_customer = 800\n",
    "coke_origin = 380\n",
    "coke_quantity = 6\n",
    "\n",
    "ban_customer = 3200\n",
    "ban_origin = 1050\n",
    "ban_quantity = 2\n",
    "\n",
    "home_customer = 1500\n",
    "home_origin = 770\n",
    "home_quantity = 4\n",
    "\n",
    "bi_total = (bi_customer - bi_origin) * bi_quantity\n",
    "tri_total = (tri_customer - tri_origin) * 0.85 * tri_quantity\n",
    "coke_total = (coke_customer - coke_origin) * 0.85 * coke_quantity\n",
    "ban_total = (ban_customer - ban_origin) * ban_quantity\n",
    "home_total = (home_customer - home_origin) * home_quantity\n",
    "\n",
    "Total = bi_total + tri_total + coke_total + ban_total + home_total\n",
    "int(Total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "44c54945-4629-4529-8fa3-7d4182a175dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "총 옮겨야 할 흙은 59kg 입니다.\n",
      "5kg은 11번, 3kg은 1번 옮겨야 합니다.\n"
     ]
    }
   ],
   "source": [
    "#2\n",
    "import random\n",
    "n = random.randint(10,100)\n",
    "\n",
    "\n",
    "move_five = n // 5 #5kg를 나르는 횟수\n",
    "move_three = int((n % 5) / 3) # 3kg를 나르는 횟수 \n",
    "\n",
    "times_five, times_three = move_five, move_three\n",
    "\n",
    "print(f'총 옮겨야 할 흙은 {n}kg 입니다.')\n",
    "print(f'5kg은 {times_five}번, 3kg은 {times_three}번 옮겨야 합니다.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b8b64bf5-cba0-473e-bcd7-a400ebf87515",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "숫자를 입력하세요:  11\n",
      "숫자를 입력하세요:  24\n",
      "숫자를 입력하세요:  35\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "제일 큰 숫자는 24입니다. \n"
     ]
    }
   ],
   "source": [
    "#3\n",
    "num1 = int(input('숫자를 입력하세요: '))\n",
    "num2 = int(input('숫자를 입력하세요: '))\n",
    "num3 = int(input('숫자를 입력하세요: '))\n",
    "\n",
    "max_num = num1 \n",
    "\n",
    "if num2 > max_num:\n",
    "    max_num = num2\n",
    "elif num3 > max_num:\n",
    "    max_num = num3\n",
    "\n",
    "print(f'제일 큰 숫자는 {max_num}입니다. ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c98d590b-f3f1-43f1-b2f7-86f2d3fbc77f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
