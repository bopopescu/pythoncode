#encoding=utf-8
import pymysql   
import json

conn = pymysql.connect(host='localhost',
        port = 3306,
        user='wort',
        passwd='wort',
        db ='wortliudb',
        charset='utf8')
cur = conn.cursor()

#创建数据表
#cur.execute("create table student(id int ,name varchar(20),class
#varchar(30),age varchar(10))")

#插入一条数据
#n = 50
#sum = 0
#counter = 1
#while counter <= n:
#    u = ("INSERT INTO
#    `wortliudb`.`username`(`Id`,`UserName`,`Gender`,`Position`)VALUES('" +
#    str(sum + 1) + "','测试" + str(sum + 1) + "','我是第" + str(sum + 1) +
#    "号','这是第" + str(sum + 1) + "个')")
#    cur.execute(u)
#    sum = sum + counter
#    print(counter)
#    counter += 1

#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
#cur.execute("delete from student where age='9'")


#查询
sql = "select * from `wortliudb`.`username`"
cur.execute(sql)
results = cur.fetchall()


#将结果集转为json 必须引入 import json
# item=json.dumps(results)
# data3 = json.loads(item)
#print(" ID UserName Gender Position")
for x in results:
    print(" " + str(x[0]) + " " + str(x[1]) + " " + str(x[2]) + " " + str(x[3]) + " ")
cur.close()
conn.commit()
conn.close()