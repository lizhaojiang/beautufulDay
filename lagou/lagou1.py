from selenium import webdriver
from lxml import etree
import re
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By





#定义一个拉钩爬虫类
class LagouSpider(object):
    driver_path = r"D:\chromedriver\chromedriver.exe" #指定谷歌浏览器驱动地址
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
        self.positions = []

    #重写run方法
    def run(self):
        self.driver.get(self.url)  # 打开拉钩网
        while True:
            source = self.driver.page_source  # 网页原代码

            #设置等待 等待下一页元素加载完成 写完两个等待后出现报错
            # WebDriverWait(driver=self.driver,timeout=10).until(
            #     EC.presence_of_element_located((By.XPATH,"//div[@class='pager_container']/span[last()]"))
            # )

            self.parse_list_page(source)
            #使用try-except 如果发生错误
            try:
                # 爬取完一页后要模拟浏览器进行点击下一页
                # 获取下一页按钮
                next_btn = self.driver.find_element_by_xpath(
                    "//div[@class='pager_container']/span[last()]")  # 获取页码的div中的最有一个span标签使用last() ,不直接获取下一页的标签是因为[下一页]标签中的class里面包含空格
                # 判断下一页按钮是否能够点击(如果是最后一页的话 下一页按钮无法点击)
                # 如果class标签中有"pager_next_disabled"表示 无法点击
                if "pager_next_disabled" in next_btn.get_attribute("class"):
                    break
                else:
                    next_btn.click()  # 执行点击操作
            except:
                print(source)
            time.sleep(1)


    #获取首页发布的信息链接
    def parse_list_page(self,source):
        html = etree.HTML(source)
        links = html.xpath('//a[@class="position_link"]/@href') #获取所有发布的信息链接 进入链接获取每一个详细信息
        for link in links:
            self.request_detail_page(link)
            time.sleep(1)

    #获取每个职位的详细信息
    def request_detail_page(self,url):
        # self.driver.get(url) #打开新的链接地址 打开新的地址将覆盖之前打开的lagou.com搜索python的页面,导致的后果就是获取下一页的时候无法再原来的页面进行点击
        #打开新窗口
        self.driver.execute_script("window.open('%s')"%url)

        # #设置等待 写完这里报错
        # WebDriverWait(driver=self.driver,timeout=10).until(
        #     EC.presence_of_element_located((By.XPATH,"//span[@class='name']"))
        # )

        #切换新窗口
        self.driver.switch_to.window(self.driver.window_handles[1])
        source = self.driver.page_source  #获取详情页面的源代码
        self.parse_detail_page(source)
        #关闭详情页窗口
        self.driver.close()
        #切换回原来的职位列表页
        self.driver.switch_to.window(self.driver.window_handles[0])


    #解析每一个详情页面的信息
    def parse_detail_page(self,source):
        html = etree.HTML(source)
        position_name = html.xpath('//span[@class="name"]/text()')[0]  # 获取职位名称
        job_request_spans = html.xpath('//dd[@class="job_request"]//span')  # 获取职位信息 薪资等信息
        salary = job_request_spans[0].text.strip()  # 去除两边的空格  获取薪资信息
        city = job_request_spans[1].text.strip()  # 去除两边的空格以及斜杠 获取城市信息
        city = re.sub(r"[\s/]", '', city)
        work_years = job_request_spans[2].text.strip()  # 去除两边的空格以及斜杠 获取城市信息
        work_years = re.sub(r"[\s/]]", "", work_years)  # 获取工作年限
        education = job_request_spans[3].text.strip()
        education = re.sub(r"[\s/]]", "", education)  # 获取学历
        desc = "".join(html.xpath('//dd[@class="job_bt"]//text()')).strip() #此方法是将所有的文本信息转换为字符串类型
        company_name = html.xpath("//h2[@class='fl']/text()")[0].strip() #获取公司名称
        position = {
            'company':company_name,
            'name':position_name, #职位名称
            'salary':salary, #薪资
            'city':city, #城市
            'work_years':work_years, #工作年限
            'education':education, #学历
            'desc':desc #要求详细描述
        }
        self.positions.append(position)
        print(position)
        print("="*40)



if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()