import requests
from bs4 import BeautifulSoup
#requests库使用
url1 = 'https://www.baidu.com/'
header1 = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
response = requests.get(url1, headers = header1)
# print(response.text)

#bs库使用
url2 = 'https://www.mzitu.com/74381'
html = requests.get(url2, headers = header1)
pagenavi = BeautifulSoup(html.text,'lxml').find('div',class_='pagenavi').find_all('span')
# print(pagenavi)

#下载一张图片
header2 = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Referer": "https://www.mzitu.com/jiepai/comment-page-1/"}
url2 = 'https://www.mzitu.com/74381'
html = requests.get(url2, headers = header2)
img_url = BeautifulSoup(html.text,'lxml').find('div',class_='main-image').find('img')['src']
img = requests.get(img_url, headers = header2)
f = open('123.jpg', 'wb')
f.write(img.content)
f.close()