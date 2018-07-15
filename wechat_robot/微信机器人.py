#coding=utf8
import requests
import itchat

def get_response(msg):
    apiUrl='http://www.tuling123.com/openapi/api'
    data={
        'key':'9a7a5493e74e4e789463bee32a4af567',
        'info':msg,
        'userid':'wechat-user',
    }
    try:
        r=requests.post(apiUrl,data=data).json()
        return r.get('text')
    except:
        return

#接收到好友的消息时...
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply#机器人出错时回复defaultReply

def lc():
    print('finish login')
def ec():
    print('exit')
itchat.auto_login(hotReload=True,loginCallback=lc,exitCallback=ec)
itchat.run()