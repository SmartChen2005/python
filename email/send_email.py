#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
send_email.py

2018.2.20
Smart Chen @MacTrick
'''

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
    
from_addr = input('您的邮箱: ')
password = input('邮箱密码: ')
to_addr = input('收件人邮箱: ')
smtp_server = input('SMTP服务器(一般为smtp.xxx.com,如smtp.163.com): ')

text = input("输入邮件内容(html或纯文本)：")
msg = MIMEText(text, 'html', 'utf-8')
name1 = input("您的称呼：")
msg['From'] = _format_addr('%s <%s>' % (name1,from_addr))
name2 = input("输入收件人的称呼：")
msg['To'] = _format_addr('%s <%s>' % (name2,to_addr))
header = input("输入邮件标题：")
msg['Subject'] = Header(header, 'utf-8').encode()

print("发送中。。。")

try:
    if smtp_server=='smtp.gmail.com':
        server = smtplib.SMTP(smtp_server, 587)
        server.starttls()
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        print("成功发送！")
    else:
        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        print("成功发送！")
except:
	print("呃呃呃。。。貌似哪里出了问题。。。")
