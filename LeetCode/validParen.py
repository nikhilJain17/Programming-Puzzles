"""Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

"""

# Nikhil Jain

# iterate through string
# push each opening char onto the stack
# if a closing char is found in string AND matches top of stack, pop
# if stack is empty, return true
import math
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

isValid('()()()')
        