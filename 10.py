#Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise.
# You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops.

def overlapping(l1,l2):
	for mem1 in l1:
		for mem2 in l2:
			if mem1==mem2:
				return True
	return False

print(overlapping([1,2,3],[3,4,5]))
print(overlapping(['a','b','c'],['e','f','c']))
print(overlapping(['swap','avi','ziva'],['samu','raj','rahul']))
print(overlapping(['swap','avi','ziva'],['samu','raj','ziva']))
