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

import numpy as np
import pdb

fibbonacci = [1,1]


n = 2
longest_fib = 1

while longest_fib < 1000:
	fn = fibbonacci[n-2]+fibbonacci[n-1]
	fibbonacci.append(fn)
	n += 1
	longest_fib = len(str(fn))
	print(longest_fib)

print(len(fibbonacci))




