# 다음은 map함수에 대한 설명이다. map 함수와 lambda 함수를 이용하여, 10진수 숫자가 문자열로 작성된 리스트 a의 각 원소의 값을 1씩 증가시킨 문자열로 변경하는 프로그램을 한 줄의 코드로 작성하시오.

# map(func, iter) 함수는 두 개의 입력을 받는다.
# 첫 번째 입력 func은 하나의 입력을 받는 함수이며, 반드시 출력이 존재한다.
# map 함수는 두 번째 입력 iter를 순회하면서 각 원소 elem을 func의 입력으로 하여, func(elem)을 출력하는 iterative object를 출력한다.
# map의 출력은 일회성으로 동작하는 iterative object이며, list() 또는 tuple()을 이용하여 여러번 참조할 수 있도록 변환할 수 있다.

# a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# <이곳에 들어갈 한 줄의 코드를 작성하시오.>
# print(a)

# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

a = list(map(lambda x : str(int(x)+ 1), a))
print(list)
print(a)

# 과제 2번 코드란

a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
a = list(map(lambda x : str(int(x) + 1), a))
print(a) 




# 과제2
# 다음 동작 수행하는 프로그램을 작성하시오. (단, 입력 a의 내용이 아래 예시 입력과 달라져도 프로그램이 동작해야 한다.)

# 최대 인원 수가 정해진 방과후 수업에 학생들을 배정하려고 한다.
# 학생들은 각자 원하는 스포츠 종목을 적어냈고, 해당 종목들은 리스트 a에 저장되어 있다.
# 방과후 수업에는 최대 정원이 있어, 파이썬 프로그램을 이용해 자료를 처리하고자 한다. 각 스포츠 종목별로 지원자의 수를 출력하는 프로그램을 작성하시오.
# a = ['base ball', 'basket ball', 'soccer', 'base ball', 'soccer', 'soccer', 'basket ball', 'base ball', 'basket ball', 'soccer', 'basket ball', 'basket ball', 'base ball', 'soccer', 'soccer', 'basket ball', 'basket ball', 'base ball', 'base ball']
 
# 출력:

# basket ball 7
# base ball 6
# soccer 6

a = ['base ball', 'basket ball', 'soccer', 'base ball', 'soccer', 'soccer', 'basket ball', 'base ball', 'basket ball', 'soccer', 'basket ball', 'basket ball', 'base ball', 'soccer', 'soccer', 'basket ball', 'basket ball', 'base ball', 'base ball']

sub_dict = {}

for subject in a :
    sub_dict[subject] = 0        

for subject in a :
    for k, v in sub_dict.items():
        if subject == k :
            sub_dict[k] = v +1

for k,v in sub_dict.items():
    print(k, v)



# 반복문과 print() 함수를 이용하여 아래와 같은 출력을 하는 프로그램을 구현하시오.
# 출력:
# 0 1 2 4 8 16 32 64 128 256 256 256

print(0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 256, 256)
        
print(0, 2**0, 2**1, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7, 2**8, 2**8, 2**8)   

list = []
for i in range(0, 11):
    if i == 0 :
        list.append(i)
        list.append(2**i)
    elif i > 0 and i <8 :
        list.append(2 ** i)
    else :
        list.append(2 ** 8)

for num in list:
    print(num, end=' ')
