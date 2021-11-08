#문제 1.
#SELECT * FROM HOSPITAL_INFO WHERE CITY like "광주%"

#문제2.
#SELECT * FROM HOSPITAL_INFO WHERE DEPARTMENT_COUNT >= 10 AND BED_COUNT >= 100

#문제3.
#SELECT name, max(DEPARTMENT_COUNT) FROM HOSPITAL_INFO
#SELECT name, max(BED_COUNT) FROM HOSPITAL_INFO

#문제4.
#SELECT * FROM HOSPITAL_INFO WHERE CITY like "제주%" AND BED_COUNT >= 300 AND InfectiousDiseasesAgency ="Y"

#문제5.
#SELECT * FROM HOSPITAL_INFO WHERE NAME like "%외과%"


#문제6.
#SELECT sum(BED_COUNT) FROM HOSPITAL_INFO WHERE CITY like "대구%"

#문제7.
#SELECT avg(BED_COUNT) FROM HOSPITAL_INFO WHERE CITY like "서울%"

#문제8.
#SELECT city, count(*) FROM COVID_TEST_ROOM GROUP BY city ORDER BY count(city) DESC LIMIT 1

#문제9.
#SELECT ADDRESS, CONTACT FROM COVID_TEST_ROOM WHERE CITY = "울산시 북구" AND NOT TIME_WEEKEND = "미운영"

#문제10.
#SELECT name FROM COVID_TEST_ROOM WHERE NAME = PUBLIC_HEALTH AND TIME_HOLIDAY ="미운영"

#문제11.
# SELECT Students_info.Name, COVID_TEST_ROOM.name FROM Students_info
# inner join COVID_TEST_ROOM
# on Students_info.City = COVID_TEST_ROOM.CITY_1 WHERE Students_info.Name = "오병수"


#12.3조 사람들이 갈 수 있는 국가보훈병원이면서 선별 진료소인 곳
# SELECT Students_info.Name, COVID_TEST_ROOM.name, HOSPITAL_INFO.NAME
# FROM Students_info
# inner join COVID_TEST_ROOM
# on HOSPITAL_INFO.NAME = COVID_TEST_ROOM.Name
# INNER JOIN HOSPITAL_INFO
# on HOSPITAL_INFO.NAME = COVID_TEST_ROOM.Name
# WHERE Students_info.Department = 3 AND Students_info.city = COVID_TEST_ROOM.CITY_1

#13. 병상수가 가장 많은 도시에 사는 학생을 찾으세요
#일단 병상은 찾음 SELECT City, sum(BED_COUNT) FROM HOSPITAL_INFO GROUP BY city ORDER BY count(city) DESC LIMIT 1

#14. 공휴일에 운영을 하고, 진료과목이 15개 이상인 병원들의 수가 많은 조


import sqlite3

conn = sqlite3.connect("Covid_Hospital_ver2.db")
cur = conn.cursor()

cur.execute("SELECT * FROM HOSPITAL_INFO WHERE CITY like '광주%'")
sqloutput = cur.fetchall()
print("1번")
print(sqloutput)

cur.execute("SELECT * FROM HOSPITAL_INFO WHERE DEPARTMENT_COUNT > 10 AND BED_COUNT > 100")
sqloutput = cur.fetchall()
print("2번")
print(sqloutput)

cur.execute("SELECT name, max(DEPARTMENT_COUNT) FROM HOSPITAL_INFO")
sqloutput = cur.fetchall()
print("3번-1")
print(sqloutput)

cur.execute("SELECT name, max(BED_COUNT) FROM HOSPITAL_INFO")
sqloutput = cur.fetchall()
print("3번-2")
print(sqloutput)

cur.execute("SELECT * FROM HOSPITAL_INFO WHERE CITY like '제주%' AND BED_COUNT >= 300 AND InfectiousDiseasesAgency ='Y'")
sqloutput = cur.fetchall()
print("4번")
print(sqloutput)

cur.execute("SELECT * FROM HOSPITAL_INFO WHERE NAME like '%외과%'")
sqloutput = cur.fetchall()
print("5번")
print(sqloutput)

cur.execute("SELECT sum(BED_COUNT) FROM HOSPITAL_INFO WHERE CITY like '대구%'")
sqloutput = cur.fetchall()
print("6번")
print(sqloutput)

cur.execute('SELECT avg(BED_COUNT) FROM HOSPITAL_INFO WHERE CITY like "서울%"')
sqloutput = cur.fetchall()
print("7번")
print(sqloutput)

cur.execute('SELECT city, count(*) FROM COVID_TEST_ROOM GROUP BY city ORDER BY count(city) DESC LIMIT 1')
sqloutput = cur.fetchall()
print("8번")
print(sqloutput)

cur.execute("SELECT ADDRESS, CONTACT FROM COVID_TEST_ROOM WHERE CITY = '울산시 북구' AND NOT TIME_WEEKEND = '미운영'")
sqloutput = cur.fetchall()
print("9번")
print(sqloutput)

cur.execute("SELECT name FROM COVID_TEST_ROOM WHERE NAME = PUBLIC_HEALTH AND TIME_HOLIDAY ='미운영'")
sqloutput = cur.fetchall()
print("10번")
print(sqloutput)

cur.execute('SELECT Students_info.Name, COVID_TEST_ROOM.name FROM Students_info inner join COVID_TEST_ROOM on Students_info.City = COVID_TEST_ROOM.CITY_1 WHERE Students_info.Name = "오병수"')
sqloutput = cur.fetchall()
print("11번")
print(sqloutput)

cur.execute("SELECT Students_info.Name, COVID_TEST_ROOM.name, HOSPITAL_INFO.NAME \
FROM Students_info \
inner join COVID_TEST_ROOM \
on HOSPITAL_INFO.NAME = COVID_TEST_ROOM.Name \
INNER JOIN HOSPITAL_INFO \
on HOSPITAL_INFO.NAME = COVID_TEST_ROOM.Name \
WHERE Students_info.Department = 3 AND Students_info.city = COVID_TEST_ROOM.CITY_1")
sqloutput = cur.fetchall()
print("12번")
print(sqloutput)

cur.execute('select Students_info.Name, Students_info.City, Students_info.Department, HOSPITAL_INFO.BED_COUNT, count(Students_info.Department)from COVID_TEST_ROOM \
inner join HOSPITAL_INFO \
on COVID_TEST_ROOM.name = HOSPITAL_INFO.Name \
INNER JOIN Students_info \
on Students_info.City = COVID_TEST_ROOM.CITY_1 or Students_info.city = COVID_TEST_ROOM.CITY_2 \
where not COVID_TEST_ROOM.TIME_WEEKEND = "미운영" and HOSPITAL_INFO.BED_COUNT >= 15 \
GROUP by Students_info.Department \
order by count(Students_info.Department) desc LIMIT 1')
sqloutput = cur.fetchall()
print("14번")
print(sqloutput)

