#!/usr/bin/python
#coding:utf-8

def test():
    i = 2
    print i
    i += 1
    def test2():
	print i
    return test2
	
test()()
