#coding=utf-8
from flask import Flask,current_app,redirect,url_for
# import demo

#创建flask应用对象
# __name__表示当前的模块名字
app = Flask(__name__)


@app.route("/")#路由
def index():
    '''定义视图函数'''
    return "hello word"

@app.route('/post_only',methods=['POST'])
def post_only():
    '''只能post访问'''
    return 'post only page'

@app.route('/hello',methods=['POST'])
def hello1():
    return 'hello 1'

@app.route('/hello',methods=['GET'])
def hello2():
    return 'hello 2'

@app.route('/hi1')
@app.route('/hi2')
def hi():
    return 'hi page'

@app.route('/login')
def login():
    #使用url_for的函数，通过视图函数的名字找到对应的url路径
    url = url_for('index')
    return redirect(url)

@app.route('/register')
def register():
    url=url_for('index')
    return redirect(url)




if __name__=="__main__":
    #
    print(app.url_map)
    #启动flask程序
    app.run(debug=True)







