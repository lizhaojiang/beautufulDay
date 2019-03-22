import os

stu_list = []

def show_menu():
    print("-----学生管理系统-----")
    print("1·添加学生信息")
    print("2·删除学生信息")
    print("3·修改学生信息")
    print("4·查询学生信息")
    print("5·显示所有学生")
    print("6·保存信息并退出")

#添加学生信息
def add_stu_info():
    stu_info = {}
    name = input("请输入学生姓名:")
    age = input("请输入学生的年龄")
    sex = input("请输入学生的性别")

    stu_info['name'] = name
    stu_info['age'] = int(age)
    stu_info['sex'] = sex

    stu_list.append(stu_info)

#显示所有学生信息
def show_all_info():
    for index,value in enumerate(stu_list):
        stu_no = index +1
        print("学号:%d,姓名:%s,年龄:%d,性别:%s"%(stu_no,value['name'],value['age'],value['sex']))

#删除学生信息
def del_stu_info():
    num = int(input("请输入要删除的学生的学号:"))
    index = num-1
    if index>=0 and index<len(stu_list):
        result = stu_list.pop(index)
        # del stu_list[index]
        print("删除的学生的学号:%d,姓名:%s,年龄:%d,性别:%s"%(index+1,result['name'],result['age'],result['sex']))
    else:
        print("请输入正确的学号")

#修改学生的信息
def update_stu_info():
    num = int(input("请输入要修改的学生的学号:"))
    index = num-1
    if index>=0 and index<len(stu_list):
        name = input("请输入修改后的姓名:")
        age = input("请输入修改后的年龄:")
        sex = input("请输入修改后的性别:")

        stu_list[index]['name'] = name
        stu_list[index]['age'] = int(age)
        stu_list[index]['sex'] = sex
    else:
        print("请输入正确的学号")


#查询学生信息
def search_stu():
    name = input("请输入要查询的学生的姓名:")
    for index,value in enumerate(stu_list):
        if value['name'] == name:
            print("找到了")
            print("学生的学号:%d,学生的姓名:%s,学生的年龄:%d,学生的性别:%s"%(index+1,value['name'],value['age'],value['sex']))

            break
    else:
        print("没有找到你查询的信息")


#保存学生的信息到文件中
def save_stu_info():
    file = open('stu_info.data','w',encoding='utf-8')
    #把列表转换为字符串
    stu_list_str = str(stu_list)
    #把字符串列表数据写入到文件中
    file.write(stu_list_str)
    file.close()
#文件加载
def load_stu_info():
    #首先判断文件或者文件夹是否存在
    if os.path.exists('stu_info.data'):
        file = open('stu_info.data','r',encoding="utf-8")
        #读取文件的信息
        file_content = file.read()
        #将读取出来的信息,使用eval转换为原来的数据类型
        new_stu_list = eval(file_content)
        #将读取出来的信息添加到列表中,供程序使用
        stu_list.extend(new_stu_list)
        file.close()


def run():
    load_stu_info()

    while True:
        show_menu()
        menu_no = input("请输入您要操作的选项:")
        if menu_no == '1':
            print("添加学生")
            add_stu_info()
        if menu_no == '2':
            print("删除学生")
            del_stu_info()
        if menu_no == '3':
            print("修改学生")
            update_stu_info()
        if menu_no == '4':
            print('查询学生')
            search_stu()
        if menu_no == '5':
            print("显示所有学生信息")
            show_all_info()
        if menu_no == '6':
            save_stu_info()
            print('保存信息退出')
            break

run()

















