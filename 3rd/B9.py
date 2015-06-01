#!/usr/bin/python
#coding:utf-8


def average(lista):
    def add(x,y):
	return x+y
    return reduce(add,lista)/len(lista)

       
listnum = [1,2,3,4,5,1,3,8]
print average(listnum)
