'''
In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going. A simple set of heuristic rules can be given as follows:

    If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
    If the verb ends in ie, change ie to y and add ing
    For words consisting of consonant-vowel-consonant, double the final letter before adding ing
    By default just add ing

Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form returns its present participle form. Test your function with words such as lie, see, move and hug. However, you must not expect such simple rules to work for all cases.
'''


def make_ing_form(v):
	conso="bcdfghjklmnpqrstvwxz"
	vowel="aeiou"
	avoid=['be','see', 'flee','knee']
	if v in avoid:
		return v+'ing'
	elif v[-1] in conso and v[-2] in vowel and v[-3] in conso:
        	v+=v[-1]
        	return v+'ing'
	elif(v.endswith('ie')==True):
		return v[:-2]+'ying'
	elif(v.endswith('e')==True):
		return v[:-1]+'ing'
	else:
		return v+'ing'

print(make_ing_form('lie'))
print(make_ing_form('see'))
print(make_ing_form('move'))
print(make_ing_form('hug'))
print(make_ing_form('see'))
print(make_ing_form('beg'))

