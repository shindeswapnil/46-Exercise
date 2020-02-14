#Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

def find_longest_word(l):
	longest=0
	for word in l:
		if len(word)>longest:
			longest=len(word)
	return longest

l=['abcd','ab','x','pqrstu','xy']
print(find_longest_word(l))

