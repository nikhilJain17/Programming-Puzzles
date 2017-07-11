# # -*- coding: utf-8 -*-
'''The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

'''
import math

# def F(n):
#     return ((1+math.sqrt(5))**n-(1-math.sqrt(5))**n)/(2**n*math.sqrt(5))

# print F(4787)

firstFib = 1
secondFib = 1
currentFib = firstFib + secondFib
index = 3

while math.floor(math.log(currentFib, 10)) < 999:
	firstFib = secondFib
	secondFib = currentFib
	currentFib = firstFib + secondFib
	index += 1

print index