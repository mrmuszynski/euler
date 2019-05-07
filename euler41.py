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

from numpy import load, array, vstack, logical_and, empty, unique, arange
from itertools import permutations
from datetime import datetime
from copy import copy
start_time = datetime.now()
import pdb

primes = load('primesUnder1000000.npy')

def isPandigital(number):
	pandigitalCheckNumber = ''.join((arange(len(str(number)))+1).astype(str))
	sortedNumber = ''.join(sorted([x for x in str(number)]))
	return sortedNumber == pandigitalCheckNumber

for prime in primes:
	if isPandigital(prime):
		print(prime)	
pdb.set_trace()



















