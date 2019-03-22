#定义一个家类:
class Home(object):
    def __init__(self,area):
        self.area = area #房间的面积
        self.containsItem = [] #房间存放的物品

    def __str__(self):
        msg = "当前房间可用面积:" + str(self.area)
        if len(self.containsItem) > 0:
            msg = msg + "容纳的物品有:"
            for temp in self.containsItem:
                msg = msg + temp.getName() + ","

            msg = msg.strip(",")

        return msg

    #可容纳的物品
    def accommodateItem(self,item):
        #如果可用面积大于物品的占用面积
        needArea = item.getUserArea()
        if self.area > needArea:
            self.containsItem.append(item)
            self.area -= needArea
            print("物品已经存放倒房间中")
        else:
            print("err:房间的可用面积为:%d,但是要放的物品的面积为:%d"%(self.area,needArea))

#定义一个床类
class Bed(object):
    def __init__(self,area,name="床"):
        self.area = area
        self.name = name

    def __str__(self):
        msg = "床的面积为:" + str(self.area)
        return msg

    #获取床的面积
    def getUserArea(self):
        return self.area

    def getName(self):
        return self.name

#创建一个新家
newHome = Home(100)
print(newHome)

#创建一个床对象
newBed = Bed(30)
print(newBed)

#把床放到家里
newHome.accommodateItem(newBed)
print(newHome)

#创建一个床对象
newBed2 = Bed(20,"席梦思")
print(newBed2)

#把床放到家里
newHome.accommodateItem(newBed2)
print(newHome)














