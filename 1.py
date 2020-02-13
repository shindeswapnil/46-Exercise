#Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct available in Python. 
#(It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)
def my_max(a,b):
	if a>b	:
		return a
	elif b>a :
		return b
	elif a==b :
		print('Both are Same !')

a=int(input('Enter the First Number : '))
b=int(input('Enter the Second Number : '))
print(my_max(a,b))
