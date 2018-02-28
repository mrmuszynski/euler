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

def find_prime_factors(n):
	possible_primes = np.array(range(2,n+1))
	i = possible_primes[0]
	j = 0
	
	while j < len(possible_primes):
		condition = np.logical_or(possible_primes%i != 0, possible_primes==i)
		possible_primes = \
		np.extract(condition, possible_primes)
		i = possible_primes[j]
		j = j+1
	primes_le_n = possible_primes

	prime_factors = []
	for prime in primes_le_n:
		if (n/prime)%1 == 0:
			prime_factors.append(prime)

	return prime_factors


factors1 = []
factors2 = []
factors3 = []
factors4 = []

n = 10
while True:
	factors4 = factors3
	factors3 = factors2
	factors2 = factors1
	factors1 = find_prime_factors(n)
	all_factors = factors4 + factors3 + factors2 + factors1
	print(set(all_factors))
	if len(set(all_factors)) == 9 and len(all_factors) == 9:
		break
	print(n)
	n += 1








