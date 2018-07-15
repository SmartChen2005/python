#coding=utf8
import itchat

#登录微信
#登陆完成后的方法需要赋值在loginCallback中
#而退出后的方法需要赋值在exitCallback中
def lc():
    print('finish login')
def ec():
    print('exit')
itchat.auto_login(hotReload=True,loginCallback=lc,exitCallback=ec)

#按昵称搜索微信好友
friend=itchat.search_friends(nickName="陈飞")[0]#搜索到的列表中的第一项
#发送消息
friend.send('测试消息发送')

#退出登录(若程序持续工作则不需要此代码，手动退出即可)
itchat.logout()