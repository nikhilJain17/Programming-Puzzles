'''Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

'''

def fullJustify(words, maxWidth):

	# first, distribute words amongst lines

	current_line = ''
	arr_line = []

	for i in range(len(words)):

		word = words[i]

		if len(word) + len(current_line) > maxWidth:
			arr_line.append(current_line)
			current_line = ''

		current_line += word + ' '

		# off by one error, catch the last word and put in arr
		if i == len(words) - 1:
			arr_line.append(current_line)


	finalans = []

	# print arr_line

	# next, distribute spaces evenly

	for line in arr_line:
		# split line into array of words
		line_words = line.split()

		# go round robin between words spreading spaces out

		# remove whitespaces for counting purposes
		line = line.replace(' ', '')
		idx = 0		# which word gets whitespace

		while len(line) <= maxWidth:
			line_words[idx] += ' '
			line += ' ' # this keeps line_words and line having same length for counting purposes

			# handles last word
			if len(line_words) == 1:
				idx = 0
			else:
				idx = (idx + 1) % (len(line_words) - 1)

		# print line_words

		l = ''
		for lw in line_words:
			l += lw

		finalans.append(l)

	return finalans

print fullJustify(["This", "is", "an", "example", "of", "text", "pes."], 100)






