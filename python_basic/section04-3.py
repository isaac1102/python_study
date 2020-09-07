# Section04-3
# 파이썬 데이터 타입(자료형)
#  List, Tuple

# List - 순서o, 중복o, 수정o, 삭제o

a = []
b = list()
c = [1,2,3,4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])


# 슬라이싱
print(d[0:3])
print(e[2][1:3])


# 연산
print(c + d) 
print(c*3)
# print(c[0]+'hi')  #에러 : 정수와 스트링의 합은 불가
print(str(c[0]) + 'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)
c[1:2] = [10, 100, 1000]
print(c)

c[1] = ['a', 'b', 'c']
print(c)

del c[0]
print(c)

print()
print()
print()
print()
print()
print()

y = [5,2,4,1,3]
y.append(7)
print(y)
y.sort()
print(y)
y.reverse()
print(y)

y.insert(1,10)
print(y)

y.remove(2)
print(y)

y.pop()
print(y) # LIFO

ex = [88,77]
y.append(ex)
print(y)
y.extend(ex)
print(y)


# 삭제 : remove, del, pop

# 튜플 : 순서o, 중복o, 수정x,  삭제x
# 프로그램에 영향을 중요한 값들 (계좌번호같은..)에 사용함

a = ()  
b = (1,)
c = (1,2,3,4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(d[2][0:len(d[2])])

print(d[2:])
print(d[2][0:2])
print(c+d)
print(c*3)


print()
print()
print()
print()
print()

# 튜플함수
z = (5,1,2,3,1)
print(z)
print(3 in z)
print(z.index(5))
print(z.count(1))

