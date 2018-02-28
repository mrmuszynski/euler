#! /usr/bin/env python3
# H+
#	Title   : euler1.py
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


sum = 0
for i in range(1,1000):
	if i%3 == 0:
		print(i)
		sum = sum + i
	elif i%5 == 0:
		print(i)
		sum = sum + i

print(sum)














