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

from numpy import load, arange, meshgrid
from prime_seive import prime_seive
from scipy.misc import factorial
import pdb

def combinations(n,r):
	return factorial(n)/factorial(r)/factorial(n-r)

n, r = meshgrid(arange(100)+1,arange(100)+1)
n = n.reshape(10000)
r = r.reshape(10000)
index = n >= r
n = n[index]
r = r[index]
comb = combinations(n,r)
pdb.set_trace()



















