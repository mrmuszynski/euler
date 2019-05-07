#! /usr/bin/env python3
# H+
#	Title   : euler15.py
#	Author  : Matt Muszynski
#	Date    : 4/22/17
#	Synopsis: 
#
#
#	$Date$
#	$Source$
#  @(#) $Revision$
#	$Locker$
#
#	Revisions:
#
# H-
# U+
#	Usage   :
#	Example	:
#	Output  :
# U-
# D+
#
# D-
###############################################################################

from numpy import load, arange
from itertools import permutations
from datetime import datetime
from copy import copy
from math import factorial
from itertools import permutations
from string import ascii_uppercase
start_time = datetime.now()
import pdb

file = open('words.txt','r')

for line in file:
	words = line.replace("\"","").split(',')

def decodeWord(word):
	return sum([ascii_uppercase.index(x)+1 for x in word])

n = arange(50)
triangles = n*(n+1)/2
decode = [decodeWord(word) for word in words]
triangleWords = [word for word in decode if word in triangles]
print(len(triangleWords))
pdb.set_trace()



















