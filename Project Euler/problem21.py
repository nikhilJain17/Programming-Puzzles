# -*- coding: utf-8 -*-
'''Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''

# Nikhil Jain
import math
from collections import defaultdict

# inputs int n, returns sum of proper divisors less than n
def d(input):

	sum = 0
	# find all the factors and their pairs
	for x in range(1, int(math.sqrt(input)) + 1):
		if input % x == 0:
			sum = sum + x + (input / x) # both factors are included

	return sum - input

# while iterating from 1 to 10,000
# find higher pair of amicable pair (i.e. a = 280, d(a) = 220)
# check arr[d(a)] == a to confirm lower pair matches
# print ans
def main():

	values = []			# all vals
	amicable_sum = 0	# sum of all amicable nums under 10,000
	
	for x in range(0, 10001):
		
		values.append(d(x))

		val = d(x)
		if val < x:
			print 'true'
			if values[val] == x:
				amicable_sum += (x + d(x))

	print amicable_sum

main()