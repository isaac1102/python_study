# Section13-1
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random
import time


words = [] # 영어 단어 리스트 1000개
n = 1  # 게임시도 횟수
cor_cnt = 0  # 정답개수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip()) #strip : 양쪽 공백 제거 함수
# print(words) # 단어 리스트 확인

# input : 사용자 입력 함수
input("Ready? Press Enter Key!") #Enter Game Start
start = time.time()

while n <= 5:
    random.shuffle(words) #shuffle에 리스트를 넣으면 알아서 섞어서 랜덤으로 뽑아줌
    q = random.choice(words) # 랜덤으로 하나 뽑아옴

    print() # 줄바꿈
    print("*Question # {}".format(n))
    print(q)

    x = input()

    print()

    if str(q).strip() == str(x).strip():
        print('pass!')
        cor_cnt += 1 
    else:
        print('wrong..')

    n += 1   

end = time.time() #end time
et = end - start # 총 게임 시간
et = format(et, '.3f') # 소수 3째자리까지

if cor_cnt >= 3:
    print('합격')
else:
    print('불합격')

# 수행 시간 출력
print('게임 시간 : ', et, '초', '정답 개수 : {} '.format(cor_cnt))

print()
print('아무키나 누르시면 종료됩니다.')
input()
# 시작 지점 ( 메인에서 실행할 경우에만 실행되도록 )
if __name__ == '__main__' :
    pass