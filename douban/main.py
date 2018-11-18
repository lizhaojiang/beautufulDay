import requests
from lxml import etree
#设置请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Referer':'https://movie.douban.com/'
}
#定义URL
url = "https://movie.douban.com/cinema/nowplaying/beijing/"

#第一步 先将目标网站抓取下来
#使用requests库 使用get方法获取网页(因为此网页是使用get获取的,获取方式可以在请求头中查看)
respones = requests.get(url,headers=headers)
text = respones.text #获取整个网页
#respones.text
#respones.content
#y以上这两种方式都可以抓取网页代码,但是因为两个方法所对应的解码方式不同,不同网页使用不同的

#测试获取整个网页
#print(respones.text)

#第二步 使用xpath获取所需的数据
html = etree.HTML(text)
#获取网页中所有ul中class=lists属性的标签
ul = html.xpath("//ul[@class='lists']")[0]
#打印测试所获取的数据,发现有两个结果,通过查看原网页发现有两个ul中class=lists的 一个为正在上映 一个为即将上映 打印结果:[<Element ul at 0x354c9c8>, <Element ul at 0x354c948>]
#所以只获取第一个即可 即:ul = html.xpath("//ul[@class='lists']")[0]
# print(etree.tostring(ul,encoding="utf-8").decode("utf-8"))
#获取ul下面的li标签
lis = ul.xpath("./li")
movies = [] #定义一个空列表,用于存放所有电影信息
for li in lis:
    # print(etree.tostring(li,encoding='utf-8').decode('utf-8'))
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    region = li.xpath("@data-region")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    thumbnail = li.xpath(".//img/@src")[0] #获取电影缩略图,因为图片在li中只有一个,所以直接使用.//获取 注意img不是在li的直接子元素下 所以必须使用.//不能用./
    # print(thumbnail)
    movie = {
        'title':title,
        'score':score,
        'region':region,
        'director':director,
        'actors':actors,
        'thumbnail':thumbnail
    }
    movies.append(movie)
print(movies)