# -*- coding: utf-8 -*-
'''An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1,000 × d10,000 × d100,000 × d1,000,000
'''

string = ''
count = 1

while len(string) <= 1000000:
	string += str(count)
	count += 1

print int(string[0:1]) * int(string[9:10]) * int(string[99:100]) * int(string[999:1000]) * int(string[9999:10000]) * int(string[99999:100000]) * int(string[999999:1000000]) 