# Secion02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this
import sys

# 파이썬 기본 인코딩(기본적으로 UTF-8)
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print("My name is Euijin")

# 변수선언
myName = 'GoodBoy'

# 파이썬은 indent가 곧 문법이다

# 조건문
if myName == 'GoodBoy':
    print('OK')

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i, j), i*j )

# 변수 선언(한글 가능, 다만 하지않는 것을 추천)
이름 = "좋은 사람"
print(이름)

# 함수 선언
def 인사():
    print('안녕하세요. 반갑습니다.')
인사()

def greeting():
    print('hello nice to meet you')
greeting()

# 클래스
class Cookie:
    pass

# 객체생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))

# 파이썬 가상환경 생성
# python -m venv 폴더명
# script 폴더로 이동 후 
# 활성화 activate.bat 
# 비활성화 deactivate.bat
