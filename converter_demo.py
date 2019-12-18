#coding=utf-8
from flask import Flask,current_app,redirect,url_for
from werkzeug.routing import BaseConverter
# import demo
#创建flask应用对象
# __name__表示当前的模块名字
app = Flask(__name__)

#转换器
# @app.route('/goods_detail/<int:goods_id>')
@app.route('/goods_detail/<goods_id>')#不加转换器类型 默认是普通的字符串规则 （除了/的字符
def goods_detail(goods_id):
    return 'goods detail page %s' % goods_id

#自定义转换器
# 举例手机号

# 1：定义自己的转化器
class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        #调用父类的初始化方法
        super(RegexConverter,self).__init__(url_map)
        #将正则表达式的参数保存到对象的属性中，flask会去使用这个属性来进行路由的正则匹配
        self.regex = regex
    def to_python(self, value):
        #value时在路径进行正则表达式匹配的时候提取的参数
        return  value
    def to_url(self, value):
        '''使用url_for的方式的时候被调用'''
        return value

# 2:将自定义的转换器添加到flask的应用中
app.url_map.converters['re']=RegexConverter

# 3:使用
# 127.0.0.1：5000/seed/18612345678

@app.route("/send/<re(r'1[34578]\d{9}'):mobile_num>")
def send_sms(mobile_num):
    return 'send sms to %s' % mobile_num

@app.route('/index')
def index():
    url=url_for('send_sms',mobile_num='18611111111')
    return redirect(url)






if __name__=="__main__":
    #
    print(app.url_map)
    #启动flask程序
    app.run(debug=True)







