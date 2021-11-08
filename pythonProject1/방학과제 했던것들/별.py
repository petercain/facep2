a = 7
b = 7

for y in range(3):
    for x in range(15):
        if a <= x <= b:
            print("*", end='')
            continue
        print(" ",end='')
    a -= 1
    b += 1
    print()

a = 0
b = 14

for y in range(3):
    for x in range(15):
        if a <= x <= b:
            print("*", end='')
            continue
        print(" ", end='')
    a += 1
    b -= 1
    print()

a = 2
b = 12

for y in range(3):
    for x in range(15):
        if a <= x <= b:
            print("*", end='')
            continue
        print(" ",end='')
    a -= 1
    b += 1
    print()

a = 5
b = 9

for y in range(3):
    for x in range(15):
        if a <= x <= b:
            print("*", end='')
            continue
        print(" ", end='')
    a += 1
    b -= 1
    print()