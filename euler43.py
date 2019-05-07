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

from numpy import load, meshgrid, array, empty, unique, vstack
from itertools import permutations
from datetime import datetime
from copy import copy
from math import factorial
from itertools import permutations
start_time = datetime.now()
import pdb

digits = [0,1,2,3,4,5,6,7,8,9]
numbers = empty(shape=(10,))


for number in permutations(digits):
	numbers = vstack([numbers, list(number)])

# newNumbers = []
# for number in numbers:
# 	print(number)
# 	print(number[1:3])
# 	if number[1:3]%2 == 0:
# 		print(newNumbers)

pdb.set_trace()



















