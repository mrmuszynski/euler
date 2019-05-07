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
oddsLT1000000 = arange(1,1000001,2)
compositesLT1000000 = array([x for x in oddsLT1000000 if x not in primesLT1000000])
doubledSauares = arange(1,101)**2*2
asdf, zxcv = meshgrid(primesLT1000000,doubledSauares)
goldbachNumbers = unique(asdf + zxcv)
for composite in compositesLT1000000:
	if composite not in goldbachNumbers:
		print('#'*80)
		print(composite)
		print('#'*80)
	if str(composite)[-4:] == '9999': print(composite)

pdb.set_trace()



















