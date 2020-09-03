def print1():    
    print('I am Nice Boy.')

def print2():
        print('I am Good Boy.')

# 현재 파일로 실행하면 실행됨(단위 테스트)
# 타 파일에서 import할 경우 실행되지 않음
if __name__ == "__main__":
    print1()
    print2() 