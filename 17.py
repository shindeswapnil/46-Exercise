#Write a version of a palindrome recognizer that also accepts phrase palindromes such 
#as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", 
#"Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas",
# "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". 
#Note that punctuation, capitalization, and spacing are usually ignored.

import string
def palindrome_phrase(s):
	punctuations=string.punctuation #gives all punctuations
	for ch in s.lower(): 
		if ch in punctuations: 
			s=s.replace(ch, "") 
		elif ch==' ':
			s=s.replace(ch, "")
	s1=s[::-1]
	if s1.upper()==s.upper():
		return True
	else:
		return False

s="Go hang a salami I'm a lasagna hog."
print(palindrome_phrase(s))
print(palindrome_phrase("Was it a rat I saw?"))
print(palindrome_phrase("Step on no pets"))
print(palindrome_phrase("Sit on a potato pan, Otis"))
print(palindrome_phrase("Lisa Bonet ate no basil"))


