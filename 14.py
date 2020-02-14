#Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.

def map_the_length(w):
	l=[]
	for word in w:
		l.append(len(word))
	return l

w=['abc','pq','opqr','x','abcdefg']
print(map_the_length(w))

