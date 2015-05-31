#!/usr/bin/python
#coding:utf-8
"""
日志文件抽取搜狗的不重复IP
过程化实现
"""
filename = "ip.txt"
myfile = open(filename,"r")
iplist = []
for line in myfile:
    index = line.find('"Sogou web spider')
    if index > 0:
    	line = line[:index].strip()
  	iplist.append(line)
print sorted(list(set(iplist)))
