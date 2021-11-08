price = 0
money = input("돈을 넣어주세요 ")
money = int(money)
while(money == 0):
    money = input("돈을 다시 넣어주세요 ")
    money = int(money)
print("%d원을 넣으셨습니다\n" % money)
order = 0
while(1):
    if order == 0:
        menu = input("""1번 아메리카노 2000원
2번 라떼 2500원
3번 헤이즐넛 2600원
4번 모카 2700원
5번 카라멜 마끼야또 2700원

메뉴를 번호로 선택해주세요.""")
        menu = int(menu)
        if menu == 1:
            ondo = input("아메리카노를 선택하셨습니다.\n핫은 1번, 아이스는 2번입니다. 아이스는 300원 추가입니다.")
            ondo = int(ondo)
            if ondo == 1:
                print("핫을 선택하셨습니다")
                price += 2000
            elif ondo == 2:
                print("아이스를 선택하셨습니다")
                price += 2300
            else:
                print("없는 번호입니다. 다시 선택해주세요")
                menu = 1


        elif menu == 2:
            ondo = input("라떼를 선택하셨습니다.\n핫은 1번, 아이스는 2번입니다. 아이스는 300원 추가입니다.")
            ondo = int(ondo)
            if ondo == 1:
                print("핫을 선택하셨습니다")
                price += 2500
            elif ondo == 2:
                print("아이스를 선택하셨습니다")
                price += 2800
            else:
                print("없는 번호입니다. 다시 선택해주세요")
                menu = 2

        elif menu == 3:
            ondo = input("헤이즐넛을 선택하셨습니다.\n핫은 1번, 아이스는 2번입니다. 아이스는 300원 추가입니다.")
            ondo = int(ondo)
            if ondo == 1:
                print("핫을 선택하셨습니다")
                price += 2600
            elif ondo == 2:
                print("아이스를 선택하셨습니다")
                price += 2900
            else:
                print("없는 번호입니다. 다시 선택해주세요")
                menu = 3

        elif menu == 4:
            ondo = input("모카를 선택하셨습니다.\n핫은 1번, 아이스는 2번입니다. 아이스는 300원 추가입니다.")
            ondo = int(ondo)
            if ondo == 1:
                print("핫을 선택하셨습니다")
                price += 2700
            elif ondo == 2:
                print("아이스를 선택하셨습니다")
                price += 3000
            else:
                print("없는 번호입니다. 다시 선택해주세요")
                menu = 4

        elif menu == 5:
            ondo = input("카라멜 마끼아또를 선택하셨습니다.\n핫은 1번, 아이스는 2번입니다. 아이스는 300원 추가입니다.")
            ondo = int(ondo)
            if ondo == 1:
                print("핫을 선택하셨습니다")
                price += 2700
            elif ondo == 2:
                print("아이스를 선택하셨습니다")
                price += 3000
            else:
                print("없는 번호입니다. 다시 선택해주세요")
                menu = 5

        else:
            print("없는 번호입니다. 다시 선택해주세요")
            order = 0

    else:
        break

    order = input("재주문을 원하시면 0번을, 계산을 원하시면 아무번호나 눌러주세요")
    order = int(order)

if money < price:
    print("요금이 부족합니다. %d원을 반환합니다" % money)
else:
    print("총 가격은 {}원 입니다. 잔돈은 {}입니다.".format(price, money-price))