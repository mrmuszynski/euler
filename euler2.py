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

f1 = 1
f2 = 1
f3 = 0
sum = 0
while f3 < 4000000:
	if f3%2 == 0:
		sum = sum + f3
	f3 = f1 + f2
	f1 = f2
	f2 = f3

print(sum)












