#!/usr/bin/python
#coding:utf-8


def myfoo(year):
    if year%100 != 0 and year%4 == 0:
	return year
    elif year%400 == 0:
	return year
    else:
	return
    
list1 = [2004,2000,1900,1988,1967,2008]

print filter(myfoo,list1)
