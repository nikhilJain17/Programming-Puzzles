'''Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

'''


def roman(num):

	result = ''

	while num > 0:
		if (num > 999):
			result += 'M'
			num -= 1000
		
		# 900 to 1000 
		elif (num <= 999 and num > 899):
			result += 'CM'
			num -= 900

		elif (num > 499 and num < 900):
			result += 'D'
			num -= 500
		
		elif (num > 99):
			result += 'C'
			num -= 100

		# 90 to 99
		elif (num <= 99 and num > 89):
			result += 'XC'
			num -= 90

		elif (num > 49):
			result += 'L'
			num -= 50

		elif (num > 9):
			result += 'X'
			num -= 10

		## num is 9 lol
		elif (num == 9):
			result += 'IX'
			num -= 9
		
		elif (num > 4):
			result += 'V'
			num -= 5

		else:
			result += 'I'
			num -= 1
		
	# now get rid of repeats (such as IIII, which becomes IV)
	if result.count('I') > 3:
		result = result.replace('IIII', 'IV')

	if result.count('X') > 3:
		result = result.replace('XXXX', 'XL')

	if result.count('C') > 3:
		result = result.replace('CCCC', 'CD')

	return result

for x in range (1, 100):
	print str(x) + ', ' + roman(x)
		
		
		