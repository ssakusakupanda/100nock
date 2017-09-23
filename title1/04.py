#coding:utf-8
#100nock 04

dict = {}

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str = str.split(" ")

for i,word in enumerate(str):

	n = i+1
	if n in [1,5,6,7,8,9,15,16,19]:
		dict[word[:1]] = n
	else:
		dict[word[:2]] = n

print(dict)
