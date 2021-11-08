import random
#1번과 11번이 없는 번호버전입니다
AI2 = [2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23]

for i in range(3):
    X = random.choice(AI2)
    print(X)
    AI2.remove(X)
for l in range(2):
    X = random.choice(AI2)
    print(X)
    AI2.remove(X)
