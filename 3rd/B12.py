#!/usr/bin/python
#coding:utf-8
import time

def testit(fun,*args,**kargs):
    starttime = time.time()
    res = fun(*args,**kargs)
    endtime = time.time()
    return (res, endtime-starttime)

def test():
    func = (int, long, float)
    vals = (1234,12.34,"1234")

    for eachfunc in func:
	print '-'*20
	for eachval in vals:
	    resval = testit(eachfunc,eachval)
	    print resval

if __name__ == "__main__":
    test()

