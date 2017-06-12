import requests
import re
import random

import time
from bs4 import BeautifulSoup

class download:
    def __init__(self):
        self.iplist = []
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        html = requests.get("http://www.xicidaili.com/nn",headers = headers)
        # html = requests.get("http://www.xicidaili.com/nn",headers = )
        iplistn = BeautifulSoup(html.text, 'lxml').find_all('tr', class_="odd")
        for ip in iplistn:
            ip1 = ip.find_all('td')[1].text
            port = ip.find_all('td')[2].text
            ips = ip1 + ':' + port
            self.iplist.append(ips.strip())
            # print(ips.strip())
        # print(self.iplist)
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]

    def get(self,url,proxy = None,num_retries=3):
        print(u'开始获取：',url)
        UA = random.choice(self.user_agent_list)
        headers = {'User-Agent':UA}

        if proxy == None:
            try:
                response = requests.get(url,headers = headers)
                return response
            except:
                if num_retries>0:
                    print(u'获取网页出错，再来一次')
                    time.sleep(1)
                    return self.get(url,num_retries-1)


                else:

                    time.sleep(1)
                    IP = ''.join(str(random.choice(self.iplist)).strip())
                    print(IP)
                    proxy = {'http':IP}

                    return self.get(url,proxy)

        else:
            try:
                print(u'开始使用代理')
                time.sleep(1)
                IP = ''.join(str(random.choice(self.iplist)).strip())
                print(IP)
                proxy = {'http': IP}
                response = requests.get(url, headers=headers, proxies=proxy)
                return response

            except:

                if num_retries > 0:

                    IP = ''.join(str(random.choice(self.iplist)).strip())
                    proxy = {'http':IP}
                    time.sleep(2)
                    print(u'正在更换代理')
                    print(u'当前代理：',IP)
                    return self.get(url,proxy,num_retries-1)

                else:
                    print(u'代理也不好使了')
                    return self.get(url)

request = download()


