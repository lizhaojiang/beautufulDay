import pymysql

conn = pymysql.connect(host='localhost',user='root',password='123456',database='pymysql_demo',port=3306)

cursor = conn.cursor()

#插入数据
# sql = """
# insert into user(username,age,password) values("张婕",25,"zhangjie1007")
# """
# cursor.execute(sql)
# conn.commit()

#查询数据 fetchone(查询一条) fetchall(查询所有符合条件的数据) fetchmany(int) 查询指定条数的数据
# sql = """
# select * from user
# """
# cursor.execute(sql) #执行sql语句
# resutls = cursor.fetchall()
#
# # for result in resutls:
# #     print(result)
# print(resutls)
# conn.close()

#删除数据
# sql = """
# delete from user where id=1
# """
# cursor.execute(sql)
# conn.commit() #执行 增\删\改 都需要执行此操作


#更新数据
sql = """
update user set username="李兆江" where id=2
"""
cursor.execute(sql)
conn.commit()



conn.close()