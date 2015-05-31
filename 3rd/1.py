#!/usr/bin/python
#coding:utf-8
"""
写一个函数实现以下功能
找出一个列表的中位数，列表的元素都是浮点数。
列表中的元素个数为奇数：比喻L =[15.0, 5.3, 18.2], returns 15.0. 返回中位数
列表中的元素个数为偶数：比喻L =[1.0, 2.0, 3.0, 4.0], returns 2.5. 返回中间2位数之和/2
"""

mylist = [2.4,1.2,3.5,0.1]

mylist2 = [2.4,1.2,3.5,0.1,3.2]

def myfun(clist):
    clist =  sorted(clist)
    clen = len(clist)
    if clen%2 != 0:
	return clist[(clen-1)/2]
    else:
	return (clist[clen/2]+clist[clen/2-1])/2

print myfun(mylist)
print myfun(mylist2)
