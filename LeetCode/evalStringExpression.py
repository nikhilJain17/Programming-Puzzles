'''Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.

'''

def calculate(s):
	# rip out numbers from input
	# by finding indices of operators

	s = s.replace(' ', '')		# get rid of whitespaces
	oper_index = 0			# index of operators
	oper_list = []				# actual operators
	num_list = []

	# snag operators and nums into list
	for x in range(len(s)):
		c = s[x]
		if c in ['+', '-', '*', '/']:
			num_list.append(s[oper_index:x])
			oper_index = x + 1
			oper_list.append(c)

		# snag last num, off by 1 error
		if x == len(s) - 1:
			num_list.append(s[oper_index:]) 

	# pemdas: do all mult and div first

	print oper_list
	print len(oper_list)
	print num_list
	print len(num_list)
	print '_' * 70

calculate('3    + 5 /13')
calculate('49+ 14-1-1-0+45/2       * 3')
calculate('')
