path='/Users/smartchen/Desktop/Walden.txt'
#这里替换为Walden.txt的存储路径

with open(path,'r') as text:
	words=text.read().split()#读文件
	for word in words:
		print('{} -{} times'.format(word,words.count(word)))
		#用count统计重复出现的单词
