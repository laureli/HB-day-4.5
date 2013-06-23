from sys import argv

script, from_file = argv  

words = open(from_file) #open file on command line
book = words.read() # returns a string
book = book.lower()
words.close()

counter = [0] *26

for char in book:
	if char.isalpha():
		counter[(ord(char) - 97)] += 1

for i in counter:
	print i




