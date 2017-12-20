import pymysql 
class SqlHelp():
    type = ''
    tabname = ''
    def __init__(self,type,tabname):
        self.type = type
        self.tabname = tabname
    def SqlConnection(self): 
        conn = pymysql.connect(host='localhost',
        port = 3306,
        user='wort',
        passwd='wort',
        db ='wortliudb',
        charset='utf8')
        cur = conn.cursor()
        #业务处理区
        if self.type == "select":
            sql = "select * from " + self.tabname
            cur.execute(sql)
            results = cur.fetchall()
            return results
        #业务处理区
        cur.close()
        conn.commit()
        conn.close()