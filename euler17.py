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

string = ''
f = 0
for i in range(1,1001):
	number = str(i)
	if len(number) == 4:
		ones = int(number[-1])
		tens = int(number[-2])
		hundreds = int(number[-3])
		thousands = int(number[-4])

	elif len(number) == 3:
		ones = int(number[-1])
		tens = int(number[-2])
		hundreds = int(number[-3])
		thousands = np.nan

	elif len(number) == 2:
		ones = int(number[-1])
		tens = int(number[-2])
		hundreds = np.nan
		thousands = np.nan

	elif len(number) == 1:
		ones = int(number[-1])
		tens = np.nan
		hundreds = np.nan
		thousands = np.nan

	if thousands == 1: string += 'onethousand'
	if hundreds == 1: string += 'onehundred'
	if hundreds == 2: string += 'twohundred'
	if hundreds == 3: string += 'threehundred'
	if hundreds == 4: string += 'fourhundred'
	if hundreds == 5: string += 'fivehundred'
	if hundreds == 6: string += 'sixhundred'
	if hundreds == 7: string += 'sevenhundred'
	if hundreds == 8: string += 'eighthundred'
	if hundreds == 9: string += 'ninehundred'
	if np.isnan(hundreds):
		if tens == 2: string += 'twenty'
		if tens == 3: string += 'thirty'
		if tens == 4: string += 'forty'
		if tens == 5: string += 'fifty'
		if tens == 6: string += 'sixty'
		if tens == 7: string += 'seventy'
		if tens == 8: string += 'eighty'
		if tens == 9: string += 'ninety'
	else:
		if tens == 2: string += 'andtwenty'
		if tens == 3: string += 'andthirty'
		if tens == 4: string += 'andforty'
		if tens == 5: string += 'andfifty'
		if tens == 6: string += 'andsixty'
		if tens == 7: string += 'andseventy'
		if tens == 8: string += 'andeighty'
		if tens == 9: string += 'andninety'
		if tens == 0 and ones != 0: string += 'and'


	if tens == 1: 
		if np.isnan(hundreds):
			if ones == 1: string += 'eleven'
			if ones == 2: string += 'twelve'
			if ones == 3: string += 'thirteen'
			if ones == 4: string += 'fourteen'
			if ones == 5: string += 'fifteen'
			if ones == 6: string += 'sixteen'
			if ones == 7: string += 'seventeen'
			if ones == 8: string += 'eighteen'
			if ones == 9: string += 'nineteen'
			if ones == 0: string += 'ten'
		else:
			if ones == 1: string += 'andeleven'
			if ones == 2: string += 'andtwelve'
			if ones == 3: string += 'andthirteen'
			if ones == 4: string += 'andfourteen'
			if ones == 5: string += 'andfifteen'
			if ones == 6: string += 'andsixteen'
			if ones == 7: string += 'andseventeen'
			if ones == 8: string += 'andeighteen'
			if ones == 9: string += 'andnineteen'
			if ones == 0: string += 'andten'
	else:
		if ones == 1: string += 'one'
		if ones == 2: string += 'two'
		if ones == 3: string += 'three'
		if ones == 4: string += 'four'
		if ones == 5: string += 'five'
		if ones == 6: string += 'six'
		if ones == 7: string += 'seven'
		if ones == 8: string += 'eight'
		if ones == 9: string += 'nine'

	# string += "\n"
	f += 1
print(string)
pdb.set_trace()







