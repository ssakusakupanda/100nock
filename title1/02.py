#coding:utf-8
#100nock 02

str1 = "パトカー"
str2 = "タクシー"
str3 = ""

for i in range(len(str1 + str2)):
	
	index = int(i/2)
	
	if	i % 2 == 0:
		str3 += str1[index]
	else:
		str3 += str2[index]

print(str3[::1])

#別解
#for i in range(len(str1)):
#	str3 += str1[i] + str2[i]
