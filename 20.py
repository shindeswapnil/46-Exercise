'''
Represent a small bilingual lexicon as a Python dictionary in the following fashion 
{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} 
and use it to translate your Christmas cards from English into Swedish. That is, 
write a function translate() that takes a list of English words and returns a list of Swedish words.
'''

def translate(l):
	d={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
	return list(map(lambda x:d[x]if x in d else x,l))

l=['merry','and','new','sad']  
print(translate(l))

	



