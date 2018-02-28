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

leap_years = [
1904,1908,1912,1916,1920,1924,1928,1932,
1936,1940,1944,1948,1952,1956,1960,1964,1968,
1972,1976,1980,1984,1988,1992,1996,2000
]

dow = 2
sunday_the_firsts = 0
for year in range(1901,2001):
	if year in leap_years:
		days = range(1,367)
		first_of_month = [1,32,61,92,122,153,183,214,245,275,306,336]
	else:
		days = range(1,366)
		first_of_month = [1,32,60,91,121,152,182,213,244,274,305,335]
	for doy in days:
		if dow%7 == 0 and doy in first_of_month:
			print(str(year)+'/'+str(doy) + " ")
			sunday_the_firsts += 1
		dow +=1
print("Sundays on First of Month: " + str(sunday_the_firsts))
pdb.set_trace()







