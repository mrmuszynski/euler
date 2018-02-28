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

upper_limit = 1000000
possible_primes = np.array(range(2,upper_limit))
i = possible_primes[0]

j = 0
while j < len(possible_primes):
	condition = np.logical_or(possible_primes<=i, possible_primes%i != 0)
	possible_primes = \
	np.extract(condition, possible_primes)
	i = possible_primes[j]
	j = j+1

print(len(possible_primes))
print(possible_primes)
print(datetime.now() - start_time)
print(sum(possible_primes))