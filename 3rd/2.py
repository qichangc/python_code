#!/usr/bin/python
#coding:utf-8
import random
"""
掷两个骰子(每个骰子有六面，1～6个点)
计算两个骰子之和
1、如果和为7或者11，玩家赢，庄家输；
2、如果和为2、3或12，玩家输，庄家赢；
3、如果和为4、5、6、8、9或10，则这个值称为“点数” t，重新掷骰子
    a.如果和为“点数” t，则玩家赢，庄家输；
    b.如果和为7，则玩家输，庄家赢；
    c.否则，重新掷骰子 
"""


def dice1():

    point1 = random.randint(1,6)
    point2 = random.randint(1,6)

    sum = point1 + point2
    print "sum is",sum
    if sum == 7 or sum == 11:
	return "player wins!"
    elif sum in [2,3,12] :
	return "banker wins!"
    else:
  	return dice2()	
	
def dice2():
    point1 = random.randint(1,6)
    point2 = random.randint(1,6)

    sum = point1 + point2  
    print "sum is",sum  
    if sum in [4,5,6,8,9,10]:
    	return "player wins"
    elif sum == 7:
	return "banker wins"
    else:
	return dice2()

print dice1()

