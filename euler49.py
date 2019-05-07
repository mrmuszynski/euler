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

from numpy import load, array, hstack, logical_and, unique, meshgrid
from datetime import datetime
from copy import copy
start_time = datetime.now()
import pdb

def gapPrevalence(asdf):
	zx, cv = meshgrid(asdf,asdf)
	zxcv = zx-cv
	zxcv = zxcv[zxcv>0]
	return max([sum(zxcv == x) for x in zxcv]) >= 2


primes = load('primes.npy')

fourDigitPrimes = array([int(x) for x in primes.astype(str) if len(x) == 4])
sortedDigitPrimes = array([''.join(sorted(str(x))) for x in fourDigitPrimes])
numPermutationsPresent = array([sum(sortedDigitPrimes == x) for x in sortedDigitPrimes])

fourDigitPrimes = fourDigitPrimes[numPermutationsPresent > 2]
sortedDigitPrimes = sortedDigitPrimes[numPermutationsPresent > 2]
uniqueSortedDigitPrimes = unique(sortedDigitPrimes)

for uniqueSortedDigitPrime in uniqueSortedDigitPrimes: 
	if gapPrevalence(fourDigitPrimes[sortedDigitPrimes == uniqueSortedDigitPrime]):
		print('-'*80)
		print(fourDigitPrimes[sortedDigitPrimes == uniqueSortedDigitPrime])
		asdf = fourDigitPrimes[sortedDigitPrimes == uniqueSortedDigitPrime]
		pdb.set_trace()

pdb.set_trace()



















