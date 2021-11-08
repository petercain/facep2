try:
    n = int(input("숫자"))
    print(n)
except:
    print("?")

list_input_a = ["52", "273", "32", "스파이", "103"]

list_number =[]
for item in list_input_a:

    try:
        float(item)
        list_number.append(item)
    except:
        pass

print("{}내부에 있는 숫자는".format(list_input_a))
print("{}입니다".format(list_number))



try:
    n_input_a = int(input("정수입력"))
    print(n_input_a)
except:
    print("정수요...")
else:
    print("예외가 발생하지 않았습니다")
finally:
    print("아무튼 끝")

#리턴, 반목문 브레이크를 만나도 끄덕없는 파이널리