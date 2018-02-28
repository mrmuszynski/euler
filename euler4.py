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

def is_palendrome(a):
	if a - int(str(a)[::-1]) == 0:
		return 1
	else:
		return 0

largest = 0

for i in range(900,1000):
	for j in range(900,1000):
			if is_palendrome(i*j):
				if i*j > largest:
					largest = i*j

print(largest)