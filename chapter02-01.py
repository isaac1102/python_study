# Chapter02-1
# 파이썬 심화
# 데이터 모델(Data Model)
# 참조 : https://docs.python.org/3/reference/datamodel.html
# NamedTuple 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(sequence), 반복(iterator), 함수(function), 클래스(class)

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value
# 파이썬 -> 일관성

# 일반적인 튜플 사용

pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

# 두 점 사이의 거리
line_leng1 = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)
print('EX-1 -', line_leng1)

# 네임드 튜플 선언
from collections import namedtuple
Point = namedtuple('Point', 'x y')

# 두 점 선언
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

line_leng2 = sqrt((pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2)

# 출력
print('EX1-2 - ', line_leng2)
print('Ex1-3 - ', line_leng1 == line_leng2)


# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])# 객체 이름을 명시적으로 , 명시적으로 리스트를 넣을 수 있다.
Point2 = namedtuple('Point', 'x, y') # comma로 구분 가능
Point3 = namedtuple('Point', 'x y') # 공백으로 구분 가능 
# 중복되는 변수명이나 , 예약어를 사용할 경우 랜덤으로 변수명을 정해준다.
# rename속성이 변수명 랜덤생성 여부 지정
Point4 = namedtuple('Point', 'x y x class', rename=True) #Default=False

# 출력
print('EX2-1 - ', Point1, Point2, Point3, Point4)

#Dic to Unpacking
temp_dict = {'x' : 75, 'y' : 55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict) # 딕셔너리 언패킹 시에는 **를 앞에 붙인다.



print(p1)
print(p2)
print(p3)
print(p4)
print(p5)


print()
print()
print()

# 사용
print('EX3-1 - ' , p1[0] + p2[1]) #Index Error 주의
print('EX3-2 - ' , p1.x + p2.y) #클래스 변수 접근 방식
x, y = p5
print('test : ', x+y )
# Unpacking(한 개로 묶인 것을 여러 값으로 푼다.)
x, y = p3


print('EX3-3 - ', x + y )

# Rename 테스트
print('EX3-4 - ', p4)


# 네임드 튜플 메소드
#리스트 : 데이터를 담는 컨테이너, 시퀀스 제공, 이터레이터를 제공하는 구조
temp = [52, 38] 

# _make() : 새로운 객체 생성 
# 리스트를 네임드 튜플로 변환
p4 = Point1._make(temp)
print('EX4-1 - ', p4)

# _fiedls : : 필드 네임 확인

print('EX4-1 - ', p1._fields, p2._fields, p3._fields)

#_asdict() : OrderedDict 반환(정렬된 딕셔너리로)
print('EX4-3 - ', p1._asdict(), p2._asdict(), p4._asdict())

#_replace() : 수정된, '새로운'객체를 반환  
print('EX4-4 - ', p2._replace(y=100)) #y만 100으로 바꿈

print()
print()

# 실 사용 실습
# 학생 전체 그룹 생성
# 반20명, 4개의 반 ->(A,B,C,D)  번호

# 네임드 튜플 선언(리스트보다 튜플이 빠르다. 불변이므로.)
# 변수명과 똑같이 선언하는 게 관례
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)] #list comprehension
ranks = 'A B C D'.split()
print(ranks, numbers)

# List Comprehension으로 생성     이중반복문의 방식처럼 생성된다.
# List 내부에서 namedtuple을 생성해서 append하는 방식
students = [Classes(rank, number) for rank in ranks for number in numbers] 

print()
print('EX5-1 -', len(students))
print('EX5-2 -', students)

print()
print()

# 가독성은 안좋은 케이스지만 가능은 함
students2 = [Classes(rank, number) 
                    for rank in 'A B C D'.split() 
                        for number in [str(n) for n in range(1,21)]]
print('EX6-1 -', len(students2))
print('EX6-2 -', students2)

# 출력
for s in students:
    print('EX7 -1 -', s)  s