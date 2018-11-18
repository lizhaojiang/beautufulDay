import requests
from bs4 import BeautifulSoup
from pyecharts import Bar


ALL_DATA = []

def parse_pages(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    }
    response = requests.get(url,headers= headers)
    text = response.content.decode('utf-8') #使用content获取页面内容再进行解码 ,因为使用response.text会出现乱码
    soup = BeautifulSoup(text,"html5lib")
    conMidtab = soup.find('div',class_='conMidtab') #获取第一个div标签 使用find方法 直接返回查找的标签的直接子元素
    tables = conMidtab.find_all('table') #获取所有的table标签
    for table in tables:
        trs = table.find_all("tr")[2:] #因为前两个tr标签是表头 所以过滤
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]
            if index == 0:
                city_td == tds[1]
            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            ALL_DATA.append({"city":city,"min_temp":int(min_temp)}) #温度排序需要使用int类型

def main():
    # url = "http://www.weather.com.cn/textFC/gat.shtml"
    urls = [
        "http://www.weather.com.cn/textFC/hb.shtml",
        "http://www.weather.com.cn/textFC/db.shtml",
        "http://www.weather.com.cn/textFC/hd.shtml",
        "http://www.weather.com.cn/textFC/hz.shtml",
        "http://www.weather.com.cn/textFC/hn.shtml",
        "http://www.weather.com.cn/textFC/xb.shtml",
        "http://www.weather.com.cn/textFC/xn.shtml",
        "http://www.weather.com.cn/textFC/gat.shtml"
    ]
    for url in urls:
        parse_pages(url)



    #分析数据
    #使用最低气温排序
    #可以使用这种定义一个函数的方式来进行排序,但是因为这个函数在程序中只使用一次 所以使用lambda匿名函数
    # def sort_temp(data):
    #     min_temp = data['min_temp']
    #     return min_temp

    ALL_DATA.sort(key=lambda data:data['min_temp'])
    data = ALL_DATA[0:10]
    #pyecharts 可视化工具
    cities = list(map(lambda x:x['city'],data)) #map()函数数遍历列表data,将data中的而每一项都传给lambda表达式(函数)
    temps = list(map(lambda x:x['min_temp'],data)) #注意 map返回的是一个对象,需要将其装换为列表
    char = Bar("中国最低气温排行榜")
    char.add('',cities,temps)
    char.render('temp.html')


if __name__ == '__main__':
    main()