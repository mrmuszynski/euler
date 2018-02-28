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
from datetime import datetime
start_time = datetime.now()
import pdb

def find_full_factorization(n):
	full_factorization = []
	stop_here = int(np.ceil(np.sqrt(n))+1)
	print(int(stop_here))
	for i in range(1,stop_here):
		if (n/i)%1 == 0: 
			full_factorization.append(i)
			full_factorization.append(n/i)
	return full_factorization


triangle_number = 0
factorization_len = 0
n = 1
max_len = 0
while factorization_len <501:
	triangle_number += n
	n += 1
	factorization_len = len(find_full_factorization(triangle_number))
	if factorization_len>max_len:max_len=factorization_len
	print(str(triangle_number) + ", " + str(max_len))








