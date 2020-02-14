'''
Your task in this exercise is as follows:

    Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
    Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of
     opening/closing brackets (in that order), none of which mis-nest.

Examples:

   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK
'''

from random import randrange
import re

def brackets(n):
	i,result,brackets = 0,'','[]'
	while i<n*2:
		result+=brackets[randrange(len(brackets))]
		i+=1

	bracket_string=result
	while len(re.findall(r'\[\]',result))>0:
		result=re.sub(r'\[\]','',result)

	if len(result) > 0:
		print(bracket_string,'NOT OK')
	else:
		print(bracket_string,'OK')

n=int(input('How Many Brackets ? : '))
brackets(n)
