'''If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''
import math

digitstr = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

written = ''
length = 0
for num in range(1, 1001):

	digits = []

	# flip digits
	for c in str(num)[::-1]:
		digits.append(int(c))
		
	for x in range(len(digits)):
			
		# ones digit
		if x == 0:
			written += digitstr[digits[x]]
		
		# tens digit
		elif x == 1: 
			# teens (overwrites ones digits)
			if digits[x] == 1:
				written = teens[digits[0]]
			elif digits[x] != 0:
				written += tens[digits[1] - 2]

		# hundred
		elif x == 2:
			if digits[2] != 0:
				written += digitstr[digits[2]] + 'hundred'
			if not (digits[0] == 0 and digits[1] == 0):
				written += 'and'

		# thousand
		elif x == 3:
			written += 'onethousand'

	print str(num) + ', ' + written + ', ' + str(len(written))
	length += len(written)
	written = ''

print length

	