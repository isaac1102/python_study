# Section05-2
# 파이썬 흐름제어(반복문)

# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print("v1 is : " , v1)
    v1 += 1

for v2 in range(10):
    print("v2 is : " , v2)

for v3 in range(2, 10):
    print("v3 is : " , v3)


sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1 

print("1 ~ 100의 합 ", sum1)
print("1 ~ 100의 합 ", sum(range(1, 101)))
# range함수에 3가지 매개변수를 넣으면 마지막 값은 건너뛰는 간격이다
#                               시작, 끝, 증감단위
print("1 ~ 100의 합 ", sum(range(1, 101, 2)))



