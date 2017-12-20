class Nameclass:
  #定义基本属性
     name = ''
     age = 0
     #定义私有属性,私有属性在类外部无法直接进行访问
     weight = 0
  #"""一个简单的类实例"""
     def __init__(self, a, b,c):
        self.name = a
        self.age = b
        self.weight = c
     def FunctionName(self,name,age):   
        print(self.name + '------' + str(self.age))
#x = Nameclass("wortliu",27,2017)
#x.FunctionName("wortliu",27)
#print("构造函数输出内容：%s今年 %d 岁" % (x.name,x.age))



'''
#同文件继承
class student(Nameclass):
    grade = ''
    def __init__(self,a,b,c,d):
        #调用父类的构函
        Nameclass.__init__(self,a,b,c)
        self.grade = d
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我 %d年在读 %d 年级" % (self.name,self.age,self.weight,self.grade))

s = student("wortliu",27,2017,1)
s.speak() 
'''