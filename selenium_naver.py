from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'

driver = webdriver.Chrome('./chromedriver')
driver.get(url)

# driver.get(f'https://search.naver.com/search.naver?where=realtime&sm=tab_nmr&query={word}')로 입력해도 ㄱㅊ
# f 를 앞에 입력하여 한글이 입력되도 안 헷갈리도록 한다

words = driver.find_elements_by_css_selector(
    '#content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul > li > a > span')
texts = [word.text for word in words]

print("실시간 검색어")
for n in range(0, len(texts)):
    print("%d"%(n+1) + "." + " " + texts[n])

driver.quit()
