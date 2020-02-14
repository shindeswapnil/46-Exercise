#Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True.

def is_palindrome(s):
	s1=s[::-1]
	if s==s1 :
		return True
	else :
		return False

s=input('Enter String : ')
print(is_palindrome(s))
