#!/usr/bin/env python
# coding: utf-8
'''
@File   :run.py
@Author :youxinweizhi
@Date   :2020/7/16
@Github :https://github.com/youxinweizhi
'''
from flask import Flask,request,make_response,jsonify
import os,json

app=Flask(__name__)
#读取配置文件
app.config.from_object('settings.Dev')

#获取认证文件
@app.route('/aligenie/<name>',methods=['GET'])
def auth(name):
    base_dir = os.path.dirname(__file__)
    resp = make_response(open(os.path.join(base_dir,'aligenie',name)).read())
    resp.headers["Content-type"]="text/plan;charset=UTF-8"
    return resp


#天猫自定义技能
@app.route('/skill/',methods=['POST'])
def skill():
    #固定响应格式
    RETURN_DATA = {
        "returnCode": "0",
        "returnErrorSolution": "",
        "returnMessage": "",
        "returnValue":
            {"reply": "",
             "resultType": "RESULT",
             "actions":
                 [{"name": "audioPlayGenieSource",
                   "properties": {"audioGenieId": "123"}}],
             "properties": {},
             "executeCode": "SUCCESS",
             "msgInfo": ""
             }
    }
    
    #技能判断、响应技能
    if request.method=="POST":
        res_data=request.data.decode()
        res_data=json.loads(res_data)
        print(res_data)
        if res_data['skillName']=="扇贝物联":
            RETURN_DATA['returnValue']['reply'] = "哈哈哈，我是扇贝物联（bigiot.xyz），一个可以用天猫点灯的物联网平台"
        elif res_data['skillName']=="自定义技能":
            pass   #通过技能名响应不同的技能
        else:
            RETURN_DATA['returnValue']['reply'] = "技能不存在，或暂时无法查询！"
    return jsonify(RETURN_DATA)
if __name__ == '__main__':
    app.run(host='0.0.0.0')
