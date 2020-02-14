#Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers.
# For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24i

def my_sum(l):
	s=0
	for n in l:
		s=s+n
	return s

def my_multiply(l):
	m=1
	for n in l:
		m=m*n
	return m

l=[1,2,3,4]
print('sum = ',my_sum(l))
print('multiplication = ',my_multiply(l))

