# Chapter03-2
# 파이썬 심화
# 시퀀스형
# 해시테이블(hashtable)
# Dict -> Key 중복 허용하지 않음. Set -> 중복 허용하지 않음
# 중복허용이 없다는 것은 같은값이 내부적으로 있는지 검사한다는 의미와 같음.
# 이때 hashtable을 내부적으로 사용한다. 
# hashtable엔진에서 해쉬값이라는 숫자를 만들어서 숫자가 같으면 중복값이 있고, 아니면 서로 다른 값으로 생각하는 것이다.
# hashtable은 적은 리소스로 많은 데이터를 효율적으로 관리할 수 있다. 색인과 같다. 
# Dict 및 Set 심화

# Dict 구조
print('ex1-1 -')
# print(__builtins__.__dict__) # 파이썬 내장함수 목록을 볼 수 있다. 

print()
print()

# Hash 값 확인
# 둘의 차이점은?
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])
# 튜플은 불변. 리스트는 가변.
# 따라서 리스트는 해쉬값 생성 불가하다. (언제든 변경 가능하기에)

print('ex1-2 - ', hash(t1)) # t1이라는 변수에 할당된 튜플형태의 자료형의 해쉬값이 출력된다. 
# print('ex1-3 - ', hash(t2)) # t2는 리스트이기 때문에 에러 발생, 가변형이라서 그렇다. 

print()
print()

# 지능형 딕셔너리(Comprehension Dict)
import csv

# 외부 CSV to List of tuple
with open('./resource/test1.csv', 'r', encoding='utf-8') as f:
    temp = csv.reader(f)
    # Header skip
    next(temp)
    # 변환
    NA_CONDES = [tuple(x) for x in temp]

print('ex2-1 -')
print(NA_CONDES)

n_code1 = {country : code for country , code in NA_CONDES}
n_code2 = {country.upper(): code for country, code in NA_CONDES}

print()
print()

print('ex2-2 - ',)
print(n_code1)
print()
print()
print('ex2-3 - ',)
print(n_code2)

print()
print()

# Dict Setdefault 예제
# 딕셔너리에서 사용할 키값이 중복되는 경우... k1, k2가 중복됨
source = (('k1', 'val1'),
            ('k1', 'val2'),
            ('k2', 'val3'),
            ('k2', 'val4'),
            ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print('ex3-1 - ', new_dict1)

# Use setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v) #있으면 k, 없으면 []로 append하겠다.

print('ex3-2 - ', new_dict2)

# 사용자 정의 dict 상속(UserDict 가능)
class UserDict(dict):
    def __missing__(self, key):
        print('Called : __missing__ method')
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        print('Called : __getitem__ method')
        try:
            return self[key]
        except KeyError:
            return default
    
    def __contains__(self, key):
        print('Called : __contains__ method')
        return key in self.keys() or str(key) in self.keys()
    
        
user_dict1 = UserDict(one=1, two=2)
user_dict2 = UserDict({'one':1, 'two':2})
user_dict3 = UserDict([('one',1), ('two', 2)])

# 출력
print('ex4-1 - ', user_dict1, user_dict2, user_dict3)
print('ex4-2 - ', user_dict2.get('two'))
print('ex4-3 - ', 'one' in user_dict3)
# print('ex4-4 - ', user_dict3['three'])
print('ex4-5 - ', user_dict3.get('three'))

# print('ex4-4 - ', user_dict3['three']) # 에러 발생
print()
print()

# immutable Dict

from types import MappingProxyType
d = {'key1' : 'TEST1'}

# Read Only
d_frozen = MappingProxyType(d)

print('ex5-1 - ', d, id(d))
print('ex5-2 - ', d_frozen, id(d_frozen))
print('ex5-3 - ', d is d_frozen, d == d_frozen) #첫번째 비교는 id을 비교, 두번째는 값을 비교

# 수정 불가
# d_frozen['key1'] = 'TEST2' # 'mappingproxy' object does not support item assignment 에러 남

# d_frozen['key2'] = 'TEST2'
d['key2'] = 'TEST2'

print('ex5-4 - ', d)

print()
print()

# Set 구조(FrozenSet)
s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set() # 빈 set을 선언할 때.  Not {}
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

# 추가
s1.add('Melon')
print('ex6-1 - ', s1, type(s1))

# 추가 불가

