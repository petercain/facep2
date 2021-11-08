'''프로그램을 만드시면서 요구사항이나 이미있는 사물 코드화하는 작업들을 해싸, 별도찍고, 구독자증가, 금붕어도 키워보고 숫자, 영어, 기호 -> 컴파일러, 인터프리터 0,1
사물들을 코드드로 변환시키는것 -> 추상화
object 사물들을 객체로 만들고

사물이 가지고 있는속성
자동차 변수
색깔 변수
브랜드 변수
차종 변수
바퀴 변수

기능(얘가 해야되는것)
에어컨 on-> 함수
네비게이션 on -> 함수

클래스하는 이름으로 묶는 작업
자동차(속성,기능)
게임에서 클래스(직업)
전사 궁수 마법사 힐러
전사 클래스 내의
ID = peter
전사의 특성과 기술들
..
...
....
플라톤의 이데아?좀 다르긴한데 아무튼

class student
score = 학생의 점수
name
code = 학번

변수 - . 반복, 명시화
함수
클래스 -> 객체(객체)

클래스 도물->움직이는 애들
클래스 고양이과        클래스 개과
->발톱,야행성         ->멍멍, 산책성

Exception
안에 각종 에러들

students = [
    {"name": "윤인성", "korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "연하진", "korean": 92, "math": 98, "english": 96, "science": 98},
    {"name": "구지연", "korean": 76, "math": 96, "english": 94, "science": 90},
    {"name": "나선주", "korean": 98, "math": 92, "english": 96, "science": 92},
    {"name": "윤아린", "korean": 95, "math": 98, "english": 98, "science": 98},
    {"name": "윤명월", "korean": 64, "math": 88, "english": 92, "science": 92}
]

print("이름", "총점", "평균", "수학", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    sore_average = score_sum / 4

    print(student["name"], score_sum, sore_average, student["math"], sep="\t")

scores = {
    "korean":[87,92,76,98,95,64,],
    "math":[98,98,96,92,98,88],
    "english":[88,96,94,96,98,92],
    "science":[95,98,90,92,98,92],
    "python":[80,85,96,100,60,70]
}
for key,element in scores.items():
    print("과목:{}, 평균:{}, 최고점:{}, 최소점:{}".format({key},sum(element)/len(element),max(element),min(element)))

class Student:
    #생성자 함수에 name,korean...등을 받아서 클래스를 생성한다.
    #이 클래스는 이러한 속성을 가지는 것이 필수니까
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

students = [
    Student("윤인성",87,98,88,95),
    Student("연하진",92,98,96,98),
    Student("구지연",76,96,94,90),
    Student("나선주",98,92,96,92),
    Student("윤아린",95,98,98,98),
    Student("윤명월",64,88,92,92)
]

for amugona in students:
    print(amugona.name)

class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_averange(self):
        return self.get_sum() / 4

    def to_string(self):
        return "{}\t{}\t {}".format(self.name,self.get_sum(),self.get_averange())

students = [
    Student("윤인성",87,98,88,95),
    Student("연하진",92,98,96,98),
    Student("구지연",76,96,94,90),
    Student("나선주",98,92,96,92),
    Student("윤아린",95,98,98,98),
    Student("윤명월",64,88,92,92)
]

print("이름","\t총점\t","평균",)
for amugona in students:
    print(amugona.to_string())
print("{} {}".format(students[0].name,students[0].get_sum()))


class Student:
    def __init__(self):
        print("생성자 실행")
        print("학생 클래스가 호출될때 실행됩니다")
        self.math = 0
    python = 0

class Professor:
    def __init__(self):
        print("생성자 실행")
        print("교수 클래스가 호출될때 실행됩니다")
        self.pay = 0
        self.python = 0

class University:
    def __init__(self):
        print("힉교 클래스 호출")
        student = Student()
        student.python = 100

uni = University()
pro = Professor()
stu = Student()

pro.pay = 10000
pro.python = 90

print((pro.python))
print(stu.python)
'''


class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init__ 메소드가 호출되었습니다.")

    def test(self):
        print("Parent 클래스의 test() 메소드입니다")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child 클래스의 __init()__메소드가 호출 되었습니다.")
    def test(self):
        print("자식의 테스트 메소드입니다")


child = Child()
child.test()
print(child.value)





#
# 상속을 받을 클래스는
# 부모 클래스의 변수와 함수를 활용가능하다
# 또 한 내가 다시 재정의해서 쓸 수 있다
# Overriding 오버라이딩이라고 한다.
# 스타크래트 공격을 시키면 공격을 실해했는데 어떤애는 근접, 원거리, 원거리2 공격함수를 받았는데 다시 각각 재정의해서 각각사용

#
# class CustomException(Exception):
#     def __init__(self):
#         Exception.__init__(self)
#         print("내가 만든 오류가 생성되었어요")
#     def __str__(self):
#         return "오류가 발생했아요"
#
# raise CustomException

class Student:
    def study(self):
        print("공부를 함시다")

class Teacher:
    def teach123(self):
        print("학생을 가르칩니다")

classroom = [Student(), Student(), Teacher()]

for amu in classroom:
    if isinstance(amu, Student):
        amu.study()
    elif isinstance(amu, Teacher):
        amu.teach123()


class Student:
    #생성자 함수에 name,korean...등을 받아서 클래스를 생성한다.
    #이 클래스는 이러한 속성을 가지는 것이 필수니까
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

students = [
    Student("윤인성",87,98,88,95),
    Student("연하진",92,98,96,98),
    Student("구지연",76,96,94,90),
    Student("나선주",98,92,96,92),
    Student("윤아린",95,98,98,98),
    Student("윤명월",64,88,92,92)
]

for amugona in students:
    print(amugona.name)

class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_averange(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t {}".format(self.name,self.get_sum(),self.get_averange())

students = [
    Student("윤인성",87,98,88,95),
    Student("연하진",92,98,96,98),
    Student("구지연",76,96,94,90),
    Student("나선주",98,92,96,92),
    Student("윤아린",95,98,98,98),
    Student("윤명월",64,88,92,92)
]

print("이름","\t총점\t","평균")
for student in students:
    print(str(student))



class Student1:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

students1 = [
    Student1("윤인성",87,98,88,95),
    Student1("연하진",92,98,96,98),
    Student1("구지연",76,96,94,90),
    Student1("나선주",98,92,96,92),
    Student1("윤아린",95,98,98,98),
    Student1("윤명월",64,88,92,92)
]

print("이름","\t총점\t","평균")
for student in students1:
    print(str(student))

