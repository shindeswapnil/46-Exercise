'''
A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a language,
the works of an author, or in a single text. Define a function that given the file name of a text will return all its hapaxes.
Make sure your program ignores capitalization.
'''

def hapax(filename):
	f=open(filename)
	words=[]
	for line in f:
		words += line.lower().split()
	for word in words:
		if words.count(word)==1:
			print(word)	

hapax('ex36.txt')
