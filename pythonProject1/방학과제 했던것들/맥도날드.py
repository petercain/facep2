price = 0
coin = int(input("코인을 넣어주세요 :"))
while(coin == 0):
    coin = int(input("코인을 다시 넣어주세요 :"))

money = coin * 10000
print("{}코인을 넣으셨습니다. {}원이 충전됩니다.".format(coin, money))
time = int(input("현재 몇 시인지 입력해주세요 :"))
time2 = int(input("현재 몇 분인지 입력해주세요 :"))
time3 = time*100 + time2
order = int(input("""햄버거는 1번
디저트는 2번
음료는 3번
사이드는 4번입니다.
06시부터 10시30분까지는 햄거버가 아닌 맥모닝이 제공됩니다.
번호를 선택해주세요 :"""))

while 1:
    if order == 1:
        if 600 <= time3 <= 1030:
            mmo = int(input("맥모닝 타임~\n1번 베이컨 토마토 에그 머핀 4200원\n2번 에그 맥머핀 3200원\n3번 베이컨 에그 맥머핀 3700원\n4번 소시지 에그 맥머핀 3700원\n5번 치킨 치즈 머핀 3900원\n6번 상하이 치킨 스낵랩 2900원\n7번 디럭스 브렉퍼스트 5500원\n8번 핫케익 3조각 3700원\n9번 핫케익 2조각 3000원\n만약 다른 메뉴를 원하시면 지정되지 않은 번호를 눌러주세요\n번호를 선택해주세요 :"))
            if mmo == 1:
                print("베이컨 토마토 에그 머핀")
                price += 4200
            elif mmo == 2:
                print("에그 맥머핀")
                price += 3200
            elif mmo == 3:
                print("베이컨 에그 맥머핀")
                price += 3700
            elif mmo == 4:
                print("소시지 에그 맥머핀")
                price += 3700
            elif mmo == 5:
                print("치킨 치즈 머핀")
                price += 3900
            elif mmo == 6:
                print("상하이 치킨 스낵랩")
                price += 2900
            elif mmo == 7:
                print("디럭스 블랙퍼스트")
                price += 5500
            elif mmo == 8:
                print("핫케잌 3조각")
                price += 3700
            elif mmo == 9:
                print("핫케익 2조각")
                price += 3000
            else:
                order = int(input("햄버거는 1번\n디저트는 2번\n음료는 3번\n사이드는 4번입니다.\n계산을 원하시면 지정되지 않은 아무번호를 눌러주세요.\n번호를 선택해주세요 :"))
        else:
            ham = int(input("햄버거 타임~\n1번 상하이 어니언 버거 5900원\n2번 슈니언 버거 5600원\n3번 트리플 치즈버거 6300원\n4번 더블 블고기 버거 5100원\n5번 빅맥 5300원\n6번 맥스파이시 상하이 버거 5300원\n7번 1955버거6400원\n8번 맥치킨 모짜렐라 5500원\n9번 더블 필레 오 피쉬 5700원\n10번 필레 오 피쉬 4200원\n11번 맥치킨 4000원\n12번 에그 불고기 버거 3900원\n13번 불고기 버거2900원\n14번 슈슈 버거 5200원\n15번 베이컨 토마토 디럭스 6200원\n16번 더블 쿼터파운더 치즈 7700원\n17번 쿼터파운더 치즈 5900원\n18번 치즈버거 3000원\n19번 더블 치즈버거 5100원\n20번 햄버거 2700원\n만약 다른 메뉴를 원하시면 지정되지 않은 번호를 눌러주세요.\n번호를 선택해주세요"))
            if ham == 1:
                print("상하이 어니언 버거")
                price += 5900
            elif ham == 2:
                print("슈니언 버거")
                price += 5600
            elif ham == 3:
                print("트리플 치즈버거")
                price += 6300
            elif ham == 4:
                print("더블 불고기 버거")
                price += 5100
            elif ham == 5:
                print("빅맥")
                price += 5300
            elif ham == 6:
                print("맥스파이시 상하이 버거")
                price += 5300
            elif ham == 7:
                print("1955버거")
                price += 6400
            elif ham == 8:
                print("맥치킨 모짜렐라")
                price += 5500
            elif ham == 9:
                print("더블 필레 오 피쉬 버거")
                price += 5700
            elif ham == 10:
                print("필레 오 피쉬 버거")
                price += 4200
            elif ham == 11:
                print("맥치킨")
                price += 4000
            elif ham == 12:
                print("에그 불고기 버거")
                price += 3900
            elif ham == 13:
                print("불고기 버거")
                price += 2900
            elif ham == 14:
                print("슈슈 버거")
                price += 5200
            elif ham == 15:
                print("베이컨 토마토 디럭스")
                price += 6200
            elif ham == 16:
                print("더블 쿼터파운더 치즈")
                price += 7700
            elif ham == 17:
                print("쿼터파운더 치즈")
                price += 5900
            elif ham == 18:
                print("치즈버거")
                price += 3000
            elif ham == 19:
                print("더블 치즈버거")
                price += 5100
            elif ham == 20:
                print("햄버거")
                price += 2700
            else:
                order = int(input("햄버거는 1번\n디저트는 2번\n음료는 3번\n사이드는 4번입니다.\n계산을 원하시면 지정되지 않은 아무번호를 눌러주세요.\n번호를 선택해주세요 :"))
    elif order == 3:
        ju = int(input("음료수 코너입니다.\n1번 커피쉐이크 3200원\n2번 제주 한라봉 칠러 3400원\n3번애플망고 칠러 3400원\n4번 배칠러 3400원\n5번 까페라떼 3400원\n6번 카푸치노 3400원\n7번 아메리카노 2900원\n8번 에스프레소 2200원\n9번 드립 커피 2200원\n10번 아이스 카페라떼 3400원\n11번 아이스 아메리카라노 2900원\n12번 아이스 드립 커피 1700원\n13번 코카콜라 2100원\n14번 코카콜라제로 2100원\n15번 스프라이트 2100원\n16번 환타 2100원\n만약 다른 메뉴를 원하시면 지정되지 않은 번호를 눌러주세요.\n번호를 선택해주세요"))
        if ju == 1:
            print("커피쉐이크")
            price += 3200
        elif ju == 2:
            print("제주 한라봉 칠러")
            price += 3400
        elif ju == 3:
            print("애플 망고 칠러")
            price += 3400
        elif ju == 4:
            print("배칠러")
            price +=  3400
        elif ju == 5:
            print("까페라뗴")
            price += 3400
        elif ju == 6:
            print("카푸치노")
            price += 3400
        elif ju == 7:
            print("아메리카노")
            price += 2900
        elif ju == 8:
            print("에스프레소")
            price += 2200
        elif ju == 9:
            print("드립 커피")
            price += 2200
        elif ju == 10:
            print("아이스 까페라뗴")
            price += 3400
        elif ju == 11:
            print("아이스 아메리카노")
            price += 2900
        elif ju == 12:
            print("아이스 드립 커피")
            price += 1700
        elif ju == 13:
            print("코카콜라")
            price += 2100
        elif ju == 14:
            print("코카콜라제로")
            price += 2100
        elif ju == 15:
            print("스프라이트")
            price += 2100
        elif ju == 16:
            print("환타")
            price += 2100
        else:
            order = int(input("햄버거는 1번\n디저트는 2번\n음료는 3번\n사이드는 4번입니다.\n계산을 원하시면 지정되지 않은 아무번호를 눌러주세요.\n번호를 선택해주세요 :"))
    elif order == 2:
        de = int(input("디저트 메뉴 입니다. \n1번 커피쉐이크 3200원\n2번 오레오 맥플러리3200원\n3번 베리스트로베리 맥플러리 3200원\n4번 제주 한라봉 칠러 3400원\n5번 애플망고 칠러 3400원\n6번 배칠러 3400원\n7번 애플파이 1900원\n8번 초코 선데이 아이스크림 2200원\n9번 딸기선데이 아이스크림 2200원\n10번 바닐라 선데이 아이스크림 2200원\n11번 바닐라쉐이크 3200원\n12번 딸기쉐이크 3200원\n13번 초코쉐이크 3200원\n만약 다른 메뉴를 원하시면 지정되지 않은 번호를 눌러주세요.\n번호를 선택해주세요"))
        if de == 1:
            print("커피쉐이크")
            price += 3200
        elif de == 2:
            print("오레오 맥플러")
            price += 3200
        elif de == 3:
            print("베리스트로베리 맥플러리")
            price += 3200
        elif de == 4:
            print("제주 한라봉 칠러")
            price += 3400
        elif de == 5:
            print("애플망고 칠러")
            price += 3400
        elif de == 6:
            print("배칠러")
            price += 3400
        elif de == 7:
            print("애플파이")
            price += 1900
        elif de == 8:
            print("초코 선데이 아이스크림")
            price += 2200
        elif de == 9:
            print("딸기 선데이 아이스크림")
            price += 2200
        elif de == 10:
            print("바닐라 선데이 아이스크림")
            price += 3200
        elif de == 11:
            print("바닐라쉐이크")
            price += 3200
        elif de == 12:
            print("딸기 쉐이크")
            price += 3200
        elif de == 13:
            print("초코쉐이크")
            price += 3200
        else:
            order = int(input("햄버거는 1번\n디저트는 2번\n음료는 3번\n사이드는 4번입니다.\n계산을 원하시면 지정되지 않은 아무번호를 눌러주세요.\n번호를 선택해주세요 :"))
    elif order == 4:
        side = int(input("1번 lck 레전드 스낵팩 12000원\n2번 맥윙 1인팩-치즈스틱 6500원\n3번 맥윙 1인팩 - 웨지 후라이 6500원\n4번 맥윙 2인팩 10900원\n5번 웨지 후라이 2900원\n6번 맥윙 2조각 3400원\n7번 골드 모짜렐라 치즈스틱 2조각 2900원\n8번 맥너겟 10조각 5200원\n9번 애플 파이 1900원\n만약 다른 메뉴를 원하시면 지정되지 않은 번호를 눌러주세요.\n번호를 선택해주세요 :"))
        if side == 1:
            print("lck 레전드 스낵백")
            price += 12000
        elif side == 2:
            print("맥윙 1인팩 - 치즈스틱")
            price += 6500
        elif side == 3:
            print("맥윙 1인팩 - 웨지 후라이")
            price += 6500
        elif side == 4:
            print("맥윙 2인팩")
            price += 10900
        elif side == 5:
            print("웨지 후라이")
            price += 2900
        elif side == 6:
            print("맥윙 2조각")
            price += 3400
        elif side == 7:
            print("골드 모짜렐라 치즈스틱 2조각")
            price += 2900
        elif side == 8:
            print("맥너겟 10조각")
            price += 5200
        elif side == 9:
            print("애플파이")
            price += 1900
        else:
            order = int(input("햄버거는 1번\n디저트는 2번\n음료는 3번\n사이드는 4번입니다.\n계산을 원하시면 지정되지 않은 아무번호를 눌러주세요.\n번호를 선택해주세요 :"))
    else:
        break
    order = int(input("햄버거는 1번\n디저트는 2번\n음료는 3번\n사이드는 4번입니다.\n계산을 원하시면 지정되지 않은 아무번호를 눌러주세요.\n번호를 선택해주세요 :"))
if money - price >= 0:
    print("계산 금액은 총 %d입니다. 잔돈 %d원을 반환합니다" % (price, money - price))
else:
    print("금액이 부족합니다. 코인 %d개를 반환합니다." % coin)