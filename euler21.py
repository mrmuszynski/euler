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

def find_prime_factorization(n):
	prime_factors = find_prime_factors(n)
	prime_factorization = []
	for prime_factor in prime_factors:
		x = 1

		while 1==1:
			if (n/prime_factor**x)%1 != 0: break
			prime_factorization.append(prime_factor)
			x += 1
	return prime_factorization

def find_full_factorization(n):
	full_factorization = []
	for i in range(1,n+1):
		if (n/i)%1 == 0: full_factorization.append(i)

	return full_factorization

pdb.set_trace()

total = 0

for i in range(2,10001):
	i_factorization_sum = sum(find_full_factorization(i)[0:-1])
	if i_factorization_sum < 10000:
		complimentary_sum = sum(find_full_factorization(i_factorization_sum)[0:-1])
		if complimentary_sum == i:
			print(str(complimentary_sum) + ", " + str(i_factorization_sum))
			
			if complimentary_sum != i_factorization_sum:
				total += i

print(total)
pdb.set_trace()










