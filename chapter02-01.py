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
line_leng1 = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)
print('EX-1 -', line_leng1)

# 네임드 튜플 선언
from collections import namedtuple
Point = namedtuple('Point', 'x y')

pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

line_leng2 = sqrt((pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2)

# 출력
print('EX1-2 - ', line_leng2)
print('Ex1-3 - ', line_leng1 == line_leng2)


# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
# 중복되는 변수명이나 , 예약어를 사용할 경우 랜덤으로 변수명을 정해준다. rename속성이 변수명 랜덤생성 여부 지정
Point4 = namedtuple('Point', 'x y x class', rename=True) #Default=False

# 출력
print('EX2-1 - ', Point1, Point2, Point3, Point4)

temp_dict = {'x' : 75, 'y' : 55}

# 객체 생성
print(Point2)
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(40, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)

#Dic to Unpacking

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)


print()
print()
print()