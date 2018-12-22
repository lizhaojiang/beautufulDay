from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



class Qiangpiao(object):
    def __init__(self):
        self.login_url = "https://kyfw.12306.cn/otn/login/init" #12306登陆url
        self.initmy_url = "https://kyfw.12306.cn/otn/view/index.html" #登陆成功后显示的url
        self.search_url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc" #查票url
        self.passenger_url = "https://kyfw.12306.cn/otn/confirmPassenger/initDc" #点击预订 乘客选择url
        self.driver = webdriver.Chrome(executable_path="D:\chromedriver\chromedriver.exe")

    #登陆操作 前面加下划线表示这个方法不希望在类外面调用 不能再类外面使用
    def _login(self):
        self.driver.get(self.login_url)
        #显示等待
        WebDriverWait(self.driver,1000).until(
            EC.url_to_be(self.initmy_url) #这个方法表示 url是否是等于指定的url
        )
        print("登陆成功")

    #定义函数 输入出发地和目的地
    def wait_input(self):
        self.from_station = input("出发地: ")
        self.to_station = input("目的地: ")
        #时间格式必须是yyyy-MM-dd 的方式
        self.depart_time = input("出发时间: ")

        self.passengers = input("乘车人(如果有多个乘客用英文逗号分隔): ").split(",")
        self.trains = input("输入车次(如果有多趟车次请用英文逗号分隔): ").split(",")

    #订票
    def _order_ticket(self):
        #1\登陆成功后跳转到查票的url
        self.driver.get(self.search_url)

        #2\使用显示等待 等待用户输入的出发地是否正确
        WebDriverWait(self.driver,1000).until(
            EC.text_to_be_present_in_element_value((By.ID,"fromStationText"),self.from_station)  #注意 此处是元组,通过id查找元素  检查文本输入法值
        )

        # 3\使用显示等待 等待用户输入的目的地是否正确
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, "toStationText"), self.to_station)
        )

        # 4\使用显示等待 等待用户输入的出发日期是否正确
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, "train_date"), self.depart_time)
        )

        #5\等待 查询按钮是否可以点击
        WebDriverWait(self.driver,1000).until(
            EC.element_to_be_clickable((By.ID,"query_ticket")) #此方法检查元素是否可以被点击
        )

        #6\如何按钮可以被点击,就找到这个按钮进行点击事件
        searchBtn = self.driver.find_element_by_id("query_ticket") #找到按钮元素
        searchBtn.click() #执行点击事件

        #7\在点击查询按钮以后 等待 检查车次信息是否显示完整
        WebDriverWait(self.driver,1000).until(
            EC.presence_of_element_located((By.XPATH,".//tbody[@id='queryLeftTable']/tr")) #此方法检查元素时候加载完毕,检查tr标签是否已经显示
        )

        #8\车次信息下tr标签比较多 有部分是不需要的 去除有datatran属性的tr
        ##注意:此处必须使用find_elements_by_xpath## element是加s的 因为是匹配多个
        tr_list =  self.driver.find_elements_by_xpath(".//tbody[@id='queryLeftTable']/tr[not(@datatran)]") #查找没有datatran的tr标签

        #9\遍历所有的tr标签 找出所有车次信息
        for tr in tr_list:
            train_number = tr.find_element_by_class_name("number").text
            # print(train_number)
            # print("="*20)
            #如果所遍历的车次信息中有之前输入指定好的车次信息 就点击预订按钮
            if train_number in self.trains:
                left_ticket = tr.find_element_by_xpath(".//td[4]").text
                if left_ticket == "有" or left_ticket.isdigit:
                    orderBtn = tr.find_element_by_class_name("btn72")
                    orderBtn.click()

                    #等待确认是否进入到了乘客选择页面
                    WebDriverWait(self.driver,1000).until(
                        EC.url_to_be(self.passenger_url)
                    )

                    #进入乘客确认页面后 等待所有乘客加载完成
                    WebDriverWait(self.driver,1000).until(
                        EC.presence_of_element_located((By.XPATH,".//ul[@id='normal_passenger_id']/li")) #presence_of_element_located此方法检测某个元素是否存在
                    )

                    #乘客信息加载完成后 找到所有乘客的lable标签
                    passenger_labels = self.driver.find_elements_by_xpath(".//ul[@id='normal_passenger_id']/li/label")
                    #遍历所有的乘客
                    for passenger_label in passenger_labels:
                        name = passenger_label.text
                        if name in self.passengers:
                            passenger_label.click()
                            submitBtn = self.driver.find_element_by_id("submitOrder_id")
                            submitBtn.click()

                            #点击提交订单后, 等待确认框是否出现
                            WebDriverWait(self.driver,1000).until(
                                EC.presence_of_element_located((By.CLASS_NAME,"dhtmlx_wins_body_outer"))
                            )

                            #在确定 确认按钮是否出现 是否是可以点击状态
                            WebDriverWait(self.driver,1000).until(
                                EC.presence_of_element_located((By.ID,"qr_submit_id"))
                            )

                            #查找确认按钮元素
                            confirmBtn = self.driver.find_element_by_id("qr_submit_id")

                            # while True:
                            #     confirmBtn.click()
                            confirmBtn.click()

                            time.sleep(5)

                            return


    def run(self):
        self.wait_input() #在登陆之前请输入所有需要的信息
        self._login()
        self._order_ticket()



if __name__ == '__main__':
    spider = Qiangpiao()
    spider.run()