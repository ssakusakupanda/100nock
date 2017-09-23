#coding:utf-8
#100nock 03

import re

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str = str.replace(".","").replace(",","")

print(sorted(str.split(" "),key=len))
