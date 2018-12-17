#分析网页进行爬取
#后面添加详情页面的爬取

import requests
from lxml import etree
import time
import re

headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Referer":"https://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=",
        'Cookie':'user_trace_token=20181213213113-5c50b217-fedb-11e8-9130-525400f775ce; LGUID=20181213213113-5c50b68c-fedb-11e8-9130-525400f775ce; sajssdk_2015_cross_new_user=1; ab_test_random_num=0; JSESSIONID=ABAAABAAADEAAFI3CA66745879CFADD69FDBA1F4547B6E5; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22167a7d1b0a7101-0aa4344cbf249a-58133b15-1049088-167a7d1b0a834e%22%2C%22%24device_id%22%3A%22167a7d1b0a7101-0aa4344cbf249a-58133b15-1049088-167a7d1b0a834e%22%7D; LG_LOGIN_USER_ID=9a87a5c446edd32f0b531f099c103b7fd7c7117052889e90; _putrc=13C40F4E1686C6D6; login=true; unick=%E6%9D%8E%E5%85%86%E6%B1%9F; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=106; gate_login_token=9e43e0cbb4fd41685f8edaf2cbe5d703d662dac72d7aaeed; _gat=1; TG-TRACK-CODE=search_code; _gid=GA1.2.562066263.1544707878; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1544707878,1544708918,1544710403; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1544711290; _ga=GA1.2.178524049.1544707878; LGSID=20181213213113-5c50b3d7-fedb-11e8-9130-525400f775ce; LGRID=20181213222805-4df5d49f-fee3-11e8-8cef-5254005c3644; SEARCH_ID=eaa2b683972b40abb50985dcc88f8e2a; index_location_city=%E5%8C%97%E4%BA%AC'
    }

def request_list_page():
    url = "https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"

    data = {
        'first':'false',
        'pn':1,
        'ks':'python'
    }
    for x in range(1,31):
        data['pn'] = x
        response = requests.post(url, headers=headers)
        result = response.json()
        positions = result['content']['positionResult']['result']
        for position in positions:
            positionId = position['positionId']
            position_url = 'https://www.lagou.com/jobs/%s.html'%positionId
            parse_positon_detail(position_url)
            break
        break

def parse_positon_detail(url):
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    position_name = html.xpath('//span[@class="name"]/text()')[0] #获取职位名称
    job_request_spans = html.xpath('//dd[@class="job_request"]//span') #获取职位信息 薪资等信息
    # salary = job_request_spans[0].xpath['.//text()'][0].strip() #去除两边的空格  获取薪资信息
    salary = job_request_spans[0].text.strip() #去除两边的空格  获取薪资信息
    # city = job_request_spans[1].xpath['.//text()'][0].strip() #去除两边的空格以及斜杠 获取城市信息
    city = job_request_spans[1].text.strip() #去除两边的空格以及斜杠 获取城市信息
    city = re.sub(r"[\s/]",'',city)
    # work_years = job_request_spans[2].xpath['.//text()'][0].strip() #去除两边的空格以及斜杠 获取城市信息
    work_years = job_request_spans[2].text.strip() #去除两边的空格以及斜杠 获取城市信息
    work_years = re.sub(r"[\s/]]","",work_years) #获取工作年限
    education = job_request_spans[3].xpath['.//text()'][0].strip()
    education = re.sub(r"[\s/]]","",education) #获取学历

    # desc = html.xpath('//dd[@class="job_bt"]//text()') #获取职位要求及详细信息
    #将所有的职位信息转换为字符串
    desc = "".join(html.xpath('//dd[@class="job_bt"]//text()')).strip()

def main():
    request_list_page()

if __name__ == '__main__':
    main()