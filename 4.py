#Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
def is_vowel(ch):
	v=['a','e','i','o','u','A','E','I','O','I','U']
	if ch in v :
		return True
	else :
		return False

ch=input('Enter Character : ')
print(is_vowel(ch))
	
	
