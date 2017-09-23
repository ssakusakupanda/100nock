#coding:utf-8
#100nock 09

import random

def Typoglycemia(str):

	str = str.split(" ")
	n_str = ""

	for word in str:
		if len(word) > 4:
			n_str += word[0]
		
			num = random.sample(range(1,len(word)-1),len(word)-2)
			for i in num:
				n_str += word[i]
			
			n_str += word[len(word)-1] + " "
		
		else:
			n_str += word + " "
	
	return n_str

#main()
str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(Typoglycemia(str))
