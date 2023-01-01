# aliyun-chatgpt 帮助文档

aliyun-chatpt是基于最近较火的chatgpt开发的一个项目，本项目代码十分简单，
通过简单调用openai的接口来实现功能，有如下的优点和缺点：

优点：
1. 调用不会受到chatgpt官网的限制
2. 个人使用大概只需要1个月更换一次key，且无需繁琐配置token
3. 阿里云函数首年免费，后续如果继续基于本项目使用，收费一天也不超过1块钱
4. 返回的字符数量和回答精度一定程度上可以自由设置

缺点：
1. 无法让AI继续，只能重新提问



## 前期准备
1. 使用该项目，请先开通阿里云[函数计算FC](https://www.aliyun.com/product/fc)
2. 将本项目fork，且提前修改好`openai.py`内的如下设置
```python
def __init__(self):
    # 替换为你的api_key <https://beta.openai.com/account/api-keys>
    self.keys = "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"
    # 这个是设置回答的长度,最大可以设置到4096 (免费额度为$18,该值影响你的用量)
    self.max_tokens = 40
    # 值越高意味着模型将承担更多风险。对于更具创造性的应用程序，请尝试 0.9,建议0.5-0.6
    self.temperature = 0.5
```

# 代码 & 预览
该项目基于: https://github.com/kjhuanhao/chatgpt-magic-plug
修改而来，原项目是油猴插件，您可以先进入该项目地址查看是否符合你的预期


## 部署 & 体验
文字部署教程：https://www.laijiahao.cn/posts/bb8fab97/

视频部署教程：待制作

部署完成之后，可以修改然后导入该项目的油猴脚本以获得完成体验：https://github.com/kjhuanhao/chatgpt-magic-plug/blob/main/oil_monkyjs.js



## 交流
- 如果有关于错误的反馈或者未来的期待，您可以通过以下几个方式联系
  - 本项目的`issues`
  - 作者邮箱：`mrlaijiahao@126.com`
  - 作者的B站：`mrhuanhao`

云函数研究的不多，欢迎大家一起开源，优化这个基础项目

## MIT开源协议

请遵循[MIT开源协议](https://github.com/kjhuanhao/chatgpt-magic-plug/blob/main/LICENSE)

