a = 0
b = 17

for y in range(9):
    for x in range(18):
        if a <= x <=8:
            print("*", end='')
            continue
        elif b <= x <= 17:
            print("*", end='')
            continue
        print(" ",end='')
    a += 1
    b -= 1
    print()

a = 8
b = 9
for y in range(9):
    for x in range(18):
        if 0 <= x <= a:
            print("*", end='')
            continue
        elif 9 <= x <= b:
            print("*", end='')
            continue
        print(" ", end='')
    a -= 1
    b += 1
    print()