'''
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words. 
Write it in three different ways: 1) using a for-loop, 2) using the higher order function map(), and 3) using list comprehensions
'''
def length_for(lst):
	length=[]
	for word in lst:
		length.append(len(word))
	return length

def length_map(lst):
	return list(map(lambda x:len(x),lst))

def length_lcomp(lst):
	length=[len(l) for l in lst]
	return length

lst=['ABC','PQRS','XY','LMNOPQR']
print('Using For Loop : ',length_for(lst))
print('Using For Map(): ',length_map(lst))
print('Using For List comp : ',length_lcomp(lst))
