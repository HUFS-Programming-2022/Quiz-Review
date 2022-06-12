#!/usr/bin/env python
# coding: utf-8

# In[101]:


menu_announce = """
구구단 출력기
-----------------------------------------------------------
    1) n단 출력    2)n단까지 출력    3) n~m단 출력    q)나가기
-----------------------------------------------------------
메뉴를 선택하세요 >>>"""

error_announce = """
입력값을 확인한 후, 다시 입력해주세요
( n <= m, 0 < n <10, 0 < m <10 )"""

quit_announce = '이용해주셔서 감사합니다.'

menu_choices = ['1', '2', '3', 'q']

number_choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


# In[102]:


operation = True
while operation == True:
    menu = input(menu_announce)
    if menu not in menu_choices:
        print(error_announce)
    else:
        operation2 = True
        while operation2 == True:
            if menu == '1':
                n = input('몇단을 출력하시겠습니까?')
                m = n
                if (n in number_choices) and (m in number_choices):
                    operation2 = False
                elif n == 'q' or m == 'q':
                    print(quit_announce)
                    operation2 = False
                    operation = False
                    break
                else:
                    print()
                    
            elif menu == '2':
                m = input ('몇단까지 출력하시겠습니까?')
                n = '1'
                if (n in number_choices) and (m in number_choices):
                    operation2 = False
                elif n == 'q' or m == 'q':
                    print(quit_announce)
                    operation2 = False
                    operation = False
                    break
                else:
                    print()
                    
            elif menu == '3':
                n = input('몇단부터 출력하시겠습니까?')
                m = input('몇단까지 출력하시겠습니까?')
                if (n in number_choices) and (m in number_choices):
                    operation2 = False
                elif n == 'q' or m == 'q':
                    print(quit_announce)
                    operation2 = False
                    operation = False
                    break
                else:
                    print()
                    
            else:
                print(quit_announce)
                operation2 = False
                operation = False
                break

            if (n in number_choices) and (m in number_choices):
                n = int(n)
                m = int(m)
                if n <= m:
                    for i in range(n, m+1):
                        print(f'===={i}단====')
                        for j in range(1, 10):
                            print(f'{i}X{j} = {i*j}')   
            else:
                print(error_announce)


# In[106]:



def gugudan():
    operation = True
    while operation == True:
        menu = input(menu_announce)
        if menu not in menu_choices:
            print(error_announce)
        else:
            operation2 = True
            while operation2 == True:
                if menu == '1':
                    n = input('몇단을 출력하시겠습니까?')
                    m = n
                    if (n in number_choices) and (m in number_choices):
                        operation2 = False
                    elif n == 'q' or m == 'q':
                        print(quit_announce)
                        operation2 = False
                        operation = False
                        break
                    else:
                        print()

                elif menu == '2':
                    m = input ('몇단까지 출력하시겠습니까?')
                    n = '1'
                    if (n in number_choices) and (m in number_choices):
                        operation2 = False
                    elif n == 'q' or m == 'q':
                        print(quit_announce)
                        operation2 = False
                        operation = False
                        break
                    else:
                        print()

                elif menu == '3':
                    n = input('몇단부터 출력하시겠습니까?')
                    m = input('몇단까지 출력하시겠습니까?')
                    if (n in number_choices) and (m in number_choices):
                        operation2 = False
                    elif n == 'q' or m == 'q':
                        print(quit_announce)
                        operation2 = False
                        operation = False
                        break
                    else:
                        print()

                else:
                    print(quit_announce)
                    operation2 = False
                    operation = False
                    break

                if (n in number_choices) and (m in number_choices):
                    n = int(n)
                    m = int(m)
                    if n <= m:
                        for i in range(n, m+1):
                            print(f'===={i}단====')
                            for j in range(1, 10):
                                print(f'{i}X{j} = {i*j}')   
                else:
                    print(error_announce)
gugudan()


# In[ ]:




