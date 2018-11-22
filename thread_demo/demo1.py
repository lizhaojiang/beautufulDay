import threading #引入多线程库
import time

#使用传统的方式
# def coding():
#     for x in range(3):
#         print("正在写代码%s"%x)
#         time.sleep(1)
# def drawing():
#     for x in range(3):
#         print("正在画图%s"%x)
#         time.sleep(1)
# def main():
#     coding()
#     drawing()

#使用多线程
# def coding():
#     for x in range(3):
#         print("正在写代码%s"%threading.current_thread()) #查看当前线程名称
#         time.sleep(1)
# def drawing():
#     for x in range(3):
#         print("正在画图%s"%threading.current_thread())
#         time.sleep(1)
# def main():
#     t1 = threading.Thread(target=coding) #使用多线程方式
#     t2 = threading.Thread(target=drawing)
#     t1.start()
#     t2.start()
#     print(threading.enumerate()) #查看当前的线程数


#继承threading多线程类 进行自定义多线程
class CodingThread(threading.Thread):
    def run(self):  #必须使用run方法
        for x in range(3):
            print("正在写代码%s"%threading.current_thread()) #查看当前线程名称
            time.sleep(1)

class DrawingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print("正在画画%s"%threading.current_thread()) #查看当前线程名称
            time.sleep(1)

def main():
    t1 = CodingThread() #使用创建类创建线程
    t2 = DrawingThread()

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()