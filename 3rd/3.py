#!/usr/bin/python
#coding:utf-8
import string
"""
gettysburg.txt是一个文件文件，请用函数，list,dict,文件读写等知识分析该文本文件中单词个数（输出所有单词，并输出个数），输出不重复的单词和个数， 统计每个单词出现的次数，并输出单词和出现次数的表
"""
def foo(filename):

    myfile = open(filename,"r")#打开文件
    mylist = []

    for line in myfile:
	line = line.strip("\n")#去掉每行结尾的回车符
	line = line.translate(None,string.punctuation)#去掉标点符号
	a = line.split(" ")#根据空格将这一行分隔为多个单词，返回一个列表，无法解决多个空格问题
	
	mylist += a
    while True:
	if "" in mylist:
	    mylist.remove("")#为了解决多个空格问题，手动去掉列表中的“”元素
	else:
	    break

    mylist = sorted(mylist)#将列表排序

    print "All words are:\n"
    for word in mylist:
	print word,

    mylen = len(mylist)
    print "\n"
    print "The number of all words are: ",mylen
    print

    newlist = list(set(mylist))#去掉列表中重复的元素
    print "All words are (without repetition):\n"
    newlist = sorted(newlist)

    for word in newlist:
	print word,

    print "\n"
    print "The number of all words are (without repetition): ",len(newlist)
    print
    mydic = {}
    for word in newlist:
	mydic[word] = mylist.count(word)#得出列表中重复元素的个数
    diclist =  sorted(mydic.iteritems(),key=lambda fun:fun[1])#按照字典的键值来排序，返回的是一个列表
    print "====\t\t============="
    print "word\t\ttimes of word"
    print "====\t\t============="
    for item in diclist:
	print "%s\t\t%s"%(item[0],mydic[item[0]])#item是一个元组




filename = "gettysburg.txt"
foo(filename)

