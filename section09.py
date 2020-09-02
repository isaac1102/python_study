# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : r,  쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대 경로, . : 절대 경로
# 기타 : https://docs.python.org/3.7/library/functions.html#open

# 파일 읽기
# 예제1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
# 반드시 close로 리소스 반환해야 한다.
# 커넥션 작업 시 닫지 않으면, 언젠가는 그것에 대한 예외가 발생할 수 있다.
f.close()

print('------------------')
print('------------------')

# 예제2
# with문은 close 생략 가능
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c)) #for문에서 사용 가능한 iter

print('------------------')
print('------------------')

# 예제3
with open('./resource/review.txt', 'r') as f:
    # 한 line 단위로 출력
    for c in f : 
        # 양쪽 공백제거 : strip()
        print(c.strip())
print('------------------')
print('------------------')

# 예제4
with open('./resource/review.txt', 'r') as f:
    # 한번 읽어오면 커서가 끝으로 가므로 다시 읽지 않는다
    content = f.read()
    print(">", content)
    content = f.read() #내용 없음
    print(">", content)

print('------------------')
print('------------------')

# 예제5
with open('./resource/review.txt', 'r') as f:
    # 한 줄 읽음, 커서가 이동하면서 한 줄씩 읽음
    # 반복문을 통해 호출 가능
    # line = f.readline()
    # print(line)

    line = f.readline()
    # line이 비어있으면 False가 되어서 while문 중지
    while line:
        print(line, end=' ####')
        line = f.readline()

# 예제6
with open('./resource/review.txt', 'r') as f:
    # 모든 문장을 엔터를('\n') 기준으로 줄바꿈 형태로 리스트 형태로 가지고 있는다.
    contents = f.readlines()
    print(contents)
    for c in contents :
        print(c, end = ' ******** ')

# 예제7
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)
print('Average : {:6.3}'.format(sum(score)/len(score)))

# 파일 쓰기
# 예제1
with open('./resource/text1.txt', 'w') as f:
    f.write('NiceMane\n')

# 예제2
with open('./resource/text1.txt', 'a') as f:
    f.write('GoodMan!\n')

# 예제3
from random import randint

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')


# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Joe\n']
    f.writelines(list)

# 예제5
with open('./resource/text4.txt', 'w') as f:
    print('Test Coontents1!', file=f)
    print('Test Coontents2!', file=f)


with open('./resource/text4.txt', 'r') as f:
    c = f.read()
    print(c)