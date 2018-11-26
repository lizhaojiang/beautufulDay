import requests
from lxml import etree
from urllib import request
import os
import re






def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    }
    respones = requests.get(url,headers=headers) #解析url链接
    text = respones.text #获取网页源代码
    html = etree.HTML(text) #生成HTML对象文件
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    for img in imgs:
        img_url = img.get('data-original') #使用get()方法可以直接获取某个元素中的属性
        alt = img.get('alt') #获取图片的名称(解释)
        alt = re.sub(r'[\?？\.，。！!]]','',alt) #使用正则表达式替换标题中的特殊字符
        suffix = os.path.splitext(img_url)[1] #使用os模块分割链接 获取链接的后缀(.gif)
        filename = alt + suffix
        request.urlretrieve(img_url,'imgs/'+filename)



def main():
    for x in range(1,100):
        #获取前100页的数据 构建url链接
        url = "https://www.doutula.com/photo/list/?page=%d"%x
        parse_page(url)
        break

if __name__ == '__main__':
    main()