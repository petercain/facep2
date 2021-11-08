import random
import time
import pickle
number0 = 0
MP = {1 : '피카츄', 2 : '파이리' , 3 : '꼬부기' , 4 : '이상해씨'}
EP = ['구구', '꼬렛', '꼬리선', '모다피', '주벳', '잉어킹']
save = {}
user = "  "
prompt0 = ("""1. 새로시작
2. 이어하기(미구현)
3. 종료""")
prompt1 = ("""
1. 포켓몬선택
2. 모험시작
3. 저장(종료)(미구현)""")
prompt2 = ("1. 싸운다 2. 포켓몬상태 3. 도망간다")
prompt3 = ("1. 공격 2. 포션 3. 도망간다")
prompt4 = ("무엇을 할까?\n1. 모험을떠난다 2. 포켓몬센터로간다 3. 레포트를 작성한다")
while number0 !=3:
    print(prompt0)
    number0 = int(input("숫자로 입력해주세요\n>>>"))
    if number0 == 1:
        number1 = 0
        while number1 != 3:
            Lvl = 1
            Bhp = 500
            GP = []
            print(prompt1)
            number1 = int(input("숫자로 입력해주세요\n>>>"))
            if number1 == 1:
                print("너는 누구니?")
                user = input("이름을 입력해주세요")
                print("이야- 오래 기다리게 했다!\n포켓몬스터의 세계에 잘왔단다!")
                time.sleep(0.5)
                print("나의 이름은 오박사\n모두로부터는 포켓몬박사라고 존경받고 있단다.")
                print("포켓몬스터.........포켓몬")
                time.sleep(0.5)
                print("이 세계에는 포켓몬스터라고 불려지는 생명체들이\n도처에 살고있다! [마릴~]")
                time.sleep(0.5)
                print("사람은 포켓몬들과 정답게 지내거나 함께 싸우거나........")
                time.sleep(0.5),
                print("""서로 도와가며 살아가고 있단다
하지만 우리들은 포켓몬 전부를 알고 있지는 못하다
포켓몬의 비밀은 아직도 잔뜩 있다!""")
                time.sleep(0.5)
                print("나는 그것을 밝혀내기 위하여 매일 포켓몬의 연구를 계속 하고 있다는 말이다!")
                time.sleep(0.5)
                print("바깥은 위험하니 이 아이들중 하나를 데려가렴!!")
                print(MP)
                a = int(input("숫자로 입력해주세요\n>>>"))
                if a == 1:
                    print("피카츄를 골랐구나!")
                    print(user, MP[a], "을(를) 잘부탁한다!")
                    GP.append(MP[a])
                    print("피카츄~")
                elif a == 2:
                    print("파이리를 골랐구나!")
                    print(user, MP[a], "을(를) 잘부탁한다!")
                    GP.append(MP[a])
                    print("파이~")
                elif a == 3:
                    print("꼬부기를 골랐구나!")
                    print(user, MP[a], "을(를) 잘부탁한다!")
                    GP.append(MP[a])
                    print("꼬북 꼬북!")
                elif a == 4:
                    print("이상해씨를 골랐구나!")
                    print(user, MP[a], "을(를) 잘부탁한다!")
                    GP.append(MP[a])
                    print("씨~ 씨~")
            if number1 == 2:
                print("모험을 시작합니다")
                print("밖은 위험하니 포션을 5개 챙겨주마!")
                portion = 5
                numbera = 0
                MPHp = 500
                EPHp = 500
                Mid = 100
                Mad = 200
                MPBa = random.randint(Mid, Mad)
                EPBa = random.randint(int(Mid * 9 / 10), int(Mad * 9 / 10))
                Lvl = 1
                while True :
                    print(prompt4)
                    numbera = int(input("숫자로 입력해주세요\n>>>"))
                    EPHp1 = EPHp
                    MPHp1 = MPHp
                    Mid1 = Mid
                    Mad1 = Mad
                    MPBa1 = MPBa
                    EPBa1 =EPBa
                    if numbera == 1:
                        EPn = EP[random.randrange(0,len(EP))]
                        print("앗 야생의", EPn, "을(를) 만났다!!")
                        print(user, "은(는) 무엇을 할까?")
                        number2 = 0
                        while number2 != 3:
                            print(prompt2)
                            number2 = int(input("숫자로 입력해주세요\n>>>"))
                            if number2 == 1:
                                print("Lv", Lvl, EPn, "체력", EPHp1, "공격력", int(Mid * 9 / 10), "~", int(Mad * 9 / 10))
                                while True :
                                    print(prompt3)
                                    number3 = int(input("숫자로 입력해주세요\n>>>"))
                                    if number3 == 1:
                                        Fn = random.randrange(0,2)
                                        if Fn == 0:
                                            EPHp1 -= MPBa
                                            if 0 < EPHp1:
                                                print(MP[a], "이(가) 공격합니다!\n", MPBa, "의 데미지를 주었습니다.\n", EPn, "의 체력이", EPHp1, "남았습니다!")
                                            elif EPHp1 <= 0:
                                                print(MP[a], "이(가) 공격합니다!\n", MPBa, "의 데미지를 주었습니다.\n", EPn, "의 체력이", 0, "남았습니다!")
                                                Lvl += 1
                                                MPHp += int(Bhp * (random.randint(5, 10) / 100))
                                                EPHp += int(Bhp * (random.randint(5, 10) / 100) * 7 / 10)
                                                Mid += int(Mid * random.randint(5, 10) / 100)
                                                Mad += int(Mid * (random.randint(5, 10) / 100))
                                                print(MP[a], "(이)가 승리했습니다\n남은체력", MPHp1, "\n레벨이 오릅니다.", Lvl-1, "->", Lvl)
                                                Pn = random.randrange(0, 2)
                                                if Pn == 0:
                                                    portion += 1
                                                    print("포션을 획득했습니다!", portion)
                                                    save[user] = [GP, Lvl, portion, MPHp, Mid, Mad]
                                                elif Pn == 0:
                                                    save[user] = [GP, Lvl, portion, MPHp, Mid, Mad]
                                                    pass
                                                break
                                        elif Fn == 1:
                                            MPHp1 -= EPBa
                                            if 0 < MPHp1:
                                                print(EPn, "이(가) 공격합니다!\n", EPBa, "의 데미지를 주었습니다.\n", MP[a], "의 체력이", MPHp1, "남았습니다!")
                                            if MPHp1 <= 0:
                                                print(EPn, "이(가) 공격합니다!\n", EPBa, "의 데미지를 주었습니다.\n", MP[a], "의 체력이", 0, "남았습니다!")
                                                Lvl -= 1
                                                MPHp -= int(Bhp * (random.randint(5, 10) / 100))
                                                EPHp -= int(Bhp * (random.randint(5, 10) / 100) * 7 / 10)
                                                Mid -= int(Mid * random.randint(5, 10) / 100)
                                                Mad -= int(Mid * (random.randint(5, 10) / 100))
                                                print(EPn, "(이)가 승리했습니다\n남은체력", EPHp1, "\n레벨이 떨어집니다", Lvl+1, "->", Lvl, user, "(은)는 눈앞이 깜깜해졌다.")
                                                save[user] = [GP, Lvl, portion, MPHp, Mid, Mad]
                                                break
                                    elif number3 == 2:
                                        if portion > 0:
                                            number4 = 0
                                            while number4 != 2:
                                                print("포션이", portion, "개 있습니다.\n포션을 마시겠습니까?")
                                                number4 = int(input("1.예 2.아니오"))
                                                if number4 == 1:
                                                    if MPHp <= MPHp1 + 300:
                                                        print(MP[a], "이(가) 체력을", MPHp1 + 300 - MPHp, "회복합니다", "포션이", portion - 1, "개 있습니다.")
                                                        MPHp1 = MPHp
                                                        print("현재체력", MPHp1)
                                                        portion -= 1
                                                    else :
                                                        print(MP[a], "이(가) 체력을 300 회복합니다", "포션이", portion - 1, "개 있습니다.")
                                                        MPHp1 += 300
                                                        print("현재체력", MPHp1)
                                                        portion -= 1
                                                    if portion == 0:
                                                        print("포션을 모두 사용했습니다.")
                                                        break
                                                elif number4 == 2:
                                                    print("전투로 돌아갑니다")
                                                else:
                                                    print("다시입력해주세요")
                                                    continue
                                        elif portion == 0:
                                            print("현재 보유중인 포션이 없습니다.")
                                    elif number3 == 3:
                                        print("도망치겠습니까?")
                                        break
                                    else:
                                        print("다시입력해주세요")
                                        continue
                                break
                            elif number2 == 2:
                                print(MP[a], "의 상태를 보여줍니다")
                                print("Lv", Lvl, MP[a], "체력", MPHp1, "공격력", Mid,"~",Mad)
                            elif number2 == 3:
                                print(user, "은(는) 도망쳤습니다")
                                break
                            else:
                                print("다시입력해주세요")
                                continue
                    elif numbera == 2:
                        MPHp1 = MPHp
                        print(MP[a], "의 체력이 모두 회복되었습니다.")
                        print(MPHp1)
                        continue
                    elif numbera == 3:
                        print("레포트 작성 후 종료합니다")
                        # with open("pokuser.pickle", "wb") as fw:
                        #     pickle.dump(save, fw)

                        break
                    else:
                        print("다시입력해주세요")
                        continue
            elif number1 == 2:
                pass

            else:
                print("다시입력해주세요")
                continue
    elif number0 == 2:
        pass

    elif number0 == 3:
        print("게임을 종료합니다")
    else:
        print("다시입력해주세요")
        continue