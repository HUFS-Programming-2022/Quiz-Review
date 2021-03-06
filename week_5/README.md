# Quiz - Week 5.

1. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
 
    산술평균 : N개의 수들의 합을 N으로 나눈 값
    중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
    최빈값 : N개의 수들 중 가장 많이 나타나는 값
    범위 : N개의 수들 중 최댓값과 최솟값의 차이

    N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
 
    - 입력: 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.
 
    - 출력:
        - 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
        - 둘째 줄에는 중앙값을 출력한다.
        - 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 가장 작은 값을 출력한다.
        - 넷째 줄에는 범위를 출력한다. (힌트: 범위 = 최대값-최소값)
 
    - [ 입출력 예시 ]
        입력) 5                 출력) 2
        1                         2
        3                         1
        8                        10
        -2
        2
        
2.  `X = [3, 1, -2, 6, 7]`인 리스트에 대해 `prefix sum S`는 다음과 같이 정의된다.
     `S[i] = X[0] + X[1]+ … +X[i]`
     즉, `S = [3, 4, 2, 8, 15]` 가 된다.
    이중 for 루프를 사용하여 prefixSum 함수를 구현하고 함수의 수행시간을 구하시오.
 
    - [힌트]
    실행시간을 측정하기 위해서는 아래와 같은 함수를 사용한다.
    ```sh
    import time
    time.process_time() # time.process_time()함수는 현재 clock 시간을 알려준다.
    ```
 
    시간 측정 예시)
    함수 f()의 시간을 측정하고 싶을 때,
     ```sh
    import time
    before = time.process_time() #현재 시간을 얻는다
    f() #함수 f 호출
    after = time.process_time() #현재 시간을 얻는다
    print(after-before) #함수 호출 전과 후의 시간 차이
    ```