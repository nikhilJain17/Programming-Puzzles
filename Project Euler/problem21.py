# -*- coding: utf-8 -*-
'''Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''

# Nikhil Jain
import math
from collections import defaultdict

# inputs int n, returns sum of proper divisors INCLUDING n
# because d(n) + n = d(m) + m if both m and n are amicable
def dprime(input):

	sum = 0
	# find all the factors and their pairs
	for x in range(1, int(math.sqrt(input)) + 1):
		if input % x == 0:
			sum = sum + x + (input / x) # both factors are included

	return sum

# given a list, this func returns the index of the repeated values in the list
def getIndexOfDups(values):

	seen = set()
	repeatedVals = [] # assumes max repetitions is 2
	indices = []

	for index, val in enumerate(values):
		if val not in seen:				# first time seeing it boi
			seen.add(val)
		else:							# already seen val, so it is a repeat
			indices.append(index)		# only gets duplicated index, not original index
			repeatedVals.append(val)

	# prepare array by making nonrepeated vals = 0

	print repeatedVals

	s = 0
	for x in range(len(values)):
		if values[x] in repeatedVals:
			# print x 
			s += x

	print 's: ' + str(s)

	# # get first indices
	# for i in repeatedVals:
	# 	indices.append(values.index(i))

	# print indices
	return indices

def main():


	values = []	# all vals
	repeated_vals = set()
	
	for x in range(0, 1001):
		
		d = dprime(x)
		values.append(dprime(x))

	s = 0
	for val in values:
		indices = [i for i, x in enumerate(values) if x == val]
		if len(indices) > 2:
			print indices
			for i in indices:
				s += i

	print s

	# 	# DOESN'T PROPERLY GET ALL THE REPEATED VALS
	# 	if d not in repeated_vals:
	# 		repeated_vals.add(d)

	# # now we have a set of all the repeated vals
	# s = 0
	# for x in range(0, 101):
	# 	if values[x] in repeated_vals:
	# 		print str(x) + ' is amicable at value ' + str(values[x])
	# 		s += x

	# print s

	# getIndexOfDups(values)

	# print "Sum of amicable numbers under 10,000 is: " + str(sum(getIndexOfDups(values)))

main()