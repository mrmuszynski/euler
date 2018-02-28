#! /usr/bin/env python3
# H+
#	Title   : euler2.py
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

sum_of_squares = 0

for i in range(1,101):
	sum_of_squares = sum_of_squares + i**2

square_of_sums = 0

for i in range(1,101):
	square_of_sums = square_of_sums + i

square_of_sums = square_of_sums**2

print(square_of_sums - sum_of_squares)