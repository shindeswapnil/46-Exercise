#Using the higher order function filter(), define a function filter_long_words()
#that takes a list of words and an integer n and returns the list of words that are longer than n.

def filter_long_words(n,lst):
	return list(filter(lambda x:len(x)>n,lst))
	
lst=['that','takes','a','list','of','words']
print(filter_long_words(4,lst))



