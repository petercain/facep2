import datetime
#
# try:
#     number_input = int(input("정수를 입력해주세여"))
#     print("{}".format(number_input))
#
# except Exception as exception:
#     file = open("log.txt", "w")
#     file.write("발생시간 : {}\n오류명 : {}".format(datetime.datetime.now(), type(exception)))
# finally:
#     try:
#         file.close()
#     except:
#         pass
# #에러가 없으면 file이 생성되지 않기때문에 file이 꺼질 수 가 없어서 오류가 남.


#정수 입력을 받으면 출력되고 아니면 오류가 파일에 저장되는 함수?
def ex(value):
    try:
        value = int(value)
        print("{}".format(value))

    except Exception as exception:
        file = open("log.txt", "a")
        file.write("발생시간 : {}\n오류명 : {}\n".format(datetime.datetime.now(), type(exception)))
        print("에러발생")
    finally:
        try:
            file.close()
        except:
            pass
        # 에러가 없으면 file이 생성되지 않기때문에 file이 꺼질 수 가 없어서 오류가 남.

n = input("정수를 입력해주세여")
ex(n)