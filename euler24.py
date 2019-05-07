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

from numpy import load, array, vstack, linspace, zeros
from math import factorial
from itertools import permutations
from datetime import datetime
from copy import copy
start_time = datetime.now()
import pdb

factorials = array([factorial(x) for x in linspace(9,0,10)])
print factorials
coeffs = zeros(10)
for jj in range(len(coeffs)):
	ii = 0
	while sum(coeffs*factorials) + ii*factorials[jj] < 1000000:
		ii += 1
	coeffs[jj] = ii-1
	print(coeffs[jj])
pdb.set_trace()



















