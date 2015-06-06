#!/usr/bin/python
# coding:utf-8


def brefile(filname1, filename2):

    myfile = open(filname1, 'r')
    writefile = open(filename2, 'w')
    filelist = []
    while True:
        myline = myfile.readline()
        if not myline:
            break
        else:
            filelist.append(myline.strip("\n"))
    for item in filelist:
        if item.find("***编号****") == 0:
            print "\n"
            writefile.write('\n\n')
            print item
            writefile.write(item + '\n')
        else:
            breline(item, writefile)
    myfile.close()
    writefile.close()


def breline(line, wfile):

    str1 = "公司行业"
    str2 = "公司性质"
    str3 = "公司规模"

    fi1 = line.find(str1)
    fi2 = line.find(str2)
    fi3 = line.find(str3)
    # print line+"========="

    if fi1 >= 0:
        print
        wfile.write('\n')
        print line[:fi2]
        wfile.write(line[:fi2] + '\n')
        print line[fi2:fi3]
        wfile.write(line[fi2:fi3] + '\n')
        print line[fi3:]
        wfile.write(line[fi3:] + '\n')
        print "公司简介: ",
        wfile.write("公司简介: ")
    else:
        print line,
        wfile.write(line)


filename = "test.txt"
filename2 = "res"
brefile(filename, filename2)
