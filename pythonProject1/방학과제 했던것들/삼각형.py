a = int(input("변의 길이"))
b = a
for y in range(b):
    for x in range(a):
        print("*",end='')
    a -= 1
    print()