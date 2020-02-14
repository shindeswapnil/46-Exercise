#Write a version of a palindrome recogniser that accepts a file name from the user, 
#reads each line, and prints the line to the screen if it is a palindrome.

def check_palindrome(filename):
	f=open(filename)
	for line in f.read().split('\n'):
		if line==line[::-1]:
			print(line)

filename=input('Enter File Name : ')
check_palindrome(filename)
