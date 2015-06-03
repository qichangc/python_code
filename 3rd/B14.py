#!/usr/bin/python
#coding:utf-8

def fib(n):
    if n in [1,2]:
	return 1
    else:
	return fib(n-1)+fib(n-2)

print fib(6)
