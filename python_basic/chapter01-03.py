# Chapter01-3
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, 스테이틱 메소드

# 기본 인스턴스 메소드

class Student(object):
    '''
    Student Class
    Author : Jeong
    Date : 2020.09.02
    Description : Class, static, Instance Method
    '''

    # Class Variable
    tuition_per = 1.0

    # 초기화 메서드(자바의 생성자)
    def __init__(self, id, first_name, last_name, email, grade, tuition_per, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition_per
        self._gpa = gpa
        
    # Instance Method
    def full_name(self):
        return '{}, {}'.format(self._first_name, self._last_name)
    
    # Instance Method
    def detail_info(self):
        return 'Student Detail Info : {}, {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._grade)
    
    # Instance Method
    def get_fee(self):
        return "Before Tuition -> Id : {}, fee : {}".format(self._id, self._tuition)
    
    # Instance Method
    def get_fee_culc(self):
        return 'After tuition -> Id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition_per)

    def __str__(self):
        return 'Student Info -> name : {}, grade : {}, email : {}'.format(self.full_name(), self._grade, self._email )

    # Class Method
    @classmethod #클래스 데코레이터
    def raise_fee(cls, per):
        if per < 1 :
            print('Please Enter 1 or Move')
            return
        # cls는 여기서 Student클래스를 의미    
        cls.tuition_per = per
        print('Success! tuition increased!')

    # Class Methood 
    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, tuition *  cls.tuition_per, gpa)
     
    # staticmethod
    @staticmethod
    def is_scholarship_st(inst):
        if inst._gpa >= 4.3 : 
            return '{} is a scholarship recipient. '.format(inst._last_name)
        return 'Sorry. Not a scholarship recipient.'


# 학생 인스턴스
student_1 = Student(1, 'kim', 'sarang', 'kim1@namver.com', '1', 400, 3.5)
student_2 = Student(2, 'Lee', 'Myungho', 'lee@namver.com', '2', 500, 4.3)

# 기본정보
print(student_1)
print(student_2)

print()
# 전체 정보
print(student_1.detail_info())
print(student_2.detail_info())

# 학비정보(인상 전)
print(student_1.get_fee())
print(student_2.get_fee())
print()


print()

# 학비 인상(클래스 메소드 미사용)
# Student.tuition_per = 1.2

# 학비 인상(클래스 메소드 미사용)
Student.raise_fee(1.3)

print(student_1.get_fee_culc())
print(student_2.get_fee_culc())

# 클래스 메소드 인스턴스 생성 실습(객체 생성에 이 방법을 권장함)
student_3 = Student.student_const(3, 'park', 'minji', 'student3@gmail.com', '3', 550, 4.5)
student_4 = Student.student_const(4, 'lee', 'sunghan', 'student4@gmail.com', '4', 600, 4.1 )

# 전체정보
print(student_3.detail_info())
print(student_4.detail_info())
print()

# 학생 학비 변경 확인
print(student_3._tuition)
print(student_4._tuition)
print()


# 장학금　혜택　여부（스테이틱　메소드　미사용）
def is_scholarship(inst):
    if inst._gpa >= 4.3 : 
        return '{} is a scholarship recipient. '.format(inst._last_name)
    return 'Sorry. Not a scholarship recipient.'

print(is_scholarship(student_1))
print(is_scholarship(student_2))
print(is_scholarship(student_3))
print(is_scholarship(student_4))

print()
print()

print(Student.is_scholarship_st(student_1))
print(Student.is_scholarship_st(student_2))
print(Student.is_scholarship_st(student_3))
print(Student.is_scholarship_st(student_4))

print()
print()

print(student_1.is_scholarship_st(student_1))
print(student_1.is_scholarship_st(student_2))
print(student_1.is_scholarship_st(student_3))
print(student_1.is_scholarship_st(student_4))