import urllib.request
import urllib 
import json
'''
获取webapi数据接口json数据，转换为数组对象，传递到客户端
'''
class WebApi(object): 
     def ShowInfo():  
        req = urllib.request.Request("http://192.168.1.12:8444/api/QDLiveInformationModification/Getsystype")      
        response = urllib.request.urlopen(req)      
        the_page = response.read().decode("utf-8") 
        json_str = json.loads(the_page) #json转换object
        return json_str


