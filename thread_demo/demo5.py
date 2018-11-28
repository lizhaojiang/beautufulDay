import requests
from lxml import etree
from urllib import request
import os
import re
from queue import Queue
import threading

#使用生产者和消费者模式 异步 爬取下载图片


#创建生产者
class Procuder(threading.Thread): #因为两个线程在main函数中 所以要重写init方法
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    }
    def __init__(self,page_queue,img_queue,*args,**kwargs): #args表示任意的参数 kwargs表示任意的关键字参数
        super(Procuder, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get() #获取队列中的url
            self.parse_page(url)

    def parse_page(self,url):
        respones = requests.get(url,headers=self.headers) #解析url链接
        text = respones.text #获取网页源代码
        html = etree.HTML(text) #生成HTML对象文件
        imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        for img in imgs:
            img_url = img.get('data-original') #使用get()方法可以直接获取某个元素中的属性
            alt = img.get('alt') #获取图片的名称(解释)
            alt = re.sub(r'[\?？\.，。！!\*]','',alt) #使用正则表达式替换标题中的特殊字符
            suffix = os.path.splitext(img_url)[1] #使用os模块分割链接 获取链接的后缀(.gif)
            filename = alt + suffix
            # request.urlretrieve(img_url,'imgs/'+filename) #获取好链接后 下载图片的任务就放到消费者线程当中去
            self.img_queue.put((img_url,filename)) #将每个图片的url和文件名放到 图片的队列中去

#创建消费者
class Consumer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs): #args表示任意的参数 kwargs表示任意的关键字参数
        super(Consumer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url,filename = self.img_queue.get()
            request.urlretrieve(img_url, 'imgs/' + filename)
            print(filename + " 下载完成!")



def main():
    page_queue = Queue(100)  # 爬取100页的数据
    img_queue = Queue(1000)  # 指定下载的图片数量 尽可能大点
    for x in range(1,101):
        #获取前100页的数据 构建url链接
        url = "https://www.doutula.com/photo/list/?page=%d"%x
        page_queue.put(url) #把每一个的url 添加到队列中

    for x in range(5): #创建5个生产者
        t = Procuder(page_queue,img_queue) #此处括号内的元素顺序要和定义类中的顺序一致
        t.start()
    for x in range(5): #创建5个消费者
        t = Consumer(page_queue,img_queue) #此处括号内的元素顺序要和定义类中的顺序一致
        t.start()

if __name__ == '__main__':
    main()