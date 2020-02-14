#A pangram is a sentence that contains all the letters of the English alphabet at least once, 
#for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a 
#sentence to see if it is a pangram or not.

import string 
alpha=string.ascii_lowercase
def pangram(s):
	s=s.lower()
	l=[c for c in s]
	for ch in alpha:
		if ch not in l:
			print('Not a Pangram !')
			return
	print('It is Pangram !')

pangram('The quick brown fox jumps over the lazy dog')
