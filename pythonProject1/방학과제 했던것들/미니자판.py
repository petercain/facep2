money = int(input("돈을 넣어주세요 : "))
while 1:
    if money <= 0:
        money = int(input("돈을 넣어주세요 : "))
    else:
        break
print("%d원을 받았습니다" % money)

dic_m = {
    "환타": 600,
    "사이다": 700,
    "포카리": 800,
    "콜라": 900,
}
print(dic_m)
while 1:
    key = input("메뉴를 고르세요 : ")
    if key in dic_m:
        print("{}가 나옵니다. {}원을 반환합니다.".format(key,money - dic_m[key]))
        break
    else:
        print("없어요. 다시 고르세요.")