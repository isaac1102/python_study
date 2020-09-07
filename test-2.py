# 다음과 같이 작성된 csv 파일을 읽고, 읽어들인 모든 값을 더해서 출력하는 파이썬 프로그램을 작성하시오. csv파일의 위치는 실행 위치와 동일하다고 가정한다(a.csv). (단, csv 파일의 내용은 달라질 수 있으며, 자료의 개수는 10000개 이하이다.)

# --------------- a.csv --------------------
# 10,60,20,33,55,25,64,83,523,54,87,84,56,84
# ------------------------------------------
# ---------- 출력 ------------
# 1238
# ----------------------------

import csv

with open('./a.csv', 'r') as f:

    content = csv.reader(f)

    sum = 0

    for i in content:
        for v in i :
            sum += int(v)
    
    print(sum)


# 과제 2
# 아래 기반 코드를 완성하여, 입력받은 값 중 중앙값을 출력하는 클래스를 완성하시오. 
# 입력받은 값이 짝수개이면, 중앙값 2개의 평균을 출력하시오. (단, clear 메소드는 입력받은 내역을 모두 삭제)

import math
class Median:
    
    def __init__(self):
        self.input_list = []
 
    def get_item(self, item):
        self.input_list.append(item)
 
    def clear(self):
        self.input_list.clear()
 
    def show_result(self):
        length = len(self.input_list)
        if length % 2 == 0:
            # 가운데 두 수의 평균을 출력
            center1 = self.input_list[int(length/2)]
            center2 = self.input_list[int(length/2) + 1]
            
            avg =(center1 + center2) / 2
            
            print(' 가운데 두 수의 평균을 출력 : ' , avg)

        else : 
            # 가운데 수를 출력
            center = self.input_list[int(length/2)]
            
            print(' 가운데 수를 출력 : ', center)
 
median= Median()
for x in range(12):
    median.get_item(x)
median.show_result()

median = Median()
for x in range(13):
    median.get_item(x)
median.show_result()
 
median.clear()
for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
    median.get_item(x)
median.show_result()




# 과제3
# 아래 기반 코드를 완성하여, 주어진 출력을 하는 클래스를 구현하시오. 
# 단, Animal 클래스는 수정하지 않고 구현하시오. 최소한의 메소드만을 추가하여 구현하시오. 
# 하나의 메소드는 하나의 line만을 출력하시오.

class Animal:
    def __init__(self, name):
        self.name = name
 
    def speak(self):
        print(self.name + ' cannot speak.')
 
    def move(self):
        print(self.name + ' cannot move.')
 
 
class Dog(Animal):
    def move(self):
        print(self.name + ' moves like a jagger.')
 
class Retriever(Dog):
    def speak(self):
        print(self.name + 'is smart enough to speak.')
 
 
dog = Dog('Nancy')
dog.speak()
dog.move()
 
super_dog = Retriever('Michael')
super_dog.speak()
super_dog.move()

# ---------- 출력 -----------------
# Nancy cannot speak.
# Nancy moves like a jagger.
# Michael is smart enough to speak.
# Michael moves like a jagger.
# ---------------------------------



# 과제4.
# 아래 기반 코드를 완성하여, 주어진 출력을 하는 클래스를 구현하시오. 
# 단, 하나의 메소드에서는 단 하나의 line만을 출력하시오. PEP를 준수하여 코드를 작성하시오.

class Foo:

    @classmethod
    def bar(cls):
        print('A')

    class Bar:
        @classmethod
        def func(cls):
            print('C')


    def func(self):
        print('B')

    def __str__(self):
        return 'D'


    


Foo.bar()
Foo().func()
Foo.Bar.func()
print(Foo())

# ----- 출력 -----
# A
# B
# C
# D
# ----------------