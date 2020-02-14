#Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
def filter_long_words(n,l):
	fl=[]
	for word in l:
		if len(word)>n:
			fl.append(word)
	return fl

l=['abcd','ab','x','pqrstu','xy']
print(filter_long_words(1,l))

