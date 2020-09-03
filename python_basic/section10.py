# Section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임)프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크

# SyntaxError : 잘못된 문법
# 1. print('Test)
# 2. if True
#      pass
# 3. x=>y (말도 안되는 문법)

# NameError : 참조변수 없음
a = 10
b = 15
# print(c)

# ZeroDivisionError : 0 나누기 에러
# print( 10 / 0 ) 

# IndexError : 인덱스 범위 오버

x = [10, 20, 30]
print(x[0])
# print(x[3]) 예외 발생

# keyError
dict = {'name' : 'kim', 'age' : 33, 'city' : 'seoul'}
# print(dict['hobby']) 없는 키를 조회할 때 
print(dict.get('hobby')) # get메소드를 활용하면 없을 때 None으로 리턴함

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
import time
print(time.time())
# print(time.month()) #없는 attribute를 불러오려 할 때 발생하는 에러

# ValueError : 참조 값이 없을 때 발생
x = [1 , 5, 9]

# x.remove(10) : 리스트에 없는 값을 삭제하려 할 때
# x.index(10) : 리스트에 없는 값의 인덱스를 찾으려 할 때 


# FileNotFoundError
# f = open('test.txt', 'r') : 파일 처리 예외 발생


# TypeError 
x = [1, 2]
y = (1, 2)
z = 'test'

# print(x + y) : 튜플과 리스트는 결합할 수 없다.
# print(x + z) : list와 str은 결합할 수 없다.
print(x + list(y))  # 형 변환이 필요


# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩(사람은 완벽하지 않으므로)
# 그 후 런타임 예외 발생 시 예외 처리 코딩 권장(EAFP 코딩 스타일)

# 예외 처리 기본
# try : 에러가 발새ㅐㅇ할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행되는 구문

# 예제1
name = ['kim', 'lee', 'park']
try: 
    z = 'kim' #'cho'의 경우 예외 발생
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not found it! - Occured ValueError!')
else:
    print('ok! else!')


# 예제2
try: 
    z = 'jin'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except:
    print('Not found it! - Occured Error!')
else:
    print('ok! else!')

# 예제3
try: 
    z = 'kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not found it! - Occured ValueError!')
else:
    print('ok! else!')
finally:
    print('finally ok')


#예제4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    print('try')
finally:
    print('ok finally!!')


# 예제5
try: 
    z = 'kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
    # value에러를 예상해서 처리
except ValueError as l: #alias를 주고 print할 수 있다.
    print(l)
    print('Not found it! - Occured ValueError!')
    # index에러를 예상해서 처리
except IndexError:
    print('Not found it! - Occured IndexError!')
    # 이도 저도 아니면 마지막에 모든 에러 처리
except Exception:
    print('Not found it! - Occured Error!')
else:
    print('ok! else!')
finally:
    print('finally ok')

# 예제6
# 예외 발생: raise
# raise 키워드로 예외 직접 발생 (고급 프로그래밍)

try:
    a = 'Ki33m'
    if a == 'Kim':
        print('ok')
    else:
        raise ValueError
except ValueError:
    print('문제 발생')
except Exception as f:
    print(f)
else:
    print('ok')