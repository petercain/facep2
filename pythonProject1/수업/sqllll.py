import sqlite3

conn = sqlite3.connect("ex0819ver2.db", isolation_level= None) # autocommit

conn.row_factory = sqlite3.Row #sql3의 내장함수를 쓸수 있게 해줌

cur = conn.cursor()
input_name = 'AL'

    #input("검색할 이름을 입력해주세요\n")

cur.execute("SELECT * FROM EMP WHERE ENAME like '%{}%'".format(input_name)) #실핼할 sql 문

result = cur.fetchall() #튜플로 이루어진 리스트 #조회한 결과에 한 ROW는 TUPLE이고 전체결과는 리스트이다.

#dic_result = dict(result)  #내장함수인 dict을 만나서 딕셔너리 형식으로 변신

#print(dic_result['ENAME'], dic_result['SAL'])

for row in result:
    dic_result = dict(row)
    print(dic_result['ENAME'])
    if row['ENAME'] == "ALLEN":
        print("ALLEN이 맞습니다.")