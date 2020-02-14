'''
Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1 and 20.
(Source: http://inventwithpython.com) This is how it should work when run in a terminal:
'''
'''
>> import guess_number
Hello! What is your name?
Torbjörn
Well, Torbjörn, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Torbjörn! You guessed my number in 3 guesses!
'''

from random import randrange
def guess_the_number():
	print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
	user_name=input('\nHello! What is your name ? : ')
	print('\nWell, {} , I am thinking of a number between 1 and 20.\n'.format(user_name))
	number=randrange(1,21)
	tries=0
	while True:
		guess=int(input('Take a Guess : '))
		tries+=1
		if guess==number:
			print('\nGood job, {} ! You guessed my number in {} guesses!\n'.format(user_name,tries))
			print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
			break
		elif guess < number :
			print('\nYour guess is too Low !\n')
		elif guess > number :
			print('\nYour guess is too High !\n')
	
guess_the_number()


