import pymysql

#런던
conn = pymysql.connect(host='10.10.21.111', port=3306, user='dhqudtn', password='1234',
                             db='starDB', charset='utf8')
cur = conn.cursor()


cur.execute('SELECT * FROM Order_data_London')

result = cur.fetchall()

for res in result:
    print(res)

conn.commit()
conn.close()

# 본사
conn = pymysql.connect(host='10.10.21.118', port=3306, user='London', password='starDB1234@',
                             db='starDB', charset='utf8')

cur = conn.cursor()


cur.execute('SELECT * FROM Head')

result = cur.fetchall()

for res in result:
    print(res)

conn.commit()
conn.close()