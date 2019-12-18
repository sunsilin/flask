#coding:utf-8
from flask import Flask,request,make_response

app=Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    resp=make_response('success')
    resp.set_cookie('itcast','python')
    resp.set_cookie('itcast1','python1')
    resp.set_cookie('itcast2','python2',max_age=3600)
    return resp

@app.route("/get_cookie")
def get_cookie():
    c = request.cookies.get("itcast")
    if c == None:
        return 'not found'
    return c


@app.route('/delete_cookie')
def delete_cookie():
    resp=make_response('delete success')
    #删除cookie
    resp.delete_cookie('itcast')
    return resp


if __name__=="__main__":
    app.run(debug=True)