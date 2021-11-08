import random

# 튜플은 리스트와 비슷하지만 한번 결정된 요소를 바꿀 수 없다
# 근데 교환은 된다


tuple_t = (10,20,30)
list_t = [10,20,30]


print(tuple_t[0])

list_t[0] = 1

print(list_t)

tuple_one = (10, ) #하나만 있어도 콤마써야함


[a,b] = [10, 20]
(c,d) = (10, 20)

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

tuple_test = 10, 20, 30, 40
print("#괄호가 없는 듀플의 값과 자료형 출력")
print("tuple_test:", tuple_test)
print("type(tuple_test):", type(tuple_test))
print()

a, b, c =10, 20, 30
print("#괄호가 없는 듀플을 활용한 할당")
print("a:", a)
print("b:", b)
print("c:", c)

a,b = 10, 20

print("#교환 전 값")
print("a:", a)
print("b", b)
print()

a,b = b,a

print("#교환 후 값")
print("a:", a)
print("b", b)
print()

def test():
    return (11,22)
a,b = test()

print("a:", a)
print("b:", b)

def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("한국다람쥐")

call_10_times(print_hello)


def power(item):
    return item*item
def under_3(item):
    return item<3

list_input_a = [1, 2 ,3, 4, 5]

output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))

output_b = filter(under_3, list_input_a)
print("#filter()함수의 실행결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))



power = lambda x: x * x
under_3 = lambda x: x < 3

list_input_a = [1, 2 ,3, 4, 5]

output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))

output_b = filter(under_3, list_input_a)
print("#filter()함수의 실행결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))




list_input_a = [1, 2 ,3, 4, 5]

output_a = map(lambda x: x * x, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))

output_b = filter(lambda x: x < 3, list_input_a)
print("#filter()함수의 실행결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))




file = open("basic.txt", "w")

file.write("한국다람쥐")

file.close()

with open("basic2.txt", "w") as file_2:
    file_2.write("헬로으")

with open("basic.txt", "a") as file:
    file.write("쥐쥐")

with open("basic.txt", "r") as pile:
    con = pile.read()
print(con)


hanguls = list("가나다라마바사아자차카타파하")

with open("info.txt", "w") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        file.write("{},{},{}\n".format(name, weight, height))


with open("info.txt", "r") as file:
    for line in file:
        (name, weight, height) = line.strip().split(",")
        if (not name) or (not weight) or (not height):
            continue
        bmi = int(weight) / ((int(height) / 100) **2)
        result=""
        if 25 <= bmi:
            result ="과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        print('\n'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}"
        ]).format(name, weight, height, bmi, result))
        print()


def test():
    print("함수가 호출되었습니다.")
    yield "test"
print("A지점 통과")
test()

print("B지점 통과")
test()
print(test())




def test():
    print("A지점 통과")
    yield 1
    print("B지점 통과")
    yield 2
    print("C지점 통과")
output = test()

print("D지점 통과")
a = next(output)
print(a)
print("E지점 통과")
b = next(output)
print(b)
print("F지점 통과")
c = next(output)
print(c)
next(output)


