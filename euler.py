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


numbers_that_work = []

for i in range(2,1000000):
	sum_of_fifth_powers = 0
	for digit in str(i):
		sum_of_fifth_powers += int(digit)**5
	if sum_of_fifth_powers == i:
		numbers_that_work.append(i)

print(numbers_that_work)
print(sum(numbers_that_work))

