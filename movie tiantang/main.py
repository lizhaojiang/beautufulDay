import requests
from lxml import etree

# url = "http://www.dytt8.net/html/gndy/dyzz/list_23_1.html"
#请求头定义为全局变量
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}
#设置全局变量,拼接完整的url链接
BASE_DOMAIN = 'http://www.dytt8.net'

#定义为函数 获取页面所有的url链接
def get_detail_urls(url):
    respones = requests.get(url,headers=HEADERS)
    #respones.text 该网页采用的是gbk编码的 使用respones.text会产生乱码
    #respones.content 所以必须使用respones.content 并解码为gbk
    # print(respones.content.decode("gbk"))
    # text = respones.content.decode('gbk') #此处必须使用gbk解码 *****
    text = respones.text #因为有部分页面内有无法解析的字 所以使用gbk会产生错误
    html = etree.HTML(text)
    detail_url = html.xpath("//table[@class='tbspan']//a/@href")
    # for url in urls:
    #     print(BASE_DOMAIN + url)
    detail_urls = map(lambda url:BASE_DOMAIN+url,detail_url)
    return detail_urls


def parse_detail_page(url):
    movie = {} #存放到集合中 用于存放每个电影的所有数据  *****注意:存放到集合中
    respones = requests.get(url,headers=HEADERS)
    text = respones.content.decode('gbk') #使用gbk进行解码
    html = etree.HTML(text)
    title =html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0] #获取标签里面的文字内容 使用text()方法
    movie['title'] = title
    zoomE = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoomE.xpath(".//img/@src") #获取到的图片有两张 海报和电影截图
    cover = imgs[0] #第一张是海报
    screenshot = imgs[1] #第二张是电影截图
    movie['cover'] = cover
    movie['screenshot'] = screenshot
    infos = zoomE.xpath(".//text()") #获取所有电影相关的文本数据

    def parse_info(info,rule): #定义函数用于截取电影详细数据
        return info.replace(rule,"").strip()

    for index,info in enumerate(infos): #此for循环使用enumerate() 会增加index下标属性 用于获取数据下标
        if info.startswith("◎译　　名"): #函数startswith() 是以什么开头
            info = parse_info(info,"◎译　　名") #replace("将要替换的","替换后的") 替换字符串
            movie['yiming'] = info
        elif info.startswith("◎年　　代"):
            info = parse_info(info,"◎年　　代")
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = parse_info(info,"◎产　　地")
            movie['country'] = info
        elif info.startswith("◎豆瓣评分"):
            info = parse_info(info,"◎豆瓣评分")
            movie['pingfen'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info,"◎片　　长")
            movie['time'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info,"◎导　　演")
            movie["daoyan"] = info
        #***注意 主演这个会有很多个,并且每一个都占用一行
        elif info.startswith("◎主　　演"):
            info = parse_info(info,"◎主　　演")
            actors = [info]
            for x in range(index+1,len(infos)): #使用下标遍历所有有关演员的数据
                actor = infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            movie['actors'] = actors
        #***和主演的获取方式一样,简介正文前面有空行
        elif info.startswith("◎简　　介 "):
            info = parse_info(info,"◎简　　介 ")
            for x in range(index+1,len(infos)):
                profile = infos[x].strip()
                if profile.startswith("【下载地址】"):
                    break
                movie['profile'] = profile
    download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    movie['download_url'] = download_url

    return movie


#定义函数获取1-7页的链接
def spider():
    #其中{}表示占用位
    base_url = "http://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
    for x in range(1,8):
        movies = []
        url = base_url.format(x) #获取每一页的总链接
        detail_urls = get_detail_urls(url)  #获取每一页中所有的链接
        for detail_url in detail_urls:
            movie = parse_detail_page(detail_url) #获取每一个链接中的详情信息
        #     break #调试只要第一个链接
        # break #调试应该是阻止两个for循环 只执行一次   ***********这里失误***************
            movies.append(movie)
            print(movie)
if __name__ == '__main__':
    spider()