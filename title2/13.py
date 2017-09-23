#coding:utf-8
#100nock 13

file = open("hightemp2.txt",'w')

col1 = open('col1.txt','r')
col2 = open('col2.txt','r')

string1 = col1.readlines()
string2 = col2.readlines()

for i in range(len(string1)):
	file.write(string1[i].replace("\n","") + '\t' + string2[i])

