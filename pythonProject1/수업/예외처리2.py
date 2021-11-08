try:
    n_input_a = int(input("정수입력"))

except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception)



l_n = [ 52, 273, 32, 72, 100]

try:
    n_i = int(input("정수입력"))
    print("{}번째 요소: {}.".format(n_i, l_n[n_i]))
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception)


l_n = [ 52, 273, 32, 72, 100]

try:
    n_i = int(input("정수입력"))
    print("{}번째 요소: {}.".format(n_i, l_n[n_i]))
except ValueError:
    print("정수가 아닙니다")
except IndexError:
    print("리스트의 인덱스를 벗어났습니다")