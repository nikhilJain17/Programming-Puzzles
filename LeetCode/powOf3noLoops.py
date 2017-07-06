""""Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

"""""

# Nikhil Jain

# powers of three have the following sequence for last digit:
# 3, 9, 7, 1
# this program uses that fact to figure out the answer
# could be shorter but is more thorough in this form

def isPowerOfThree(n):

	digitsList = [3, 9, 7, 1]
	lastDigit = n % 10
	
	if n <= 0:
		return False
		

	if lastDigit not in digitsList:
		return False
	
	nDigsList = []
	nDigsList.append((n * 3) % 10)
	nDigsList.append((n * 9) % 10)
	nDigsList.append((n * 27) % 10)
	nDigsList.append((n * 81) % 10)

	print nDigsList

	# rotate nDigsList for thoroughness
	# so if n is pow of 3, nDigsList and digitsList are identical
	# although i don't think this is necessary
	# order doesn't really matter but just to be thorough
	
	if nDigsList.count(3) is 0:
		# safety check for rotating about 3
		# because if 3 isn't in nDigsList, func index throws err
		return false

	start = nDigsList.index(3)
	nDigsList = nDigsList[start:] + nDigsList[:start]

	print nDigsList

	if nDigsList == digitsList:
		return True
	else:
		return False