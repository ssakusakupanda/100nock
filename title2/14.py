#coding:utf-8
#100nock 14

file = open("./../hightemp.txt",'r')
string = file.readlines()

print("N=",end="")
N = input()

lines = string[:int(N):]
for line in lines:
	print(line,end="")
