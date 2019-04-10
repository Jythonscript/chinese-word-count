#!/usr/bin/env python3
import re

#number of chinese characters counted
numchinese = 0
#string full of matches
matches = ""
#string full of characters that did not match
nonmatches = ""

for line in open("input.txt", "r").readlines():
    for char in line:
        if re.search(u'[\u4e00-\u9fff]', char):#if chinese
            matches += char
            numchinese += 1
        else:#if not chinese
            if char == '\n':
                nonmatches += "\\n"
            elif char == '\t':
                nonmatches += "\\t"
            else:
                nonmatches += char

print("Matches: '" + matches + "'")
print("Nonmatches: '" + nonmatches + "'")
print("Chinese character count: " + str(numchinese))
