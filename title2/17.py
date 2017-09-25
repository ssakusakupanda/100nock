#coding:utf-8
#100nock 17

list = []
for line in open("./../hightemp.txt",'r'):
	list.append(line.split('\t')[0])
print(set(list))
