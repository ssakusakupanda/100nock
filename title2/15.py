#coding:utf-8
#100nock 15

file = open("./../hightemp.txt",'r')
string = file.readlines()

print("N=",end="")
N = input()

lines = string[len(string)-int(N):len(string):]

for line in lines:
	print(line,end="")
