from random import*
pika = 500
i = 0
while 1:
    if pika == 500:
        mon = int(random() * 5)

        if mon == 0:
            print("야생의 이브이가 나타났다!!")
            enemy = randint(100,450)
            i += 1
            while 1:
                pa = randint(1,150)
                ea = randint(1,150)

                print("피카츄의 백만볼트! %d의 데미지!" % pa)
                print("이브이의 브이브이브레이크! %d의 데미지!" % ea)
                pika = pika - ea
                enemy = enemy -pa
                print("피카츄는 {}의 데미지를 받았다! 남은 체력은 {}!".format(ea, pika))
                print("이브이는 {}의 데미지를 받았다! 남은 체력은 {}!".format(pa,enemy))
                if pika <= 0:
                    print("\n피카츄는 쓰려졌다...\n")
                    mon = 6
                    break
                elif enemy <= 0:
                    print("\n피카츄의 승리!!\n")
                    pika = 500
                    break
        elif mon == 1:
            print("야생의 야도란이 나타났다!!")
            enemy = randint(100,450)
            i += 1
            while 1:
                pa = randint(1,150)
                ea = randint(1,150)

                print("피카츄의 백만볼트! %d의 데미지!" % pa)
                print("야도란의 사이코키네시스! %d의 데미지!" % ea)
                pika = pika - ea
                enemy = enemy -pa
                print("피카츄는 {}의 데미지를 받았다! 남은 체력은 {}!".format(ea, pika))
                print("야도란은 {}의 데미지를 받았다! 남은 체력은 {}!".format(pa,enemy))
                if pika <= 0:
                    print("\n피카츄는 쓰려졌다...\n")
                    mon = 6
                    break
                elif enemy <= 0:
                    print("\n피카츄의 승리!!\n")
                    pika = 500
                    break

        elif mon == 2:
            print("야생의 파이리가 나타났다!!")
            enemy = randint(100,450)
            i += 1
            while 1:
                pa = randint(1,150)
                ea = randint(1,150)

                print("피카츄의 백만볼트! %d의 데미지!" % pa)
                print("파이리의 불대문자! %d의 데미지!" % ea)
                pika = pika - ea
                enemy = enemy -pa
                print("피카츄는 {}의 데미지를 받았다! 남은 체력은 {}!".format(ea, pika))
                print("파이리는 {}의 데미지를 받았다! 남은 체력은 {}!".format(pa,enemy))
                if pika <= 0:
                    print("\n피카츄는 쓰려졌다...\n")
                    mon = 6
                    break
                elif enemy <= 0:
                    print("\n피카츄의 승리!!\n")
                    pika = 500
                    break

        elif mon == 3:
            print("야생의 버터플가 나타났다!!")
            enemy = randint(100,450)
            i += 1
            while 1:
                pa = randint(1,150)
                ea = randint(1,150)

                print("피카츄의 백만볼트! %d의 데미지!" % pa)
                print("버터플의 벌레의야단법석! %d의 데미지!" % ea)
                pika = pika - ea
                enemy = enemy -pa
                print("피카츄는 {}의 데미지를 받았다! 남은 체력은 {}!".format(ea, pika))
                print("버터플은 {}의 데미지를 받았다! 남은 체력은 {}!".format(pa,enemy))
                if pika <= 0:
                    print("\n피카츄는 쓰려졌다...\n")
                    mon = 6
                    break
                elif enemy <= 0:
                    print("\n피카츄의 승리!!\n")
                    pika = 500
                    break

        elif mon == 4:
            print("야생의 꼬부기가 나타났다!!")
            enemy = randint(100,450)
            i += 1
            while 1:
                pa = randint(1,150)
                ea = randint(1,150)

                print("피카츄의 백만볼트! %d의 데미지!" % pa)
                print("꼬부기의 물대포! %d의 데미지!" % ea)
                pika = pika - ea
                enemy = enemy -pa
                print("피카츄는 {}의 데미지를 받았다! 남은 체력은 {}!".format(ea, pika))
                print("꼬부기는 {}의 데미지를 받았다! 남은 체력은 {}!".format(pa,enemy))
                if pika <= 0:
                    print("\n피카츄는 쓰려졌다...\n")
                    mon = 6
                    break
                elif enemy <= 0:
                    print("\n피카츄의 승리!!\n")
                    pika = 500
                    break

        elif mon == 6:
            break

    else:
        break

print("\n\n끝! 피카츄는 %d턴 동안 싸웠다" % i)