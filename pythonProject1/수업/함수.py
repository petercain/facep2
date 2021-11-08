def print_n_times(n=2, *values):
    for i in range(n):
        for value in values:
            print(value)
        print("한국다람쥐")

print_n_times()



def test(a, b=10, c=100):
    print(a+b+c)
test(10,20,30)
test(a=10,b=100,c=200)
test(c=10,a=100,b=200)
test(10,c=200)

#함수내에서 어떤 시점이나 코드에서 바로 함수를 끝내고 싶을때 return을 사용한다
def return_test():
    print("A")
    return
    print("B")

return_test()

def sum_all(start, end):
    output = 0
    for i in range(start,end +1):
        output = output + i

    return output

print("0 to 100:", sum_all(0,100))
print("0 to 1000:", sum_all(0,1000))
print("50 to 100:", sum_all(50,100))
print("500 to 1000:", sum_all(500, 1000))


def sum_all2(start=0, end=100, step = 1):
    output = 0
    for i in range(start,end +1, step):
        output = output + i

    return output

print("A", sum_all2(0, 100 ,10))
print("b", sum_all2(end=100))
print("C", sum_all2(end=100,step=2))

def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output

print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))


def factorial_(n):
    if n == 0:
        return 1
    else:
        return n * factorial_(n-1)

print("1!:", factorial_(1))
print("2!:", factorial_(2))
print("3!:", factorial_(3))
print("4!:", factorial_(4))
print("5!:", factorial_(5))




def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("fibonacci(1):", fibonacci(1))
print("fibonacci(2):", fibonacci(2))
print("fibonacci(3):", fibonacci(3))
print("fibonacci(4):", fibonacci(4))
print("fibonacci(5):", fibonacci(5))




counter = 0

def fibonacci(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
fibonacci(10)
print("---")
print("fibonacci(10)계산에 활용된 덧셈 횟수는 {}번입니다".format(counter))




dictionary = {
    1: 1,
    2: 1
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output

print("fibonacci(10):", fibonacci(10))
print("fibonacci(20):", fibonacci(20))
print("fibonacci(30):", fibonacci(30))
print("fibonacci(40):", fibonacci(40))
print("fibonacci(50):", fibonacci(50))


'''
함수호출 할 때 주의점
1.매개변수의 타입을 신경써야한다.
2.매개변수의 개수

함수의 매개변수 활용

1. 가변 매개변수
    -> 변수의 개수를 유동적으로 쓰는 것
        변수에 *표시
    -> def 함수이름(*변수이름)
2. 기본 매개변수
    -> 함수의 매개변수에 기본 값을 지정해주는 것
    -> def 함수이름(변수 = 값)
3. 키워드 매개변수
    -> 함수를 호출할 때 함수의 매개변수에
       어떤 매개변수인지 지정해주는 것
    -> 함수이름(매개변수=값(변수))
함수():
if(조검삭)
조건일 때 수행하는 코드
return

반복되는 작업(값만 달라지고) 함수로 정의해서 쓴다
유지보수하기가 쉽다.
함수의 이름으로 함수의 기능을 유추할 수 있다.
'''