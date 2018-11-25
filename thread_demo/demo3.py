import threading
import random
import time
#生产者和消费者模式

#定义一个全局变量
gMoney = 1000
#创建全局锁
gLock = threading.Lock()
#生产者生产总数
gTotleTime = 10
#记录生产次数
gTime = 0

#生产者
class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTime
        while True:
            money = random.randint(100,1000) #随机产生一个100到1000之间的数
            gLock.acquire() #创建锁
            if gTime >= gTotleTime:
                gLock.release()  # 释放锁
                break
            gMoney += money
            print("%s生产了%d元钱,剩余%d元钱"%(threading.current_thread(),money,gMoney))
            gTime += 1
            gLock.release() #释放锁
            time.sleep(0.5)



#消费者
class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100,1000) #随机产生一个100到1000之间的数
            gLock.acquire() #创建锁
            if gMoney >= money:
                gMoney -= money
                print("%s消费者消费了%d元钱,剩余%d元钱"%(threading.current_thread(),money,gMoney))
            else:
                if gTime >= gTotleTime:
                    gLock.release()
                    break
                print("%s消费者准备消费%d元钱,剩余%d元钱,不足!"%(threading.current_thread(),money,gMoney))
            gLock.release() #释放锁
            time.sleep(0.5)



def main():
    for x in range(3):
        t = Consumer(name="消费者线程%d"%x)
        t.start()

    for x in range(5):
        t = Producer(name="生产者线程%d"%x)
        t.start()


if __name__ == '__main__':
    main()