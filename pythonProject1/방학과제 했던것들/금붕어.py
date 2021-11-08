from random import*

ryu = input("금붕어의 애칭을 정해주세요")
ryul = input("{}의 짝궁의 애칭을 정해주세요".format(ryu))

gf = 2
i = 0
mom = 1

while 1:
    if 0 < gf <= 1000:
        for x in range(mom):
            baby = randint(1,5)
            gf = gf + baby*2
        i = i + 10
        print("현재 금붕어의 수 : {}\n지난 시간 {}초".format(gf,i))
        die = randint(1,5)
        if i > 10:
            gf = gf - die*2
            print("금붕어가 {}마리가 죽었습니다".format(die*2))
        mom = gf//2

    else:
        break
if gf>=1000:
    print("위대한 선조 {}와(과) {}은(는) 그들의 자손 {}마리와 함께 {}초만에 정복했습니다".format(ryu,ryul,gf,i))
elif gf < 0:
    print("{}와(과){}의 어항은 멸망했습니다".format(ryu, ryul))