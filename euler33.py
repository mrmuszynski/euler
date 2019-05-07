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

from numpy import meshgrid, arange, logical_or, logical_and, array
import pdb


a, b = meshgrid(arange(1,11),arange(1,11))
a = a.reshape(100)
b = b.reshape(100)
c = a/b
c = c[c<1]

aa, bb = meshgrid(arange(1,101),arange(1,101))
aa = aa.reshape(10000)
bb = bb.reshape(10000)
cc = aa/bb

nonTrivialIndex = logical_or((aa/10)%1!=0,(bb/10)%1!=0)
aa = aa[nonTrivialIndex]
bb = bb[nonTrivialIndex]
cc = cc[nonTrivialIndex]

twoDigitIndex = logical_and(aa > 9, bb > 9)
aa = aa[twoDigitIndex]
bb = bb[twoDigitIndex]
cc = cc[twoDigitIndex]

ltOneIndex = cc < 1
aa = aa[ltOneIndex]
bb = bb[ltOneIndex]
cc = cc[ltOneIndex]

ccInCIndex = array([True if x in c else False for x in cc])
aa = aa[ccInCIndex]
bb = bb[ccInCIndex]
cc = cc[ccInCIndex]

aaa = []
bbb = []
for ii in range(len(aa)):
	if str(aa[ii]) in str(bb):
		aaa.append(float(str(aa[ii])[1]))
	else:
		aaa.append(float(str(aa[ii])[0]))
	if str(bb[ii]) in str(aa):
		bbb.append(float(str(bb[ii])[1]))
	else:
		bbb.append(float(str(bb[ii])[0]))
aaa = array(aaa)
bbb = array(bbb)
ccc = array(aaa)/array(bbb)

nonZeroIndex = logical_and(aaa > 0, bbb > 0)
aaa = aaa[nonZeroIndex]
bbb = bbb[nonZeroIndex]
ccc = ccc[nonZeroIndex]
aa = aa[nonZeroIndex]
bb = bb[nonZeroIndex]
cc = cc[nonZeroIndex]

quotientsEqualIndex = ccc != cc
aaa = aaa[quotientsEqualIndex]
bbb = bbb[quotientsEqualIndex]
ccc = ccc[quotientsEqualIndex]
aa = aa[quotientsEqualIndex]
bb = bb[quotientsEqualIndex]
cc = cc[quotientsEqualIndex]
# def commonDigit(aa,bb):
# 	[a for a in aa]
# for ii in range(10000):


pdb.set_trace()









