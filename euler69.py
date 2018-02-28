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


for n in range(2,11):
	possible_relative_primes = n/(np.arange(1,n)+1)

	n_relative_primes = \
	len(possible_relative_primes[possible_relative_primes%1!=0])+1
	print(n)
	print(possible_relative_primes[possible_relative_primes%1!=0])


pdb.set_trace()

