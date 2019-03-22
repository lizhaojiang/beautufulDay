#在房子里面存放家具
class Home(object):
    def __init__(self,area):
        #房子的可用面积
        self.area = area
        self.furniture_list = []

    #添加家具
    # def add_furniture(self,furniture):
    #     #判断房子的面积是否大于家具的面积
    #     if self.area > furniture.area:
    #         #如果房子面积大于家具的面积,则把家具添加到列表中
    #         self.furniture_list.append(furniture)
    #         self.area -= furniture.area
    #
    #         print("添加家具成功",furniture)
    #     else:
    #         print("添加失败,房子的可用面积为:%d 家具的可用面积为:%d"%(self.area,furniture.area))


    def __str__(self):
        if self.furniture_list:
            #获取房间中的所有数据
            #1\使用列表推导式
            # new_furniture_list = [value.name for value in self.furniture_list]
            # print(new_furniture)
            #2\使用map函数
            new_furniture_list = list(map(lambda x:x.name,self.furniture_list))
            new_furniture_list = ",".join(new_furniture_list)
            # print(new_furniture_list)
            return "房子的可用面积为:%s 家具有:%s" % (self.area, new_furniture_list)
        return "房子的可用面积为:%s"%self.area


class Furniture(object):
    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        return f"家具的名字:%s 家具的面积:%d"%(self.name,self.area)

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"工人的名字:%s 工人的年龄:%d"%(self.name,self.age)

    # 添加家具
    def add_furniture(self, furniture,home):
        # 判断房子的面积是否大于家具的面积
        if home.area > furniture.area:
            # 如果房子面积大于家具的面积,则把家具添加到列表中
            home.furniture_list.append(furniture)
            home.area -= furniture.area

            print("添加家具成功", furniture)
        else:
            print("添加失败,房子的可用面积为:%d 家具的可用面积为:%d" % (home.area, furniture.area))




home = Home(200)
person = Person("小明",25)
bed = Furniture("席梦思",5)

person.add_furniture(bed,home)


tv = Furniture("小米",4)
person.add_furniture(tv,home)
print(home)




