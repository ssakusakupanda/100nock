#coding:utf-8
#100nock 19

from collections import Counter

itemList = []
for line in open("./../hightemp.txt",'r'):
    itemList.append(line.split('\t')[0])

for word,cnt in Counter(itemList).most_common():
    print(word,cnt)
