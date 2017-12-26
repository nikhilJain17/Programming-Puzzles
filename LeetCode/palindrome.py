import math

def isPalindrome(num):
    print("num ", num)
    if num < 0:
        num = num * -1
    print("num now ", num)
    first = num % 10
    last = num // 10 ** int(math.log(num) / math.log(10))
    if num < 100:
        if num < 10: 
            return True
        elif num // 10 == num % 10:
        	return True
        return False
    if first != last:
        return False
    if first == last:
        num = num // 10
        num = num % 10 ** int(math.log(num) / math.log(10))
        return True and isPalindrome(num)
