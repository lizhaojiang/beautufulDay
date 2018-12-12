#分析网页进行爬取
import requests
from lxml import etree
import time

def request_list_page():
    url = "https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Referer":"https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
    }
    data = {
        'first':'true',
        'pn':1,
        'ks':'python'
    }
    for x in range(1,31):
        data['pn'] = x
        response = requests.post(url, headers=headers)
        print(response.json())
        time.sleep(2)

def main():
    request_list_page()

if __name__ == '__main__':
    main()