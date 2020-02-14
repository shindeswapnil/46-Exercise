'''
In a game of Lingo, there is a hidden word, five characters long. The object of the game is to find this word by guessing,
and in return receive two kinds of clues: 1) the characters that are fully correct, with respect to identity as well as to position,
and 2) the characters that are indeed present in the word, but which are placed in the wrong position. Write a program with which
one can play Lingo. Use square brackets to mark characters correct in the sense of 1), and ordinary parentheses to mark characters
correct in the sense of 2). Assuming, for example, that the program conceals the word "tiger", you should be able to interact with 
it in the following way:
>> import lingo
snake
Clue: snak(e)
fiest
Clue: f[i](e)s(t)
times
Clue: [t][i]m[e]s
tiger
Clue: [t][i][g][e][r]
'''

from random import randrange
def lingo(lst):
	target=str(lst[randrange(0,len(lst))])
	ip=input()
	while ip!=target:
		output=''
		for pos, char in enumerate(ip):
			if char in target:
				if target[pos] == ip[pos]:
					output += '[' + char + ']'
				else:
					output += '(' + char + ')'
			else:
				output += char
		print("Clue: ",output)
		ip=input('')
	print( "Found !")
                                                                                          
lingo(['alley', 'tally', 'valet', 'tiger', 'white'])


