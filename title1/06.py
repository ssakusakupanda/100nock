#coding:utf-8
#100nock 06

#頻度
def frec(key,dict):
	if key not in dict:
		dict[key] = 0
	dict[key] += 1

#文字N-gram
def ngram(str):
	dict = {}
	for i in range(len(str)-1):
		key = str[i]+str[i+1]
		frec(key,dict)
	return dict

#和集合
def union(X,Y):
	dict = X.copy() 	#'='だけだと間接参照
	for k in Y.keys():
		if k not in X:
			dict[k] = Y[k]
		else:
			dict[k] += Y[k]
	return dict 

#積集合
def intersection(X,Y):
	dict = {}
	for k in Y.keys():
		if k in X:
			dict[k] = X[k] + Y[k]
	return dict 

#差集合
def defference(X,Y):
	dict = {}
	for k in X.keys():
		if k not in Y:
			dict[k] = X[k]
	return dict 

#検索
def search(X,Y,key):
	dict = intersection(X,Y)	
	if key in dict:
		print('%sはあります' % key)
	else:
		print('%sはありません' % key)

#main
#.items()で頻度		
str1 = "paraparaparadise"
str2 = "paragraph"

X = ngram(str1)
Y = ngram(str2)

print("X")
print(sorted(X))
print("Y")
print(sorted(Y))

print("X OR Y")
OR = union(X,Y)
print(sorted(OR))

print("X AND Y")
AND = intersection(X,Y)
print(sorted(AND))

print("X DFF Y")
DFF = defference(X,Y)
print(sorted(DFF))

print("SERACH")
search(X,Y,"se")
