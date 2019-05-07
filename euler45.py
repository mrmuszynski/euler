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
start_time = datetime.now()
import pdb

n = arange(100000)
triangles   = n*(n+1)/2
pentagonals = n*(3*n-1)/2
hexagonals  = n*(2*n+1)/2

triPents = []
for triangle in triangles:
	if triangle in pentagonals: triPents.append(triangle)

triPentHexes = []
for triPent in triPents:
	if triPent in hexagonals: triPentHexes.append(triPent)
pdb.set_trace()



















