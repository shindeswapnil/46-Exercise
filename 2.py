#Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
def max_of_three(a,b,c):
	if a > b :
		if a > c :
			return a
		else :
			return c
	elif b > a :
		if b > c :
			return b
		else:
			return c
	elif a==b==c :
		print('All are same !')

a=int(input('Enter 1st Number :'))
b=int(input('Enter 2nd Number :'))
c=int(input('Enter 3rd Number :'))

print(max_of_three(a,b,c))
