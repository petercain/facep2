#2단에서 9단까지
for y in range(2,10):
    print("%d단" % y)
    for x in range(1,10):
        print("{} X {} : {}".format(y,  x, y*x))
    print("")

#홀수단짝수
num = int(input("1을 입력하면 홀수단이, 2를 입력하면 짝수단이 출력됩니다 :"))
if(num == 1):
    for y in range(2,10):
        if y%2 == 0:
            continue
        for x in range(1,10):
            print("{} X {} : {}".format(y, x, y * x))
        print("")
elif(num == 2):
    for y in range(2,10):
        if y%2 == 1:
            continue
        for x in range(1,10):
            print("{} X {} : {}".format(y, x, y * x))
        print("")

#입력한 값의 그거만 나오는 구구단

aa = int(input("입력 :"))
for x in range(1,10):
    print("{} X {} : {}".format(aa, x , x * aa))

#구구단이 나오는데 입력한 값의 그거만 안나오는 구구단
vv = int(input("입력 :"))
for y in range(2, 10):
    for x in range(1, 10):
        if vv == x:
            continue
        print("{} X {} : {}".format(y, x, y * x))
    print("")