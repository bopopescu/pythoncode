from ClassPackage.mysqlhelp import db,User,UserNameList
import json
class DbModel(object):
    def SelectAll():
        userlist = UserNameList.query.all() 
        html = []
        for item in userlist:
            html.append(item.UserName)
        print(html) #查询结果输出
'''
username 表数据添加
'''
class UserNameModel():
    def UserNameTabAdd(Id,UserName,Gender,Position):
        u = UserNameList(Id=Id,UserName=UserName,Gender=Gender,Position=Position)
        db.session.add(u)
        db.session.commit()
    def UserNameTabDel(Id):
        un = UserNameList.query.get(Id)
        db.session.delete(un)
        db.session.commit()

