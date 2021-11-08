from random import*
stviewers = 0
subers = 0
name = input("유튜브 채널의 이름을 입력해주세요")

for y in range(20):
    con = input("오늘의 컨텐츠를 입력해주세요")
    for x in range(10):
        viewers = randint(50, 2500)
        stviewers = stviewers + viewers
        print("현재 시청자 수 :", stviewers)
    disub = randint(1, 5)
    subers = subers + stviewers//disub
    print("오늘 {}로 인한 구독자 상승 : {}".format(con, stviewers//disub))
    stviewers = 0
    print("현재 구독자 : {}".format(subers))

if subers >= 100000:
    print("{}(은)는 실버 버튼을 받았습니다!!".format(name))
else:
    print("{}(은)는 폭파되었습니다..구독자 여러분 죄송합니다ㅠㅠ".format(name))