import pymysql

#접속
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0623',
                             db='rotk', charset='utf8')

#커서 가져오기(연결할 DB와 상화작용하기 위해서 cursor 객체 생성필요)
cursor = connection.cursor()

#SQL문 만들기
sql = 'SELECT * FROM chok'
cursor.execute(sql) #sql문 실행

result = cursor.fetchall()

for res in result:
    print(res)

connection.close()

#sql라이트는 개인이 사용
#마리아db서버에 다른 사람이 접근해서 볼수있음, 그래서 마리아db 서버라고 부름.
#ip와 prot의 개념
#ip : 컴퓨터의 주소같은 것. 데이터 전송시에 씀.
#port : 어떤 프로그램을 보낼지는 모르니까, ip로 컴퓨터 찾고 컴퓨터 내에서 port로 판별

connection = pymysql.connect(host='', port=3306, user='root',
                             db='starDB', charset='utf8')

#커서 가져오기(연결할 DB와 상화작용하기 위해서 cursor 객체 생성필요)
cursor = connection.cursor()

#SQL문 만들기
sql = 'UPDATE jochanigtable SET NICKNAME = "Dorothy" WHERE NAME = "김승미"'
cursor.execute(sql) #sql문 실행

result = cursor.fetchall()

for res in result:
    print(res)

connection.commit()
connection.close()