#瓦尔登湖词频统计
#Smart Chen@MacTrick
#2018.7.7

import string
"""
引入了一个新的模块string
其实这个模块的用法很简单
我们可以试着把string.punctuation打印出来
其实这里面也仅仅是包含了所有的标点符号(如下)
!"#$%&'()*+,-./:;<=>?@[]^_`{|}~
"""

path='/Users/smartchen/Desktop/Walden.txt'

with open(path,'r') as text:
	words=[raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
	"""
	在文字的首位去掉了连在一起的标点符号
	并把首字母大写的单词转化成小写
	"""
	words_index=set(words)
	"""
	将列表用set函数转换成集合
	自动去除掉了其中所有重复的元素
	"""
	counts_dict={index:words.count(index) for index in words_index}
	"""
	将列表用set函数转换成集合
	自动去除掉了其中所有重复的元素
	"""
for word in sorted(counts_dict,key=lambda x: counts_dict[x],reverse=True):
	print('{} -- {} times'.format(word,counts_dict[word]))
	"""
	打印整理后的函数
	其中key=lambda x:counts_dict[x]叫做lambda表达式
	可以理解为以字典中的值为排序的参数
	"""
