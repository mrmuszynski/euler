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
import pdb

find_prime_factor = 600851475143


for i in range(1,10000):
	if (find_prime_factor/i)%1 ==0:
		find_prime_factor = find_prime_factor/i
		if find_prime_factor == 1:
			print(i)




