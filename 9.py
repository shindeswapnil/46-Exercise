#Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise.
 #(Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.)

def is_member(x, a):
	if len(a) == 0:
		return False
	for mem in a:
		if x==mem:
			return True
	return False

print(is_member(1, [1, 2]))
print(is_member('a', ['a']))
print(is_member('b', [1, 2, 'a']))
