#!/usr/bin/env python3
import re

#characters that do not count as a word
notchars = "abcdefghijklmnopqrstuvwxyz"
#number of chinese characters counted
numchinese = 0

for line in open("input.txt", "r").readlines():
    for char in line:
        if re.search(u'[\u4e00-\u9fff]', char):
            numchinese += 1
            print(char,end='')
print("\nChinese character count: " + str(numchinese))
