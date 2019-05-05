#! /usr/bin/env python3
# H+
#	Title   : euler69.py
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
from datetime import datetime
import matplotlib.pyplot as plt

def prime_seive(n, possible_primes=None):
	#returns all primes <= n
	possible_primes = np.arange(n) + 1
	i = 1
	x = -1
	while x < possible_primes[-1]:
		x = possible_primes[i]
		ind = \
			np.logical_or(possible_primes/x % 1 != 0,possible_primes == x)
		possible_primes = possible_primes[ind]
		i += 1
	#need to boot 1 from primes list
	return possible_primes[1:]

# t = []
# for i in range(1,11):
# 	start = datetime.now()
# 	dummy = prime_seive(i*100000)
# 	t.append((datetime.now() - start).total_seconds())
# 	print(str(i*100000) + ': ' + str(datetime.now() - start))

# plt.plot(t)
pdb.set_trace()

