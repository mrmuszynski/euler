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

i = 1
d = ""
while len(d) < 1000000:
	d += str(i)
	i += 1
print(int(d[1-1])*int(d[10-1])*int(d[100-1])*int(d[1000-1])*int(d[10000-1])*int(d[100000-1])*int(d[1000000-1]))
pdb.set_trace()



















