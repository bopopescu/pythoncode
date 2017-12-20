import package1.SqlHelp
import _winapi
helps = package1.SqlHelp.SqlHelp

class UserList():
        def SelectDB():
            sqlh = helps("select","username")
            results = sqlh.SqlConnection()
            print("     ID       UserName        Gender      Position")
            for x in results: 
                 print("    " + str(x[0]) + "        " + str(x[1]) + "       " + str(x[2]) + "       " + str(x[3]) + "   ") 
        
x = UserList
x.SelectDB()
