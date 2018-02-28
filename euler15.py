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


def partition(n,z,arr):
	for i in range(z+i,n-i,z+i):
		arr = arr + partition(n-i,z+i,arr)
	print(arr)
	return arr
a = partition(2,1,[])


# master = []
# arr = []
# for a in range(1,21,1):
# 	arr.append(a)
# 	print(arr)
# 	if sum(arr) > 20: break
# 	for b in range(2,21,2):
# 			arr = []
# 			arr.append(b)
# 			if sum(arr) > 20: break
# 			for c in range(3,21,3):
# 				arr = []
# 				arr.append(c)	
# 				if sum(arr) > 20: break
# 				for d in range(4,21,4):
# 						arr = []
# 						arr.append(d)	
# 						if sum(arr) > 20: break
# 						for e in range(5,21,5):
# 							arr = []
# 							arr.append(e)	
# 							if sum(arr) > 20: break
# 							for f in range(6,21,6):
# 								arr = []
# 								arr.append(f)	
# 								if sum(arr) > 20: break
# 								for g in range(7,21,7):
# 									arr = []
# 									arr.append(g)	
# 									if sum(arr) > 20: break
# 									for h in range(8,21,8):
# 										arr = []
# 										arr.append(h)	
# 										if sum(arr) > 20: break
# 										for i in range(9,21,9):
# 											arr = []
# 											arr.append(i)	
# 											if sum(arr) > 20: break
# 											for j in range(10,21,10):
# 												arr = []
# 												arr.append(j)	
# 												if sum(arr) > 20: break
# 												for k in range(11,21,11):
# 													arr = []
# 													arr.append(k)	
# 													if sum(arr) > 20: break
# 													for l in range(12,21,12):
# 														arr = []
# 														arr.append(l)	
# 														if sum(arr) > 20: break
# 														for m in range(13,21,13):
# 															arr = []
# 															arr.append(m)	
# 															if sum(arr) > 20: break
# 															for n in range(14,21,14):
# 																arr = []
# 																arr.append(n)	
# 																if sum(arr) > 20: break
# 																for o in range(15,21,15):
# 																	arr = []
# 																	arr.append(o)	
# 																	if sum(arr) > 20: break
# 																	for p in range(16,21,16):
# 																		arr = []
# 																		arr.append(p)	
# 																		if sum(arr) > 20: break
# 																		for q in range(17,21,17):
# 																			arr = []
# 																			arr.append(q)	
# 																			if sum(arr) > 20: break
# 																			for r in range(18,21,18):
# 																				arr = []
# 																				arr.append(r)	
# 																				if sum(arr) > 20: break
# 																				for s in range(19,21,19):
# 																					arr = []
# 																					arr.append(s)	
# 																					if sum(arr) > 20: break
# 																					for t in range(20,21,20):
# 																						arr = []
# 																						arr.append(t)
# 																						if sum(arr) == 20:
# 																							master.append(arr)
# 																						if sum(arr) >= 20: break
# 																						print(arr)





