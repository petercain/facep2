'''
Data
데이타 베이스
테이블
SQL(데이타 베이스를 위한 언어)


테이불에 데이터 추가
INSERT INTO 테이블명 (컬럼명, 컬럼명2)
VALUES (값1, 값2);


테이블에 저장된 데이터 조회
SELECT * FROM테이블
SELECT (조회하고싶은 컬럼) FROM 테이블


특정한 조건을 주고 싶을때
WHERE(조건식) 써준다
SELECT * FROM WHERE(조건식)


테이블에 저장된 데이터 변경
해당 테이브르이 모든 컬럼을 변경)
UODATE 테이블명 SET 컬럼명 =변경값


특정조건에 해당하는 컬럼의 값 변경)
UODATE 테이블명 SET 컬럼명 =변경값 WHERE(조건식)


테이블의 컬럼명 변경
ALTER TABLE 테이블명 RENAME COLUMN 변경전컬럼이름 TO 변경후컬럼이름


테이블의 데이터 삭제(쓰지마)
DELETE FROM 테이블명

해당하는 테이블의 데이터 삭제
DELETE FROM 테이블명 WHERE(조건식)


트랜잭션 관리
돈을 이체합니다
내 계좌에 있는 돈 - 이체금액
이체할 상대방 계좌에 있는 돈 + 이체금액
(정상실행 하지 못할 시 -이체금액 작업취소)
여러사람들이 동시에 작업
한 데이터를 여러명이 수정하려고 할 때
순차적으로 실행 할 수 있도록 해야한다.

commit;를 해야 가지고 있던 데이터를 저장
'''

import sqlite3

conn = sqlite3.connect("dorothy.db")
cur = conn.cursor()

cur.execute('CREATE TABLE employee_data(id INTEGER, name TEXT, nickname TEXT, department TEXT, employment_date TEXT)')

#여러개 한꺼번에 INSERT하는 법 # 튜플 사용
# test_tuple = (
#     (4, '효정', '최효정', '오마이걸', '1994-07-28'),
#     (5, '미미', '김미현', '오마이걸', '1955-05-01'),
#     (6, '유아', '유시아', '오마이걸', '1995-09-17')
# )
# conn.executemany("INSERT INTO employee_data(id, name, nickname, \
#                 department, employment_date)\
#                  VALUES(?,?,?,?,?)", test_tuple)

# sqloutput = cur.fetchall()
# print(sqloutput)

conn.commit()
conn.close()

#처음만들때 쓴거
#conn.execute('CREATE TABLE employee_data(id INTEGER, name TEXT, nickname TEXT, department TEXT, employment_date TEXT)')

#추가할떄 쓰는거?
#("INSERT INTO employee_data(id, name, nickname, department, employment_date)values(2, '홍길동', '서자', '활빈당', '2021-08-18')")

#읽을때 쓰는거?
#cur.execute("SELECT name, department FROM employee_data")
#sqloutput = cur.fetchall()

#가나다순
#SELECT name FROM employee_data ORDER BY name

#조건식
#EX
#SELECT * FROM employee_data WHERE department = "둘리당"
#SELECT * FROM employee_data WHERE department like "%리%"
#SELECT * FROM employee_data WHERE department like "둘리%"
#SELECT * FROM employee_data WHERE department > "하"
#SELECT * FROM employee_data WHERE ID ID = 1

#특정 조건에 해당하는 컬럼의 값 변경
#UPDATE employee_data SET department = '러블리즈' WHERE name = '홍길동'



#여러개 한꺼번에 INSERT하는 법 # 튜플 사용
# test_tuple = (
#     (4, '효정', '최효정', '오마이걸', '1994-07-28'),
#     (5, '미미', '김미현', '오마이걸', '1955-05-01'),
#     (6, '유아', '유시아', '오마이걸', '1995-09-17')
# )
# conn.executemany("INSERT INTO employee_data(id, name, nickname, department, employment_date) VALUES(?,?,?,?,?)", test_tuple)


#컴럼명 바꾸는거
#ALTER TABLE employee_data RENAME COLUMN employment_date TO birhtday

#컬럼 삭제하는법
#DELETE FROM employee_data WHERE name like '이길동'

#case인데 용도가 뭔지는 모르겠음
# SELECT name,
# CASE WHEN department = '러블리즈' THEN 'SM'
# 	 WHEN department = '오마이걸' THEN 'WM'
# END company
# FROM employee_data

#SELECT strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime') 현지시간;
#SELECT strftime('%Y-%m-%d %H:%M:%S','employment_date') 시간값

#SELECT name, strftime('%Y', 'now') - strftime('%Y', employment_date) 나이구하기
#FROM employee_data

#러블리즈
#SELECT substr(department,1,2) FROM employee_data  # 러블
##SELECT substr(department,2,3) FROM employee_data # 블리즈





#0819

#count(*) 행의 수를 세어준다
#개수 구하기
#SELECT count(*) FROM employee_data WHERE department like '오마이걸'

#맥스값
#MAX(*)조회된 행 중 가장 큰 값을 찾아준다.
#SELECT name, max(ID) FROM employee_data WHERE department like '오마이걸'
#오마이걸 내의 제알 큰 아이디 넘버와 이름 출력

#MIN(*)
##MIN(*)조회된 행 중 가장 작은 값을 찾아준다.

#그룹 내 수 집계
#SELECT department, count(*) FROM employee_data GROUP BY department
#러블리즈	4
#오마이걸	3

#join 여러 테이브르이 자료를 보여주고 싶을 떄 사용한다.
#select * from 첫번째 테이블
#inner join 두번째 테이블 on 조건식
#다같이
#ex

# 오병수님이 사는 도시의 선별 진료소 목록을 보여주세요
# SELECT Students_info.Name, COVID_TEST_ROOM.name FROM Students_info
# inner join COVID_TEST_ROOM
# on Students_info.City = COVID_TEST_ROOM.CITY_1 WHERE Students_info.Name = "오병수"

#--------------------------------------------------

# SELECT Students_info.Name, COVID_TEST_ROOM.name   #이거 두개를 셀렉할건데
# FROM Students_info    #이 테이블에
# inner join COVID_TEST_ROOM    #이 테이블을 합치는 느낌이야
# on Students_info.City = COVID_TEST_ROOM.CITY_1    #조건이고
# WHERE Students_info.Name = "오병수"  조건이야

#스튜던트인포에 코로나테스트룸을 합치고 on조건식~where조건식~

#14. 공휴일에 운영을 하고, 진료과목이 15개 이상인 병원들의 수가 많은 조
