# -*- coding: utf-8 -*-
# @Author   : LaiJiahao
# @Time     : 2022/12/16 10:29
# @File     : index.py
# @Project  : aliyun-openAI


from flask import Flask,request,jsonify
from openai import OpenAi
import json



ai = OpenAi()

app = Flask(__name__)

@app.route('/',methods= ['POST'])
def get_answer():
    try:
        data = json.loads(request.data)
        prompt = data['prompt']

        try:
            answer = ai.get_answer(prompt=prompt)

            msg = {
                "code": 200,
                "msg": answer
            }
            return jsonify(msg)

        except Exception as e:

            msg = {
                'code': 400,
                'error': repr(e),
                'msg':'出现意外的错误，请联系开发者等会再问我吧！'
            }
            return jsonify(msg)


    except:
        msg = {
            'code': 404,
            'msg': '服务器端出现问题，请检查！'
        }

        return jsonify(msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000)
