#!/usr/bin/python
#coding:utf-8

def my_max2(*a):
    
    if len(a) == 1:
	b = list(a[0])	
    else:
	b = list(a)
    b = sorted(b)
    return b[-1]

def my_min2(*a):
    
    if len(a) == 1:
	b = list(a[0])	
    else:
	b = list(a)
    b = sorted(b)
    return b[0]

print my_max2(1,2,5,1,2,8,4,6)
print my_max2("abwfewgf")

print

print my_min2(1,2,5,1,2,8,4,6)
print my_min2("abwfewgf")



