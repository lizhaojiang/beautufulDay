#使用selenium操作代理IP
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


#设置浏览器驱动
driver_path = r"D:\chromedriver\chromedriver.exe"
#设置代理
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://222.33.192.238:8118")


driver = webdriver.Chrome(executable_path=driver_path,chrome_options=options)

driver.get("http://httpbin.org/ip")