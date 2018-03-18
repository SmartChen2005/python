"""
Copyright 2017 by Smart Chen
2017.10.21
"""

#定义函数pi
def pi():
	num = int(input("输入精确度："))
	if isinstance(num,int) and num>0:
		y = 0
		c = 0
		while num != 0:
			if y == 1:
				c = c+1/(2*num-1)
				num = num-1
				y = 0
			else:
				c = c-1/(2*num-1)
				num = num-1
				y = 1
		c = c*4
		print("π≈"+str(abs(c)))
	else:
		print("请输入大于0的整数！")
		pi()

#重复运行函数pi
while True:
	pi()
