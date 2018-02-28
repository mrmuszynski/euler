#! /usr/bin/env python3
# H+
#	Title   : euler15.py
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

def collatz_chain(n):
	chain = [int(n)]
	while n != 1:
		if n%2 == 0:
			n = n/2
		else:
			n = 3*n + 1
		chain.append(int(n))
	return chain

max_chain_length = 0
print(1)
for i in range(1,1000001):
	chain_length = len(collatz_chain(i))
	if chain_length > max_chain_length:
		max_chain_length = chain_length
		print(str(i) + ": " + str(max_chain_length))
pdb.set_trace()











