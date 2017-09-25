#coding:utf-8
#100nock 18

itemList = []
for line in open("./../hightemp.txt",'r'):
  itemList.append(line.split('\t'))
itemList_sorted = sorted(itemList,key=lambda x:x[2])
print(itemList_sorted)
