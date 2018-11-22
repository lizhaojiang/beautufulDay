import threading

####进程锁一般只用到修改了全局变量的情况下
VALUE = 0

gLock = threading.Lock() #进程锁 保证数据的完整性

def add_value():
    global VALUE
    gLock.acquire() #给进程上锁
    for x in range(1000000):
        VALUE += 1
    gLock.release() #释放锁
    print("value:%d"%VALUE)

def main():
    for x in range(2):
        t = threading.Thread(target=add_value)
        t.start()

if __name__ == '__main__':
    main()