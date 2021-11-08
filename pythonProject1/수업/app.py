import math
import random
import sys
import inspect
import os
import datetime
import time
from urllib import request
from bs4 import BeautifulSoup
from flask import Flask

# print("math.sin(1) : ", math.sin(1))
# print("math.cos(1) : ", math.cos(1))
# print("math.tan(1) : ", math.tan(1))
# print("math.floor(2.5) : ", math.floor(2.5))
# print("math.ceil(1) : ", math.ceil(1))
#
# print("#random 모듈")
# print("~random():",random.random())
# print("- uniform(10,20):", random.uniform(10,20))
# print("-randrange(10):",random.randrange(10))
# print("-choice([1,2,3,45]):",random.choice([1,2,3,4,5]))
# print("-shffle([1,2,3,4,5]", random.shuffle([1,2,3,4,5]))
# print("-sample([1,2,3,4,5], k=2):",random.sample([1,2,3,4,5], k=2))
#
# print(sys.argv)
# print(sys.getwindowsversion())
# print(sys.copyright)
#
# sys.exit()
#
# print(os.name)
# print(os.getcwd())
# print(os.listdir())
#
# now = datetime.datetime.now()
#
# output_a = now.strftime("%Y")
# print(output_a)
#
# print("이런게 있네 : {}".format(*"얍"))
#
# now = datetime.datetime.now()
#
# print("#datime.timedelta로 시간 더하기")
# after = now + datetime.timedelta(weeks=1, days=1, hours=1, minutes=1, seconds=1)
# print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
#
# print("#now.replace()로 1년 더하기")
# output = now.replace(year=(now.year +1))
# print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
#
# print("지금부터 5초 동안 정지합니다")
# #time.sleep(5)
# print("5초가 지났습니다")
#
# target = request.urlopen("https://google.com")
# output = target.read()
# print(output)
#
# target = request.urlopen("https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
#
# soup = BeautifulSoup(target, "html.parser")
#
# for location in soup.select("location"):
#     print("도시:", location.select_one("city").string)
#     print("날씨:", location.select_one("wf").string)
#     print("최저기온:", location.select_one("tmn").string)
#     print("최고기온:", location.select_one("tmx").string)
#     print()

#와 웹페이지 만들기
app = Flask(__name__)

@app.route("/")
def hello():
    target = request.urlopen("https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
    soup = BeautifulSoup(target, "html.parser")

    output =""
    for location in soup.select("location"):
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날씨: {}<br/>".format(location.select_one("wf").string)
        output += "최저/최고 기온: {}/{}"\
        .format(\
            location.select_one("tmn").string,\
            location.select_one("tmx").string\
            )
        output+= "<hr/>"
    return output
#
# #데코레이터
# def test(func):
#     def wrapper():
#         print("인사 시작")
#         func()
#         print("인사 끝")
#     return wrapper
#
# @test
# def hello():
#     print("안녕")
#
# hello()