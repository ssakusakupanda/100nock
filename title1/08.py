#coding:utf-8
#100nock 08

def cipher(str):
	new_str = ""
	for c in str:
		if c.islower():
			c = chr(219-ord(c))
		new_str += c
	return new_str

str = input()
print(cipher(str))
