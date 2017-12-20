import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

'''配置数据库'''
app = Flask(__name__)
app.config['SECRET_KEY'] = 'wortliu'
#连接url说明：mysql://username:password@hostname/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://wort:wort@localhost:3306/wortliudb?charset=utf8'
#设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  
db = SQLAlchemy(app)  


class User(db.Model):  
    """定义数据模型"""  
    __tablename__ = 'user'  
    id = db.Column(db.Integer, primary_key=True)  
    username = db.Column(db.String(80), unique=True)  
    email = db.Column(db.String(120), unique=True)  
  
    def __init__(self, username, email):  
        self.username = username  
        self.email = email

class UserNameList(db.Model):
    """定义实体"""
    __tablename__ = "username"
    Id = db.Column(db.Integer, primary_key=True)  
    UserName = db.Column(db.String(500), unique=True)  
    Gender = db.Column(db.String(45), unique=True)  
    Position = db.Column(db.String(45), unique=True)  
    def __init__(self,Id,UserName,Gender,Position):
        self.Id = Id
        self.UserName = UserName
        self.Gender = Gender    
        self.Position = Position