import sqlite3
import random
import pymysql



cof = ["아메리카노","까페라떼","카라멜 마끼아또","까페모카","헤이즐넛","까푸치노"]


#si는 '시' 입니다.
#bun은 '분'입니다
si = ["09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]
bun = ["01", "02", "03", "04", "05", "06", "07", "08", "09","10"]
for i in range(50):
    i += 11
    i = str(i)
    bun.append(i)

#일만 있는 리스트인데 다른 일도 넣고 싶으면 다른 일 추가하시면 됩니다.
nal = ["01", "02", "03", "04", "05", "06", "07", "08", "09",'10', '11', '12', '13','14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29','30','31']


connection = pymysql.connect(host='10.10.21.111', port=3306, user='dhqudtn', password='1234',
                             db='starDB', charset='utf8')
cursor = connection.cursor()

#range(반복횟수)
for kk in range(500):
    Y = random.choice(nal)
    X = "2021-08-{}".format(Y)
    S = random.choice(si)
    Z = random.choice(bun)
    TI = "{}:{}".format(S, Z)
    cc = random.choice(cof)
    dum = "김더미"
    point = "런던본점"

    if cc == "아메리카노":
        bb = 2000
    elif cc == "까페라떼":
        bb = 2500
    elif cc == "카라멜 마끼아또":
        bb = 2700
    elif cc == "까페모카":
        bb = 2700
    elif cc == "헤이즐넛":
        bb = 2600
    elif cc == "까푸치노":
        bb = 2900

    cursor.execute("INSERT INTO Order_data_London VALUES ('{}','{}','{}','{}','{}','{}')".format(dum,cc,bb,X,TI,point))

connection.commit()
connection.close()
