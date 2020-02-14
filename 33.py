'''
According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards.
("Semordnilap" is itself "palindromes" spelled backwards.) Write a semordnilap recogniser that accepts a file name 
(pointing to a list of words) from the user and finds and prints all pairs of words that are semordnilaps to the screen. 
For example, if "stressed" and "desserts" is part of the word list, the the output should include the pair "stressed desserts".
 Note, by the way, that each pair by itself forms a palindrome!
'''
def semordnilap(filename):
	f=open(filename)
	words=f.read().split()
	res=[]
	for word1 in words:
		for word2 in words:
			if word1==word2[::-1] and words.index(word1)!=words.index(word2) and word2+' '+word1 not in res:
				res.append(word1+' '+word2)
	return res

filename=input('Enter File Name : ')
print(semordnilap(filename))
