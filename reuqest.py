# coding:utf-8

from flask import Flask,request

app=Flask(__name__)

@app.route('/index',methods=['GET','POST'])
def index():
    #request中包含了前端发送过来的所有请求数据
    #form 和 data 是用来提取请求体数据
    #通过request.form可以直接提取请求体中的表单格式的数据，是一个类字典的对象
    #通过get方法只能拿到多个同名参数的第一个
    name=request.form.get('name')
    age=request.form.get('age')

    name_li=request.form.getlist('name')
    print ('request.data:%s' % request.data)

    #args是用来提取url中的参数（查询字符串）
    city=request.args.get('city')
    return 'hello name=%s,age=%s,city=%s,name_li=%s'% (name,age,city,name_li)

if __name__== '__main__':
    app.run(debug=True)