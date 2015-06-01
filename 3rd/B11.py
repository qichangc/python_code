#!/usr/bin/python
#coding:utf-8
"""
Functional Programming with map(). Write a program that takes a filename and
"cleans" the file by removing all leading and trailing whitespace from each line. Read
in the original file and write out a new one, either creating a new file or overwriting
the existing one. Give your user the option to pick which of the two to perform.
Convert your solution to using list comprehensions.

"""

def choice():
    while True:
	input = raw_input("Write in a new file?\n")
	if input in ["y","Y","yes","YES","Yes"]:
	    return True
	elif input in ["N","n","NO","No"]:
	    return False
	else:
	    break

def rebnk(line):
    return line.strip()

def main(file):
    
    myline = open(file,"r")
    newline = map(rebnk,myline)
    myline.close()

    if choice():
	newfile = open("B11.newfile.txt","w")
	for line in newline:
	    newfile.write(line+"\n")
	newfile.close()
    else:
	oldfile = open(file,"w")
	for line in newline:
	    oldfile.write(line+"\n")
	oldfile.close()

filename = "B11.txt"
main(filename)

