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

different_ways = 0

for p1 in range(0,201):
	for p2 in range(0,101):
		if p1 + 2*p2 > 200: break
		for p5 in range(0,41):
			if p1 + 2*p2 + 5*p5 > 200: break
			for p10 in range(0,21):
				if p1+2*p2+5*p5+10*p10 > 200: break
				for p20 in range(0,11):
					if p1+2*p2+5*p5+10*p10+20*p20 > 200: break
					for p50 in range(0,5):
						if p1+2*p2+5*p5+10*p10+20*p20+50*p50 > 200: break
						for p100 in range(0,3):
							if p1+2*p2+5*p5+10*p10+20*p20+50*p50+100*p100 == 200: 
								print(str(p100) + " "+ str(p50) + " " + str(p20) \
								+ " " + str(p10) + " " + str(p5) + " " + str(p2) + " " + str(p1))
								different_ways += 1

print(different_ways)	