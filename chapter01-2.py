 # Chapter01-1
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 클래스 재 선언
class Student():
    """
    Student Class 
    Author : isaac
    Date : 2020.09.01
    Description : 클래스 학습
    """

    # 클래스 변수
    student_count =  0

    def __init__(self, name, number, grade, details, email=None):
        # 인스턴스 변수
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email
    
        Student.student_count += 1
    
    def __str__(self):
        return 'str : {}'.format(self._name)
    
    def __repr__(self):
        return 'repr : {}'.format(self._name)

    def detail_info(self):
        # 고유 참조값 출력
        print('Current Id : {} '.format(id(self)))
        print('Student Detail info : {} {} {}'.format(self._name, self._email, self._details))
    def __del__(self):
        Student.student_count -= 1

    
# Self의 의미
studt1 = Student('Cho', 2, 3, {'gender' : 'male', 'score1':81, 'score2':91})
studt2 = Student('Cho', 3, 4, {'gender' : 'female', 'score1':82, 'score2':92}, 'ddd@naver.com')

# ID 확인
print(id(studt1))
print(id(studt2))

print(studt1 == studt2)
# 실제적인 값을 비교
print(studt1._name == studt2._name)
# id값이 같은 지 비교
print(studt1 is studt2)

# dir & __dict__ 확인
# dir : 모든 속성(파이썬에서 기본으로 제공하는 속성까지)을 보여줌
print(dir(studt1))
print(dir(studt2))
# __dict__ :  속성과 값을 보여줌
print(studt1.__dict__)
print(studt2.__dict__)


# Docstring : 주석 확인
print(Student.__doc__)

# 실행
studt1.detail_info()
studt2.detail_info()


# 에러
# Student.detail_info()

Student.detail_info(studt1)

# 비교
print(studt1.__class__, studt2.__class__)
print(id(studt1.__class__), id(studt2.__class__))

print()

# 인스턴스 변수
# 직접 접근(PEP 문법적으로 권장X)
studt1._name = 'hahaha'
print(studt1._name, studt2._name)
print(studt1._email, studt2._email)

# 클래스 변수
# 인스턴스, 클래스 모두에서 접근 가능하다.
# 접근
print(studt1.student_count)
print(studt2.student_count)
print(Student.student_count)

print()
print()

# 클래스 딕셔너리 네임 스페이스에는 뭐가 있는가?
# print(Student.__dict__)

# 공유확인
print(studt1.__dict__)
print(studt2.__dict__)

# 인스턴스 네임스페이스 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))

del studt2

print(studt1.student_count)
print(Student.student_count)
