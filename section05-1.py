# Section05-1
# 파이썬 흐름제어(제어문)
# 조건문 실습


print(type(True))
print(type(False))

# 기본 형식

# 예1
if True:
    print("Yes")  # 들여쓰기 중요

if False:
    # 출력되지 않음.
    print("No")

# 예2
if False:
    # 여기는 실행되지 않음.
    print("You can't reach here")
else:
    # 여기가 실행된다.
    print("Oh, you are here")

# 관계연산자
# >, >=, <, <=, ==, !=


a = 10
b = 0

# == 양 변이 같을 때 참.
print(a == b)

# != 양 변이 다를 때 참.
print(a != b)

# > 왼쪽이 클때 참.
print(a > b)

# >= 왼쪽이 크거나 같을 때 참.
print(a >= b)

# < 오른쪽이 클 때 참.
print(a < b)

# <= 오른쪽이 크거나 같을 때 참.
print(a <= b)

# 참 거짓 종류
# 참 : "내용", [내용], (내용), {내용}, 1
# 거짓 : "", [], (), {}, 0, None

city = ""
if city:
    print("You are in:", city)
else:
    # 이쪽이 출력된다.
    print("Please enter your city")

city = "Seoul"
if city:
    print("You are in:", city)
else:
    # 이쪽이 출력된다.
    print("Please enter your city")

# 논리연산자
# and, or, not

a = 100
b = 60
c = 15

print('and : ', a > b and b > c)  # a > b > c
print('or : ', a > b or b > c)
print('not : ', not a > b)
print('not : ', not b > c)
print(not True)
print(not False)

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리 순서로 적용
# 1 튜플, 리스트, 딕셔너리, 세트 생성
# 2 리스트(튜플) 첨자, 슬라이싱, 함수 호출, 속성 참조
# 3 await 표현식
# 4 거듭제곱(**)
# 5 +x, -x, ~x 단항 덧셈(양의 부호), 단항 뺄셈(음의 부호), 비트 NOT
# 6 *, @, /, //, % 곱셈, 행렬 곱셈, 나눗셈, 버림 나눗셈, 나머지
# 7 +, - 덧셈, 뺄셈
# 8 <<, >> 비트 시프트
# 9 & 비트 AND
# 10 ^ 비트 XOR
# 11 | 비트 OR
# 12 in, not in, is, is not, <, <=, >, >=, !=, == 포함 연산자, 객체 비교 연산자, 비교 연산자
# 13 not x 논리 NOT
# 14 and 논리 AND
# 15 or 논리 OR
# 16 if else 조건부 표현식
# 17 lambda 람다 표현식

print('ex1 : ', 3 + 12 > 7 + 3)
print('ex2 : ', 5 + 10 * 3 > 7 + 3 * 20)
print('ex3 : ', 5 + 10 > 3 and 7 + 3 == 10)
print('ex4 : ', 5 + 10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print('합격하셨습니다')
else:
    print("죄송합니다. 불합격입니다.")

# 다중조건문
num = 50
if num >= 90:
    print("등급 A", num)
elif num >= 80:
    print('등급 B', num)
elif num >= 70:
    print('등급 C', num)    
else:
    print("꽝")

# 중첩조건문
age = 17
height = 175
if age >= 20:
    if height >= 170:
        print('A지만 지원 가능')
    elif height >= 160:
        print('B지만 지원 가능')
    else:
        print("지원 불가")
else:
    print("20세 이상만 지원 가능")