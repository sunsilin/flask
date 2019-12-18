#coding:utf-8

from flask import Flask,request

app=Flask(__name__)

@app.route('/upload',methods='POST')
def upload():
    '''接受前端传过来的文件'''
    file_obj=request.files.get('pic')
    if file_obj is None:
        #表示没有发送文件
        return '未上传文件'

    file_obj.save('./demo.png')
    return '上传成功'




if __name__=='__main__':
    app.run(debug=True)