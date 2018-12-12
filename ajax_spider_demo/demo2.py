#操作浏览器 切换浏览器页面等

from selenium import webdriver

driver_path = r"D:\chromedriver\chromedriver.exe" #定义驱动目录 因为目录里面有斜杠 所以前面加r 表示是原生的字符串
#定义谷歌浏览器的驱动 需要传递驱动路劲
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

#驱动js打开新窗口
driver.execute_script("window.open('https://www.douban.com/')")

print(driver.window_handles) #打印窗口句柄 第一个是百度 第二个是豆瓣

driver.switch_to_window(driver.window_handles[1]) #切换页面句柄到豆瓣 句柄从0开始

print(driver.current_url) #打印当前所在的网页url


# """
# 注意:
# 虽然窗口切换到了新开的页面,但是driver还没有切换
# 如果要在新开页面进行操作,必须使用driver.switch_to_window来切换指定的页面
# 要从driver.window_handles中取出第几个窗口
# driver.window_handles是列表,存放窗口句柄,按照页面打开的顺序进行存放
# """