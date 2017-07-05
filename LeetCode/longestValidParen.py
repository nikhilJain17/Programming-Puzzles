'''Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

'''

import math

# checks if parenthesis are valid
def isValid(s):
  
    stack = []

    openingChar = ['(', '{', '[']
    closingChar = [')', '}', ']']


    for c in s:
        if c in openingChar:
            stack.append(c)

        elif c in closingChar:
            
            if len(stack) == 0:
                # more closing than opening brackets
                return False
            
            # use ascii table to figure out if brackets match
            # print str(ord(stack[-1])) + ', ' + str(ord(c))
            
            if len(stack) > 0:

                if math.fabs(ord(stack[-1]) - ord(c)) < 3:
                    # brackets match
                    stack.pop()
                else:
                    # top level brackets dont match
                    return False


    if len(stack) == 0:
        return True 
    else:
        # more opening than closing brackets
        return False


def checker(input):

	max_length = 0

	# iterate through input
	for start_index in range(0, len(input)):
		
		end_index = len(input)

		# do while
		while True:
			substr = input[start_index : end_index]

			# found valid substr, check if it is max len
			if isValid(substr):
				length = end_index - start_index
				print str(length) + ' <- len of ' + substr

				if max_length < length:
					max_length = length
				
				break

			# didn't find it, keep going
			else:
				end_index -= 1

	return max_length


# checker("(()"













