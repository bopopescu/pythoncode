import package1.Nameclass
nameclass = package1.Nameclass.Nameclass 
#引用文件类单继承示例
class student():
    grade = ''
    def __init__(self,name,age,weight,grade):
        #调用父类的构函
         nameclass.__init__(self,name,age,weight)
         self.grade = grade
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name,self.age,self.grade))

#实例化
s = student("wortliu",27,2017,1)
s.speak()
