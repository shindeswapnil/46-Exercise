'''
Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user,
builds a frequency listing of the characters contained in the file,
and prints a sorted and nicely formatted character frequency table to the screen.
'''

def char_freq_table(filename):
	f=open(filename)
	alpha=f.read().lower().replace(" ", "").replace("\n", "")
	s=''
	for ch in alpha:
		s+=ch
	
	s=''.join(sorted(s))
	
	freq={key:0 for key in s}
	
	for ch in alpha:
		freq[ch]+=1
	
	for ch in freq:
     	   print('{}:{}'.format(ch, freq[ch]))

filename=input('Enter File Name : ')
char_freq_table(filename)



