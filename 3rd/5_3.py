#!/usr/bin/python
#coding:utf-8
"""
日志文件抽取搜狗的不重复IP
生成器实现
"""


def myfun(filename):
    myfile = open(filename,"r")
    
    for line in myfile:
    	index = line.find('"Sogou web spider')#查找是否有这一行，没有则返回-1
    	if index > 0:	#a[:-1] 相当与a[:] 所以要判断
    	    line = line[:index].strip()	#去空格
  	    yield line			
    


filename = "ip.txt"
p = myfun(filename)	#返回的是一个生成器对象
mylist = sorted(list(set(list(p))))#把生成器转换成列表，然后去重，然后再转换成列表，最后排序
print mylist
