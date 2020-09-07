# Section04-2
# 문자열, 문자열 연산, 슬라이싱

str1 = 'I am boy.'
str2 = 'NiceMan'
str3 = ''
str4 = str('')


# 문자열 길이 len
print(len(str1), len(str2), len(str3), len(str4))

# Raw String
# 주로 경로 표시할 때 
raw_s1 = r'C:\python_basic\Lib\site-packages'
print(raw_s1)
raw_s2 = r'\a\a\t\t\s\s'
print(raw_s2)

# 멀티라인
multi = \
"""
문자열

멀티라인

테스트
"""

print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = 'niceman'
print(str_o1 * 100)
print(str_o2 + str_o3)
# print(str_o1 + 1)
# a라는 문자가 str_o4에 포함돼 있는가
print('a' in str_o4)
print('f' in str_o4)
print('f' not in str_o4)

print(str(77))

print(str(77), type(str(77)))


# 문자열 함수
a = 'nicemaN'
b = 'orange'

print(a.islower())
print(a.endswith('N'))
print(a.capitalize())
print(a.replace('nice', 'good'))
print(list(reversed(b)))

print(a[0:3]) 
print(a[0:4])
print(a[0:len(a)])
print(a[:])
# 3번째 옵션을 넣으면 갯수만큼 점프한다.
print(b[0:4:3])
print(b[1:-2])
print(b[::-1])