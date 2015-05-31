#!/usr/bin/python
#coding:utf-8
"""
日志文件抽取搜狗的不重复IP
函数实现
"""
def myfun(filename):
    myfile = open(filename,"r")
    iplist = []
    for line in myfile:
    	index = line.find('"Sogou web spider')
    	if index > 0:
            line = line[:index].strip()
  	    iplist.append(line)
    return  sorted(list(set(iplist)))


filename = "ip.txt"
print myfun(filename)
