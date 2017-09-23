#coding:utf-8
#100nock 11

file = open('hightemp.txt','r')
print(file.read().replace("\t",' '),end="")
