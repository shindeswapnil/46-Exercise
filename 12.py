#Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example,
#histogram([4, 9, 7]) should print the following:

#****
#*********
#*******

def histogram(l):
	for n in l:
		for i in range(0,n):
			print('*',end='')
		print('')

histogram([4,9,7])


