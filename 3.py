#Define a function that computes the length of a given list or string.
# (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
def my_len(s):
	l=0
	for ch in s:
		l=l+1
	return l

s=input('Enter String : ')
print(my_len(s))
list1=[10,20,30,40,50]
print(my_len(list1))
