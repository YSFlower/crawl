import datetime

import requests
from bs4 import BeautifulSoup
import os
import time
from crawl import request
# from pymongo import MongoClient

class mzitu():

    def all_url(self,url):
        html = request.get(url)
        all_a = BeautifulSoup(html.text,'lxml').find('div',class_='postlist').find_all('a')
        for a in all_a:
            title = a.get_text()
            self.title = title
            print(u'开始保存:',title)
            path = str(title).replace("?",'_')
            if self.mkdir(path):
                os.chdir("D:\mzitu\\" + path)
                href = a['href']
                self.url = href
                self.html(href)

    def mkdir(self, path):
        path = path.strip()
        self.title = path
        isExisted = os.path.exists(os.path.join("D:\mzitu",path))
        if not isExisted:
            print(u'创建文件夹：',path)
            os.makedirs(os.path.join("D:\mzitu",path))
            os.chdir(os.path.join("D:\mzitu",path))
            return True
        else:
            print(u'该文件夹已经存在了：',path)
            return False


    def html(self,href):
        html = self.request(href)
        aa = BeautifulSoup(html.text,'lxml').find_all('span')
        max_span = BeautifulSoup(html.text,'lxml').find_all('span')[9].get_text()
        self.page_num = 0
        for page in range(1,int(max_span)+1):
            self.page_num += 1
            page_url = href + '/' + str(page)
            time.sleep(0.2)
            self.img(page_url)

    def img(self, page_url):
        img_html = self.request(page_url)
        img_url = BeautifulSoup(img_html.text,'lxml').find('div',class_='main-image').find('img')['src']
        self.save(img_url)

    def save(self, img_url):
        print('正在获取{}第{}张图片'.format(self.title, self.page_num))
        name = self.title + '_' + str(self.page_num)
        img = self.request(img_url)
        f = open(name+'.jpg', 'wb')
        f.write(img.content)
        f.close()

    def request(self,url):
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                   "Referer": "https://www.mzitu.com/jiepai/comment-page-1/"
                   }
        content = requests.get(url,headers = headers)
        return content


if __name__=="__main__":
    Mz = mzitu()
    Mz.all_url("https://www.mzitu.com/all")