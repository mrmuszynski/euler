#! /usr/bin/env python3
# H+
#	Title   : euler23.py
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

def find_full_factorization(n):
	full_factorization = []
	for i in range(1,n+1):
		if (n/i)%1 == 0: full_factorization.append(i)
	return full_factorization

def abundant_number(n):
	if sum(find_full_factorization(n)[0:-1]) > n:
		return 1
	else: 
		return 0

abundant_numbers = []
#for i in range(1,25):
for i in range(0,28124):
	if i%100 == 0: print(i)
	if abundant_number(i):
		abundant_numbers.append(i)

non_abundant_sums = np.array(range(1,28124))
pdb.set_trace()

for abundant_number_1 in abundant_numbers:
	print(abundant_number_1)
	for abundant_number_2 in abundant_numbers:
		if abundant_number_1 + abundant_number_2 > 28124: break
		non_abundant_sums = np.extract(non_abundant_sums != abundant_number_1 + abundant_number_2, non_abundant_sums)
pdb.set_trace()










