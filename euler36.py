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

from numpy import arange
from datetime import datetime
from copy import copy
start_time = datetime.now()
import pdb

dec = arange(1,1000000)

decPalindromes = [x for x in dec if str(x) == str(x)[::-1]]
binPalindromes = [x for x in decPalindromes if "{0:b}".format(x) == "{0:b}".format(x)[::-1]]

print(sum(binPalindromes))
pdb.set_trace()


















