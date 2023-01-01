# -*- coding: utf-8 -*-
# @Author   : LaiJiahao
# @Time     : 2022/12/16 10:29
# @File     : openai.py
# @Project  : aliyun-openAI

import requests
import markdown

class OpenAi:
    def __init__(self):
        # 使用的模型:功能最强大的 GPT-3
        self.model = "text-davinci-003"
        self.url = "https://api.openai.com/v1/completions"
        # 替换为你的api_key <https://beta.openai.com/account/api-keys>
        self.keys = "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"
        # 这个是设置回答的长度,最大可以设置到4096 (免费额度为$18,该值影响你的用量)
        self.max_tokens = 40
        # 值越高意味着模型将承担更多风险。对于更具创造性的应用程序，请尝试 0.9,建议0.5-0.6
        self.temperature = 0.5
    def get_answer(self,prompt):
        api_key = self.keys
        if self.max_tokens <= 4096 and self.temperature <= 0.9:
            if prompt:
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}"
                }

                # Set up the API data
                data = {
                    "model": "text-davinci-003",
                    "prompt": prompt,
                    "max_tokens": self.max_tokens,
                    "temperature": self.temperature,
                }
                # Make the API request
                response = requests.post(self.url, headers=headers, json=data)

                # Print the response

                answer = response.json()['choices'][0]['text']
                answer = markdown.markdown(answer)
            else:
                answer= "问题不能为空"
        else:
            answer = '你的max_tokens或temperature值过大！'
        return answer

# ai = OpenAi()
# print(ai.get_answer(prompt='你好'))