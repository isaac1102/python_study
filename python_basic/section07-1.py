# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 예제1

class UserInfo:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print("Name: " + self.name)

    def __del__(self):
        print("Instance removed!")


user1 = UserInfo("Kim")
user2 = UserInfo("Park")

print(id(user1))
print(id(user2))

user1.print_info()
user2.print_info()

print('user1 : ', user1.__dict__)  # 클래스 네임스페이스 확인
print('user2 : ', user2.__dict__)

print(user1.name)


# 예제2
# self의 이해

class SelfTest:
    def function1():
        print("function1 called!")

    def function2(self):
        print(id(self))
        print("function2 called!")

SelfTest.function1()
self_test = SelfTest()
self_test.function2()


# 예제3
# 클래스 변수, 인스턴스 변수

class WareHouse: 
    # 클래스 변수
    stock_num = 0
    def __init__(self,name):
        self.name  = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse("Kim")
user2 = WareHouse("Park")
user3 = WareHouse("Lee")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)

print(user1.name)
print(user2.name)
print(user3.name)

# 자기 네임스페이스에 없으면 클래스 네임스페이스에 가서 찾는다
print(user1.stock_num)

# del 명령어로 인스턴스 삭제 
del user1

print(user2.stock_num)
print(user3.stock_num)