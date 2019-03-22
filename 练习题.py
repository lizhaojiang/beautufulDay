#1.输入n个整数x,y,z,... 请把这n个数由小到大输出
# num_list = []
# while True:
#     num = input("输入整数:")
#     # print(num_list)
#     #如果没有输入文件,直接回车则退出
#     if len(num) == 0:
#         break
#     num_list.append(int(num))
#     num_list.sort()
# for x in num_list:
#     print(x ,end="")

#2.编写一个在python3实现的程序，实现计算器加减乘除的功能，并输出，利用函数实现。
# def jisuan():
#     print("请分别输入两个数,并选择计算的方式")
#     print("""
#         1|相加
#         2|相减
#         3|相乘
#         4|相除
#             """)
#     global a
#     a = int(input("请输入第一个数:"))
#     global b
#     b = int(input("请输入第二个数:"))
#
# def sum():
#     return a+b
# def jian():
#     return a-b
# def cheng():
#     return a*b
# def chu():
#     return a/b
#
# def num_cale():
#     jisuan()
#     num = int(input("请选择要计算的方式:"))
#     if num in range(1,5):
#         if num == 1:
#             print("%d + %d = %d"%(a,b,sum()))
#         if num == 2:
#             print("%d - %d = %d"%(a,b,jian()))
#         if num == 3:
#             print("%d * %d = %d"%(a,b,cheng()))
#         if num == 4:
#             print("%d / %d = %d"%(a,b,chu()))
#     else:
#         print("输入有误,请输入1-4对应的计算方式")
#         num_cale()
# num_cale()

#3．编写一个在Python3解释器中运行的程序，输出s的值，s =a+aa+aaa+aaaa+aaaaa,其中a是一个个位数。




"""
8.给定两个list ,A = [1,2,3,4,5,6,7,1,2,3]和B=[4,5,6,7,8,9,10,9,8,11],请用python找出A,B
中相同的元素放入列表D中，找出A,B中不同的元素放入列表C中，确保C、D两个列表中的元素不重复（用代码实现）：
"""
# a = [1,2,3,4,5,6,7,1,2,3]
# b = [4,5,6,7,8,9,10,9,8,11]
#
# c = []
# d = []
#
# for x in a:
#     if x in b:
#         c.append(x)
#     else:
#         d.append(x)
# for y in b:
#     if y in a:
#         c.append(y)
#     else:
#         d.append(y)
#
# for num in c:
#     if c.count(num)>=2:
#         a = c.index(num)
#         del c[a]
# for num in d:
#     if d.count(num)>=2:
#         a = d.index(num)
#         del d[a]
#
# print(c)
# print(d)

# num = input("请输入:")
#
# print(num,type(len(num)))


# print(eval(input("请输入一个式子:")))

