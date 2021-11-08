from bs4 import BeautifulSoup
from pprint import pprint
import requests

#웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("https://comic.naver.com/webtoon/weekday")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

#월요웹툰 영역 추출하기
data1 = soup.find('div', {'class':'col_inner'})
# pprint(data1)

#제목 포함영역 추출하기
data2 = data1.findAll('a',{'class':'title'})
#pprint(data2)

title_list = []
for t in data2:
    title_list.append(t.text)

pprint(title_list)