# Chapter03-1
# 파이썬 심화
# 시퀀스형 
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque], Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque) vs 불변(tuple, str, bytes)
# 리스트 및 튜플 심화

# 지능형 리스트(Comprehending Lists)

# Non Comprehending Lists
chars = '!@#$%^&*()_+'
codes1 = []

for s in chars:
    # 유니코드 리스트
    codes1.append(ord(s))

# Comprehending Lists
codes2 = [ord(s) for s in chars]

# Comprehending Lists + Map, Filter
# 속도 약간 우세

# ord(c)
# 하나의 유니코드 문자를 나타내는 문자열이 주어지면 해당 문자의 유니코드 코드 포인트를 나타내는 정수를 돌려줍니다. 
# 예를 들어, ord('a') 는 정수 97 을 반환하고 ord('€') (유로 기호)는 8364 를 반환합니다. 이것은 chr() 의 반대입니다.
codes3 = [ord(s) for s in chars if ord(s) > 40]
codes4 = list(filter(lambda x : x > 40, map(ord, chars)))

# 전체 출력
print('EX1-1 -', codes1)
print('EX1-2 -', codes2)
print('EX1-3 -', codes3)
print('EX1-4 -', codes4)

# chr(i) : 유니코드 코드 포인트가 정수 i 인 문자를 나타내는 문자열을 돌려줍니다. 
# 예를 들어, chr(97) 은 문자열 'a' 를 돌려주고, chr(8364) 는 문자열 '€' 를 돌려줍니다. 이 것은 ord() 의 반대입니다.
# 인자의 유효 범위는 0에서 1,114,111(16진수로 0x10FFFF)까지입니다. i 가 이 범위 밖에 있을 때 ValueError 가 발생합니다.
print('EX1-5 - ',  [chr(s) for s in codes1])
print('EX1-6 - ',  [chr(s) for s in codes2])
print('EX1-7 - ',  [chr(s) for s in codes3])
print('EX1-8 - ',  [chr(s) for s in codes4])

print()
print()

# Generator(모터만 반환한다. )
# 반복을 하면서 값을 생성

import array

# Generator : 한 번에 한개의 항목을 생성(메모리 유지하지 않음. 그래서 성능이 매우 좋다.)
# List Comprehension에서는 []을 사용한 것처럼, ()로 튜플모양으로 감싸주면 Generator가 실행된다.  
# 여기까지는 값 생성한 게 아닌, 대기 상태이다. 메모리에 올리기 전 상태
tuple_g = (ord(s) for s in chars)
print('EX2-1 - ', tuple_g)

# next함수나 for문을 사용하지 않으면 메모리에 올리지 않는다. 
print('EX2-2 - ', next(tuple_g))
print('EX2-2 - ', next(tuple_g))

# Array
array_g = array.array('I', (ord(s) for s in chars))

print('EX2-4 - ', array_g)
print('EX2-5 - ', array_g.tolist())

# 제네레이터 예제
print('EX3-1 - ', ('$s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)):
    print('EX3-2 - ', s)

print()
print()

# 리스트 주의 할 점
marks1 = [['~'] * 3 for n in range(3)]
marks2 = [['~'] * 3] * 3

# 같은 결과 같지만 큰 차이가 있다...
print('EX4-1 - ', marks1)
print('EX4-2 - ', marks2)

print()

marks1[0][1] = 'X'
marks2[0][1] = 'X'

print('EX4-3 - ', marks1)
print('EX4-4 - ', marks2)

# 증명
print('EX4-5 - ', [id(i) for i in marks1]) # list comprehension으로 만든 것은 객체가 다른 id를 가진다. 
print('EX4-6 - ', [id(i) for i in marks2]) # 곱해서 만든 것은 같은 id를 갖게 된다. 
# 밖에서 곱하면 객체 안에 같은 것을 append가 되고
# list comprehension을 사용했으면 내부에서 최종까지 코드를 작성하는 것이 좋다. 
# 정말 많이 나오는 실수이다. 주의 할 것. 

# Tuple Advanced (컨테이너, 불변)

# Packing & Unpacking

print('EX5-1 - ', divmod(100, 9)) #결과 값 튜플
# divmod함수 인자로 튜플을 넣을 경우 튜플 앞에 *을 붙이면 패킹을 하는 의미이다.
# 패킹을 해서 넘기면 내부에서 알아서 unpacking을 해서 계산한다. 
print('EX5-2 - ', divmod(*(100, 9)))  
print('EX5-3 - ', *(divmod(100, 9))) #최종 결과값이 unpacking이 된다. 

print()

x, y, *rest = range(10) # *rest는 list로 나머지 값들을 패킹한다. 
print('EX5-4 - ', x, y, rest) 
x, y, *rest = range(2)  # 반환되는 값이 없으니 빈 list를 반환한다. 
print('EX5-5 - ', x, y, rest) 
x, y, *rest = 1,2,3,4,5
print('EX5-5 - ', x, y, rest) 

# 메소드에서 **일때는 딕셔너리 형태, *일 때는 묶여서 패킹된 형태로 된 것을 함수 내에서 unpack해서 사용 가능하다.
# def test(*args, **args)

print()
print()

# Mutable(가변) vs Immutable(불변)

l = (10, 15, 20)
m = [10, 15, 20]

print('EX6-1 -', l, m, id(l), id(m))

# *은 append의 개념이다.
# 튜플의 경우 값을 바꿀 순(재할당) 없지만, 이것은 길이를 확장하는 extend개념이기 때문에 연산이 가능하다. 
l = l * 2
m = m * 2

# 리스트와 튜플 모두 변수에 새롭게 할당을 했기 때문에 id값이 다르다. 
print('EX6-2 - ', l, m, id(l), id(m))

# 튜플은 자체 연산자를 사용해도 값이 바뀐다.
# 리스트는 자기 리스트에 재할당을 했다. 

l *= 2
m *= 2

print('EX6-3 - ', l, m, id(l), id(m))

# 리스트의 경우 재할당을 할 경우 l = l * 2방식을,
# 객체 자체를 활용할 경우에는 내부 수정이 가능한 l *= 2방식을 사용해야 한다. 


# sort vs sorted
# reverse, key=len, key=str.lower, key=func

f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']

# sorted : 정렬 후 '새로운' 객체 반환

print('EX7-1 - ', sorted(f_list))
print('EX7-2 - ', sorted(f_list, reverse=True)) # 역순으로 정렬
print('EX7-3 - ', sorted(f_list, key=len)) # 문자의 길이 순으로 정렬
print('EX7-3 - ', sorted(f_list, key=len)) # 문자의 길이 순으로 정렬
print('EX7-4 - ', sorted(f_list, key=lambda x: x[-1])) # key=func의 경우.  단어의 끝 글자를 기준으로 정렬
print('EX7-4 - ', sorted(f_list, key=lambda x: x[-1], reverse=True))

print('EX7-6 - ', f_list) # 원본은 바뀌지 않았다.

print()

# sort : 정렬 후 객체 직접 변경
# None을 반환하면 이 함수는 반환값이 없는 함수임을 의미한다. 객체를 직접 반환하는 함수라고 생각해도 된다.  
a = f_list.sort()
print(a, f_list)

# 반환값은 None이기에, 우리는 원본만 보면 된다. 
print('EX7-7 - ', f_list.sort(), f_list)
print('EX7-8 - ', f_list.sort(reverse=True), f_list)
print('EX7-9 - ', f_list.sort(key=len), f_list)
print('EX7-10 - ', f_list.sort(key=lambda x : x[-1]), f_list)
print('EX7-11 - ', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)
