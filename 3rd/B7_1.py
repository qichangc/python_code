#!/usr/bin/python
#coding:utf-8

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]

def myfoo(a,b):
    print map(None,list1,list2)

myfoo(list1,list2)
