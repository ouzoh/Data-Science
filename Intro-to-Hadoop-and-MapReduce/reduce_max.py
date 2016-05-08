#!/bin/python

import sys
list = []

def reducer():

oldKey = None

for line in sys.stdin:
	data = line.strip().split("\t")

	if len(data) !=2:
		continue

	thisKey, thisSale = data

	if oldKey and oldKey != thisKey:
		# 1.print appended list (testing)
		#print list

		# 2.print max of appended list
		print max(list[:])

		# 3. delete list
		del list[:]

	oldKey = thisKey
	a=[thisKey,float(thisSale)]
	list.append(a)


#
if oldKey !=None:
	#the last group on the list
	a = [thisKey, float(thisSale)]
	list.append(a)
	print max(list[:])
	del list[:]
