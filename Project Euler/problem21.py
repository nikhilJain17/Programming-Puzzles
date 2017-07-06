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
	indices = []

	for index, val in enumerate(values):
		if val not in seen:				# first time seeing it boi
			seen.add(val)
		else:							# already seen val, so it is a repeat
			indices.append(index)

	return indices

def main():

	values = []	
	for x in range(0, 10001):
		values.append(dprime(x))

	print "Sum of amicable numbers under 10,000 is: " + str(sum(getIndexOfDups(values)))

main()