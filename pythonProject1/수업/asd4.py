import dload
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')

# 파싱할 Url
baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=강아지'

# Driver로 Url Open
driver.get(baseUrl)

time.sleep(3) # 5초 동안 페이지 로딩 기다리기

req = driver.page_source

soup = bs(req, "html.parser")

imgs = []
for i in range(1,12):
    # css 속성기반으로 찾는 함수 select(모두), select_one(한개만)
    img = soup.select('#main_pack > section > div > div.photo_group._listGrid > div.photo_tile._grid > div:nth-child({}) > div > div.thumb > a > img'.format(i))
    imgs.append(img)

i = 1
for img in imgs:
    for img2 in img:
        image_src = img2['src']
        dload.save(image_src, f'images/{i}.jpg')
        i += 1

driver.quit()