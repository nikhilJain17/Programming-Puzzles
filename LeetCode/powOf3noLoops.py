""""Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

"""""
import math

# Nikhil Jain

# just use logs
# log func either returns above or below int value if true
# i.e. 3^5 = 243
# but math.log(243, 3) == 4.9999999999 or 5.0000000001
# so handle both
def isPowerOfThree(n):
	if n <= 0: return False
	return math.fabs(math.log(n, 3) - math.floor(math.log(n,3))) == 0 or math.fabs(math.log(n, 3) - math.floor(math.log(n,3)) - 1) < 0.0000000001 
	