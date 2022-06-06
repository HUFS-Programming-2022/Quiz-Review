def gugudan():    
    def bye():
        print("이용해주셔서 감사합니다.") # 구구단 출력 후 프로그램 종료
        nonlocal select_menu
        select_menu = False

    def check_dan():
        ask_number = True
        global confirmed
        while ask_number:
            global dan
            dan = input('값을 입력하세요.:')
            if dan == 'q': # q가 들어왔을 경우 프로그램 종료
                ask_number = False
                confirmed = False
                bye()

            elif dan.isdigit():
                dan = int(dan)
                if dan > 9 or dan < 2:
                    print('입력값은 2와 9 사이의 정수여야 합니다. 다시 확인해주세요.')
                    continue
                else:
                    ask_number = False
                    confirmed = True
            else: # 숫자가 아닌 문자가 들어왔을 경우 되묻기
                print('입력값은 2와 9 사이의 정수여야 합니다. 다시 확인해주세요.')
                continue
                
    def print_gugudan(start_dan, end_dan):
        for i in range(start_dan, end_dan+1):
            print(f"== {i}단 ==")
            for j in range(1,10):
                print(f"{i} X {j} = {i * j} ")
                    
    select_menu = True
    while select_menu:       
        menu = input("""구구단 출력기
    ----------------------------------------------------------------------
               1) n단 출력    2) n단까지 출력   3) n ~ m단 출력   q) 나가기
    ----------------------------------------------------------------------
    메뉴를 선택하세요 > """)
        if menu == 'q':
            bye()
            break
        elif menu == '1':
            print('몇 단을 출력할까요? << q : 나가기 >>')
            check_dan()
            if confirmed:
                start_dan = dan
                end_dan = start_dan
                print_gugudan(start_dan, end_dan)
                    
        elif menu == '2':
            print('2단부터 몇 단까지 출력할까요? << q : 나가기 >>')
            start_dan = 2
            check_dan()
            if confirmed:
                end_dan = dan
                print_gugudan(start_dan, end_dan)
                 
        elif menu == '3':
            print('몇 단부터 출력할까요? << q : 나가기 >>')
            check_dan()
            if confirmed:
                start_dan = dan
                print('몇 단까지 출력할까요? << q : 나가기 >>')
                menu3 = True
                while menu3:
                    check_dan()
                    if confirmed:
                        end_dan = dan
                        if start_dan > end_dan:
                            print('시작 단이 끝 단보다 클 수 없습니다. 다시 입력해주세요.')
                            continue
                        else:
                            print_gugudan(start_dan, end_dan)
                            break
                    else:
                        break
                      
        else:
            print('메뉴 선택은 1, 2, 3, q 중에서만 가능합니다. 다시 확인해주세요.')
            continue

gugudan()
