print('Hello World!')
import pymysql
#连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306,user='root',passwd='123456',database='python0302',charset='utf8')
# 2.创建游标
cursor = conn.cursor()
#3.写sql语句
sql = "select * from S"
#4.执行sql
cursor.execute(sql)
#5.查询语句，.fetchmany可以选择查询几条
result = (cursor.fetchmany(3))
