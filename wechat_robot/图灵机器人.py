#coding=utf8
import requests

print("机器人:你好，我是MacTrick公众号的学习Python专属机器人")
apiUrl = 'http://www.tuling123.com/openapi/api'
while 1:
	text=input("我:")
	data = {
		#小编为你们建立的机器人账号的密钥
	    'key':'9a7a5493e74e4e789463bee32a4af567',
	    'info':text,#发送内容文本
	    'userid':'python_user',
	}
	#我们通过如下命令发送一个post请求
	r=requests.post(apiUrl,data=data).json()
	
	#r如下
	#{'code': 100000, 'text': 'B'}

	#打印返回值中的文本('text')
	print("机器人:"+r['text'])
