#coding:utf-8
#100nock 12

file = open("hightemp.txt",'r')
string = file.readline()

col1 = open("col1.txt",'w')
col2 = open("col2.txt",'w')

while string:
	col1.write(string.split("\t")[0] + '\n')
	col2.write(string.split("\t")[1] + '\n')
	string = file.readline()
