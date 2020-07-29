import random
def start_game():
	print("------------------------------------")
	print("Welcome to the Number Guessing Game!")
	print("------------------------------------")
	print()
	play_again = 'y'
	high_score = 10
	while play_again.lower() == 'y':
		number = random.randint(1,10)
		count = 1
		guess = None
		while guess != number:
			guess = input("Pick a number between 1 and 10: ")
			try:
				guess = int(guess)
			except ValueError: 
				print("Invalid entry. Please enter a number value between 1-10")
			else:
				if not (1 <= guess <= 10):
					print("Invalid entry. Please enter a number value between 1 and 10")
				elif guess == number:
					print("\n You got it! It took you {} tries.".format(count))
				else:
					word = 'lower' if guess > number else 'higher'
					print("It's {}!! Guess again:  ".format(word))
					count += 1
		if count < high_score:
			high_score = count
		play_again = input(" \nWould you like to play again?[y]es/[n]o: ")
		if play_again.lower() == 'y':
			print("\n\nThe HIGHSCORE is {}".format(high_score))
		else:
			print("Closing game, see you next time!")
start_game()