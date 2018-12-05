from selenium import webdriver
import time

driver_path = r"D:\chromedriver\chromedriver.exe" #定义驱动目录 因为目录里面有斜杠 所以前面加r 表示是原生的字符串


#定义谷歌浏览器的驱动 需要传递驱动路劲
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

# time.sleep(5)
# driver.close() #关闭当前页面
# driver.quit() #退出整个浏览器

# inputTage = driver.find_element_by_id('kw') #使用selenium使用获取id的方式获取input输入框
# inputTage = driver.find_element_by_name('wd') #使用selenium使用获取name的方式获取input输入框
# inputTage = driver.find_element_by_class_name('s_ipt') #使用selenium使用获取classname的方式获取input输入框\

#通过xpath语法查找
# inputTage = driver.find_element_by_xpath('//input[@id="kw"]')

#通过css选择器查找 quickdelete-wrap下面的直接子元素 quickdelete-wrap是class 前面要加点
# inputTage = driver.find_element_by_css_selector(".quickdelete-wrap > input")
#如果要加查找多个加s 返回的是列表 取0操作
inputTage = driver.find_elements_by_css_selector(".quickdelete-wrap > input")[0]


inputTage.send_keys('python') #在input输入框中输入python字符串
