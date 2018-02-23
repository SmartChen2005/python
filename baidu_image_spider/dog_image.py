'''
dog_image.py
爬取百度上的金毛照片

2018.2.22
Smart Chen @MacTrick
'''

from urllib.request import *
#用来处理网络访问
import re

url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%87%91%E6%AF%9B&oq=%E9%87%91%E6%AF%9B&rsp=-1'
html = urlopen(url)#用来打开一个网页
#html代码
obj = html.read().decode()#获取html代码并解码
urls = re.findall(r'"objURL":"(.*?)"',obj) #->列表

index = 1
for url in urls:
	try:
		print("Downloading···%d"%index)
		#相对路径保存
		urlretrieve(url,'img-'+str(index)+'.jpg')
	except:
		print("Download Error...%d"%index)
		index+=1
	else:
		print("Download Compelete...%d"%index)
		index+=1
