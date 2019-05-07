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
start_time = datetime.now()
import pdb

primesLT1000000 = load('primesUnder1000000.npy')

primesLT100 = primesLT1000000[primesLT1000000<100]
stringPrimes = [str(x) for x in primesLT1000000]
circles = [[x[len(x)-ii:] + x[:-ii+len(x)] for ii in range(len(x))] for x in stringPrimes]

circularPrimes = 0
for circle in circles:
	truth = [True  if x in stringPrimes else False for x in circle]
	if len(truth) == sum(truth): 
		circularPrimes += 1
		print(circle[0])


pdb.set_trace()



















