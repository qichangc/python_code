#!/usr/bin/python
#coding:utf-8



def tran(minute):
    hour = minute/60
    min = minute%60
    print "%shour(s) %sminute(s)"%(hour,min)

minutes = 142
tran(minutes)

