#coding:utf-8

from flask import Flask,abort,Response,request,make_response
app = Flask(__name__)

@app.route('/index')
def index():
    #1:使用元组，返回自定义的响应信息
    #       响应体        状态码      响应头
    # return 'index page' , 400 , [('city','beijing'),('itcase','python')]
    # 2: 响应体可以使用字典的形式
    # return  'index page' , 400, {"city":"beijing","itcase":"python"}
    # 3：状态码可以改成其他 例如 666
    # return  'index page' , 666, {"city":"beijing","itcase":"python"}
    # 4：状态码中可以加说明
    # return  'index page' , "666 itcast status", {"city":"beijing","itcase":"python"}
    # 5:后面的响应头可以不写 到那时状态码不可以不写
    # return  'index page' , "666 itcast status"


    # 6：使用make_response 来构造响应的信息
    res=make_response('index page 2')
    res.status='999 itcast'#设置状态码
    res.headers['city']='beijing'
    return res



if __name__=='__main__':

    app.run(debug=True)