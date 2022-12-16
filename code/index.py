# -*- coding: utf-8 -*-
# @Author   : LaiJiahao
# @Time     : 2022/12/15 23:26
# @File     : index.py
# @Project  : 阿里云部署版本
# @desc     :

from flask import Flask,request,jsonify
from openai import OpenAi
import json
from config import configs
from concurrent.futures import ThreadPoolExecutor
from RecordLog import Flask_Log,System_Log

t = ThreadPoolExecutor(max_workers=500)
a = OpenAi()


app = Flask(__name__)

@app.route('/get_answer',methods= ['POST'])
def get_answer():
    try:
        data = json.loads(request.data)
        prompt = data['prompt']
        #IP限制
        user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

        try:

            ai = t.submit(a.get_answer,prompt=prompt,max_tokens=configs['max_tokens'],temperature=configs['temperature'])
            answer = ai.result(timeout=120)
            msg = {
                "code": 200,
                "msg": answer
            }

            success_logs = {'prompt': prompt, 'ip': user_ip}
            Flask_Log('chatgpt.log', 'a+', msg['code'], success_logs)
            return jsonify(msg)

        except Exception as e:

            msg = {
                'code': 400,
                'error': repr(e),
                'msg':'出现意外的错误，请联系开发者等会再问我吧！'
            }

            failure_log = {'prompt': prompt, 'ip': user_ip , 'error': msg['error']}
            Flask_Log('chatgpt.log', 'a+', msg['code'], failure_log)

            return jsonify(msg)


    except:
        msg = {
            'code': 404,
            'msg': '服务器端出现问题，请检查！'
        }

        System_Log('error.log','a+')
        return jsonify(msg)

if __name__ == '__main__':
    if configs['keys']:
        app.run(host='0.0.0.0',port=1216)
    else:
        print('请配置你的Keys')

