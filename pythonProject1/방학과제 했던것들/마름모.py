i = int(input("마름모 가운데의 길이를 입력하세요"))
imid= i//2 +1
imin = imid
imax = imid


for y in range(imid):
    for x in range(i+1):
        if(x >= imin and x<= imax):
            print("*",end='')
            continue
        print(" ",end='')
    imin -= 1
    imax += 1
    print()

imin = 2
imax = i
for y in range(imid - 1):
    for x in range(i):
        if imin <= x <= imax-1:
            print("*", end='')
            continue
        print(" ", end='')
    imin += 1
    imax -= 1
    print()

