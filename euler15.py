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
from copy import copy
start_time = datetime.now()
import pdb

maxPosition = (3,3)
oldPositions = [(0,0)]
newPositions = []
moveMade = 1
finishedPaths = 0
while moveMade == 1:
	moveMade = 0
	for oldPosition in oldPositions:
		if oldPosition[0] < maxPosition[0]: 
			newPositions.append((oldPosition[0]+1,oldPosition[1]))
			moveMade = 1
		if oldPosition[1] < maxPosition[1]: 
			newPositions.append((oldPosition[0],oldPosition[1]+1))
			moveMade = 1
		if oldPosition == maxPosition:
			finishedPaths += 1
	oldPositions = newPositions
	newPositions = []
	print(len(oldPositions))
	print(finishedPaths)
pdb.set_trace()
# def possible_moves(n, currentLocation):
	#n is the dimension of the board


