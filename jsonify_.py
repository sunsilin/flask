#coding:utf-8
from flask import Flask,jsonify
import json

app = Flask(__name__)

@app.route('/index')
def index():
    data={
            'name':'zahngsan',
             'age':18
        }
#     # #json.dumps（字典）  将python的字典转换为接送字符串
#     # # json.loads(字符串)   将字符串转换为python中的字典
#     # json_str=json.dumps(data)
#     # return json_str,400,{'Content-Type':'application/json'}


#以上是以往的复杂的方式 flask中引入jsonify的操作方式
#jsonify帮助转为json数据，并设置响应头，Content-Type 为 application/json
    # return jsonify(data)

#另外一种方式 不用data  可以在里面直接传数据
    return  jsonify(city= 'beijing',county='china')

if __name__=='__main__':
    app.run(debug=True)