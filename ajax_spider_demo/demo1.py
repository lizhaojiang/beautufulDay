from selenium import webdriver
import time

driver_path = r"D:\chromedriver\chromedriver.exe" #定义驱动目录 因为目录里面有斜杠 所以前面加r 表示是原生的字符串

#定义谷歌浏览器的驱动 需要传递驱动路劲
driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.baidu.com/')

time.sleep(5)

# driver.close() #关闭当前页面

driver.quit() #退出整个浏览器