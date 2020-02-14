'''
Represent a small bilingual lexicon as a Python dictionary in the following fashion 
{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} 
and use it to translate your Christmas cards from English into Swedish. Use the higher order function map()
to write a function translate() that takes a list of English words and returns a list of Swedish words.
'''
def translate(lst):
	data={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
	return list(map(lambda x:data[x] if x in data else False,lst))

lst=["merry","christmas","happy","new","laptop"]
print(translate(lst))
