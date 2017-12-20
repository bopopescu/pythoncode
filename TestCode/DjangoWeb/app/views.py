"""
Definition of views.
""" 
import uuid
from ClassPackage.mysqlhelp import db,UserNameList
from ClassPackage.WebApi import WebApi
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext 
from pip._vendor.requests.api import request
from datetime import datetime
from flask import render_template 
from ClassPackage.TestModel import UserNameModel

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/index.html',
        {
            'title':'首页',
            'year':datetime.now().year,
        })
def ReturnContext():
    context = {}
    context['hello'] = '第一个数据列表展示.'
    context['ApiContent'] = '来自请求WebApi的数据列表.'
    context['userlist'] = UserNameList.query.limit(10) #返回数据到模板页
    context['datalist'] = WebApi.ShowInfo()  #返回WebApi数据到模板页
    return context
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(request,'app/contact.html',ReturnContext())

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/about.html',
        {
            'title':'数据添加',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
# 添加一条store信息
def add_store_info(request):
    Id = uuid.uuid1()
    UserName = request.POST['UserName']
    Gender = request.POST['Gender']
    Position = request.POST['Position']
    msg = ""
    try:
        UserNameModel.UserNameTabAdd(Id,UserName,Gender,Position)
        msg = "添加成功"
    except :
        msg = "添加失败"
    return render(request,'app/about.html',{'title':msg})
# 删除一条store信息
def delete_store_info(request): 
     Id = request.GET.get('Id')
     UserNameModel.UserNameTabDel(Id) 
     return render(request,'app/contact.html',ReturnContext())