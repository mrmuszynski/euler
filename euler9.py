#! /usr/bin/env python3
# H+
#	Title   : euler9.py
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
from datetime import datetime
start_time = datetime.now()

for a in range(1,1000):
	for b in range(1,1000-a):
		c = 1000 - a - b
		if a**2 + b**2 == c**2:
			print(a*b*c)








