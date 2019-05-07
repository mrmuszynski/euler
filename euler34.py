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

from numpy import load, meshgrid, array, empty, unique, arange
from itertools import permutations
from datetime import datetime
from copy import copy
from math import factorial
start_time = datetime.now()
import pdb

for number in arange(100000):
	factorials = [factorial(int(x)) for x in str(number)]
	if sum(factorials) == number:
		print(number)

pdb.set_trace()



















