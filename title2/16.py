#coding:utf-8
#100nock 16

import math

print("N=",end="")
N = int(input())

file = open("./../hightemp3.txt",'r')
lines = file.readlines()
l = len(lines)

block = math.ceil(l/N)

for i in range(N):
	wfile = open("./../hightemp_small"+str(i+1)+".txt",'w')
	for line in lines[block*i:block*(i+1):]:
		wfile.write(line)
