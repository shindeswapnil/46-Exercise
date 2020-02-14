
'''
Write a program that will calculate the average word length of a text stored in a file 
(i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens).
'''
from re import findall
def avg_word_len(filename):
	f=open(filename)
	words=findall('\w+', f.read()) #read word(alphanumeric) one or more match
	return (sum([len(word) for word in words])//len(words))	

print(avg_word_len('ex38.txt'))



