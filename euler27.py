#! /usr/bin/env python3
# H+
#	Title   : euler23.py
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

from numpy import arange, set_printoptions, load, meshgrid, array
from numpy import unique, logical_or, zeros
import pdb
set_printoptions(precision=64)

primes = load('primes.npy')
a = arange(-1000,1001)
b = arange(-1000,1001)

aa, bb = meshgrid(a,b)
aa = aa.reshape(2001*2001)
bb = bb.reshape(2001*2001)
aaa = aa
bba = bb
cc = aa*bb
dd = arange(2001*2001)

def poly(n,a,b):
	return n**2 + aa*n + bb

def filterNonPrimes(polyResult):
	uniquePolyResults = unique(polyResult)
	uniquePolyPrimes = [x for x in uniquePolyResults if x in primes]
	logical_result = zeros(len(polyResult))
	for x in uniquePolyPrimes:
		logical_result = logical_or(logical_result, polyResult == x)
	return logical_result

n = 0
polyResult = []
while len(polyResult) != 1:
	polyResult = poly(n,aa,bb)
	print(len(polyResult))
	index = filterNonPrimes(polyResult)
	print(len(polyResult))
	print (index)
	aa = aa[index]
	bb = bb[index]
	dd = dd[index]
	polyResult = polyResult[index]
	print(dd[-1])
	print(len(dd))
	n +=1

print(aaa[dd[0]]*bba[dd[0]])
pdb.set_trace()












