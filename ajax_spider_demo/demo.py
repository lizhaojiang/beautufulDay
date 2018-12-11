#常见的表单元素
#input type "text\password\email\number" 文本框
#button type = 'submit' 按钮
#checkbox type = 'checkbox' 多选选项
#select 下拉框选项

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#操作文本框
# driver_path = r"D:\chromedriver\chromedriver.exe" #定义驱动目录 因为目录里面有斜杠 所以前面加r 表示是原生的字符串
# #定义谷歌浏览器的驱动 需要传递驱动路劲
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.baidu.com/')
#
# inputTage = driver.find_element_by_id('kw')
# inputTage.send_keys('php')
# time.sleep(3)
# inputTage.clear() #清除文本框中的信息

#操作checkbox
# driver_path = r"D:\chromedriver\chromedriver.exe" #定义驱动目录 因为目录里面有斜杠 所以前面加r 表示是原生的字符串
# #定义谷歌浏览器的驱动 需要传递驱动路劲
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.douban.com/')
# rembtn = driver.find_element_by_name('remember')
# rembtn.click() #执行点击事件

# from selenium.webdriver.support.ui import Select
#
# #操作select下拉框
# driver_path = r"D:\chromedriver\chromedriver.exe" #定义驱动目录 因为目录里面有斜杠 所以前面加r 表示是原生的字符串
# #定义谷歌浏览器的驱动 需要传递驱动路劲
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.sina.com.cn/')
# selbtn = Select(driver.find_element_by_name('SerchType'))
# selbtn.select_by_index(2) #按索引选择
# selbtn.select_by_value("www.95xiu.com") #按value值进行选择
# selbtn.select_by_visible_text("95秀客户端") #按可见文本进行选择
# selbtn.deselect_all() #取消所有选中


#操作点击事件
driver_path = r"D:\chromedriver\chromedriver.exe" #定义驱动目录 因为目录里面有斜杠 所以前面加r 表示是原生的字符串
#定义谷歌浏览器的驱动 需要传递驱动路劲
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

inputTage = driver.find_element_by_id('kw')
inputTage.send_keys('php')

subTage = driver.find_element_by_id("su")
subTage.click()