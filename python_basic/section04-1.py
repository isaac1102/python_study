# 데이터 타입

v_str = 'Niceman'
v_bool = True
v_str2 = 'Goodboy'
v_fload = 10.3
v_int = 3
v_dictionary = {
    "name" : "Jeong",
    "age" : 34
}

v_tuple = 3, 5, 7
v_set = {7,8,9}
v_list = [3,5,7]

print(type(v_tuple))
print(type(v_dictionary))
print(type(v_bool))
print(type(v_fload))
print(type(v_int))
print(type(v_list))


i1 = 39
i2 = 939
big_int1 = 999999999999999999999999999999
big_int2 = 777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)

print(10/3)
print(10//3)
print(10%3)
print(2**3)
print(f1**f2)

result = i1 ** i2
print(result, type(result))

a = 5.
b = 4
c = 10.

print(type(a), type(b))
result2 = a + b
print(result2, type(result2))


# 형변환
# int, float, complex(복소수)

# float to int
print(int(result2))

print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'), type(int('3')))
print(complex(False))


# 단항연산자

y = 100
y = y + 100
y += 100 
y *= 100
print(y)


# 수치 연산 함수
print(abs(-7))

# 10을 3으로 나눠서 몫은 n에 나머지는 m에 넣는다
n, m = divmod(10, 3)
print(n, m)

import math
# 올림
print(math.ceil(5.1))
# 내림
print(math.floor(3.874))