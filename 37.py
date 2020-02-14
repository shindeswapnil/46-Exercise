
#Write a program that given a text file will create a new text file in which all the lines from 
#the original file are numbered from 1 to n (where n is the number of lines in the file).

def numbered_file(filename):
	fin = open(filename)
	fout = open('ex37_numbered.txt', 'w')
	for line, content in enumerate(fin):
		fout.write('%s %s' % ((line + 1), content))

numbered_file('ex37.txt')
