#coding:utf-8
#100nock 05

str = "I am an NLPer"

#単語N-gram
bigram_w = {}

N = 2
word = str.split(" ")

for i in range(len(word)-1):
	key = word[i] + " " + word[i+1]

	if key not in bigram_w: 
		bigram_w[key] = 0

	bigram_w[key] += 1

print(bigram_w)

#文字N-gram
bigram_c = {}

for i in range(len(str)-1):
	key = str[i] + str[i+1]

	if key not in bigram_c: 
		bigram_c[key] = 0
	bigram_c[key] += 1

print(bigram_c)
