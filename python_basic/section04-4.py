# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합

# 딕셔너리 : 순서x, 중복x, 수정o, 삭제o

# key, value(json) -> MongoDB
# 선언

a = {'name' : 'Jeong', 'phone' : '010-2102-4401', 'birth' : 870730}
b = { 0 : 'Hello Python', 1 : 'Hello Coding' }
c = {'arr' : [1,2,3,4,5]}

print(type(a))
# 출력
print(a['name'])
print(a.get('phone'))
print(a.get('addr'))  # 없으면 안 가져온다. 에러 안남.

print(c.get('arr')[1:2])

# 딕셔너리 추가
a['address'] = 'seoul'
print(a)

a['rank'] = [1,2,3]
a['rank2'] = (4,5,6,)
print(a)


# keys, values, items
print(a.keys()) #아직은 리스트가 아니다. 
print(list(a.keys())[0]) #list함수를 통해서 인덱싱이 된다.

temp = list(a.keys())
print(temp[0:3])

print(a.values)

print()
print()
print()
print()
print()

print(a.values())
print(list(a.values()))
print(a.items())

print( 0  in b)
print('name' in a)
print('name' not in a)


# 집합(Sets) : 순서X, 중복X

a = set()
b = set([1,2,3,4])
c = set([1,4,5,6,6])

print(type(a))
print(c)

t = tuple(b)
print(t)

l = list(b)
print(b)

print()
print()
print()

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합 출력
print(s1.intersection(s2))
print(s1 & s2)

# 합집합 출력(중복원소는 제거됨)
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))

# 추가 제거 가능
s3 = set([7,8,10, 15])
s3.add(18)
print(s3)
# 중복은 반영안됨
s3.add(7)
print(s3)

# 삭제
s3.remove(15)
print(s3)

print(type(s3))