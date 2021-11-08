a = 1
b = 6
list_all = []
for y in range(5):
    list_1 =[x for x in range(a,b)]
    list_all.append(list_1)
    a += 5
    b += 5

print(list_all)

a=21
b=16
c=11
d=6
e=1
list_all2 = []
for i in range(5):
    list_a = [a, b, c, d, e]
    list_all2.append(list_a)
    a += 1
    b += 1
    c += 1
    d += 1
    e += 1
print(list_all2)

a = 21
b = 26
list_all = []
for y in range(5):
    list_1 =[x for x in range(a,b)]
    list_2 = reversed(list_1)
    list_all.append(list(list_2))
    a -= 5
    b -= 5

print(list_all)
