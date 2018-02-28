#! /usr/bin/env python3
# H+
#	Title   : euler28.py
#	Author  : Matt Muszynski
#	Date    : 10/23/17
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


total = 0
n = 0
x = 0
for i in range(0,2001):
	if i % 4 == 1: n += 2
	x += n
	print(x + 1)
	total += x + 1




pdb.set_trace()

