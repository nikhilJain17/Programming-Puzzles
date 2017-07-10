'''Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

# found formulas to generate all four diagonals
# 
# top right = n^2 for all odd n
# top left = n^2 - n + 1 for all odd n
# bottom left = n^2 + 1 for all even n
# bottom right = n^2 - n + 1 for all even n

ans = 0

for x in range(1002):
	
	if x % 2 == 0:
		ans += x * x + 1 		# bottom left
		ans += x * x - x + 1 	# bottom right
	else:
		ans += x * x			# top right
		ans += x * x - x + 1 	# top left

# subract 3 since we count 1, the center, in all four diagonals
ans -= 3
print ans

