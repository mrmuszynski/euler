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

stringPrimes = primes.astype(str)

for stringPrime in stringPrimes:
	leftTrucations = [stringPrime[ii:] for ii in range(1,len(stringPrime))]
	rightTrucations = [stringPrime[:-ii] for ii in range(1,len(stringPrime))]
	allTruncations = leftTrucations + rightTrucations
	allTruncationsPrime = sum([int(x) in primes for x in allTruncations]) == len([int(x) in primes for x in allTruncations])
	if allTruncationsPrime: print(stringPrime)


pdb.set_trace()



















