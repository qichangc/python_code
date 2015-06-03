#!/usr/bin/python
#coding:utf-8
import time
def testit(fun,*args,**kargs):
    starttime = time.time()
    res = fun(*args,**kargs)
    endtime = time.time()
    return (res, endtime-starttime)


def mult(x,y):
    return x*y

list1 = [i for i in range(1,11)]

print testit(reduce,mult,list1)


print  testit(reduce,lambda x,y:x*y,list1)

def foo(n):
    if n == 1:
	return 1
    else:
	return foo(n-1)*n

print testit(foo,10)
