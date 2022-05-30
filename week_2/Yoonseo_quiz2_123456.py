import nltk
from nltk.book import *
nltk.download('book', quiet=True)


#1

from nltk import book
text5 = book.text5.tokens
text5_word = [i.lower() for i in text5 if i.isalpha() and text5.count(i) == 4]
print(sorted(set(text5_word)))



#2-1

text4 = book.text4.tokens
print(f"text4에서 democracy 나오는 횟수:", text4.count('democracy'))

#2-2


text3 = book.text3.tokens
text4_once = [i.lower() for i in text4 if i.isalpha() and text4.count(i) == 1]
text3_word = sorted(set([k.lower() for k in text3 if k in text4_once and text3.count(k) >= 2]))

len(text3_word)

#3

print('text1:', len(set(book.text1.tokens)))
print('text2:', len(set(book.text2.tokens)))
print('text3:', len(set(book.text3.tokens)))
print('text4:', len(set(book.text4.tokens)))
print('text5:', len(set(book.text5.tokens)))
print('text6:', len(set(book.text6.tokens)))
print('text7:', len(set(book.text7.tokens)))
print('text8:', len(set(book.text8.tokens)))
print('text9:', len(set(book.text9.tokens)))
print('중복을 제외하고 가장 많은 종류의 단어가 쓰인 텍스트: text1')


#4
text4_word = sorted(set([i.lower() for i in text4 if i.isalpha() and len(i) == 4]))
print(text4_word)


#5

text7 = book.text7.tokens
print(f'text7에서 가장 긴 단어: {max(text7, key=len)}, {len(max(text7, key=len))}자')
text7 = [i for i in text7 if i.isalpha()]
print(f'text7에서 기호로 이어지지 않은 순수하게 가장 긴 단어: {max(text7, key=len)}, {len(max(text7, key=len))}자')


#6

def announcement():
    '''
    print를 각 문장마다 쓰는 코드
    '''
    print('과목명: 고급 파이썬 프로그래밍\Advanced Python programming')
    print('    "이 수업은 금요일에 진행됩니다."')
    print()
    print('수업은 실시간 강의로 진행됩니다.')
    print('    - 질의사항은 조교에게 메일로 보내주세요')
announcement()

def notice():
    '''
    print 한 번으로 전체 문장을 출력하는 한 줄 코드
    '''
    print('과목명: 고급 파이썬 프로그래밍\Advanced Python programming\n    "이 수업은 금요일에 진행됩니다."\n\n수업은 실시간 강의로 진행됩니다.\n    - 질의사항은 조교에게 메일로 보내주세요')
notice()
