from bs4 import BeautifulSoup
from pprint import pprint
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import requests, re,os
from urllib.request import urlretrieve

#웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("https://comic.naver.com/webtoon/weekday")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

#요일별 웹툰영역 추출하기
data1_list = soup.findAll('div',{'class':'col_inner'})
# pprint(data1_list)

#전체 웹툰 리스트
li_list = []
for data1 in data1_list:
    #제목 + 썸네일 영역 추출
    li_list.extend(data1.findAll('li')) #해당 부분을 찾아 li_list와 병합
#pprint(li_list)

#각각 썸네일과 제목 추출하기
for li in li_list:
    img = li.find('img')
    title = img['title']
    img_src = img['src']
    #정규식 : 파일, 이미지 파싱할때 특정한 이름을 가진 애들만 가져오고 싶으면
    #정규식 가지고 id,pw만들때 이상한거 못넣게
    #print(title,img_src)
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title) #저 이상한거 정규식(특수문자를 안가져온다는뜻)
    #해당 영역의 글자가 아닌 것은 ''로 치환시킨다.
    urlretrieve(img_src, './images/'+title+'.JPG')
    #주소, 파일걍로+파일명+확장자