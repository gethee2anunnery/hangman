import random
import csv


def name_prompt():
	print "Please enter your name."
	name = raw_input('> ')
	print "Welcome to Hangman, %s! To get started, please choose a letter." % (name)

def validate_input(input):
	input_valid = len(input) == 1 and input.isalpha()
	input_is_guess = input == "0"
	if (input_valid or input_is_guess):
		return True
	else:
		return False


def validate_guess(secret_word, guess):
	if secret_word == guess:
		print "That's right!! You won!! The secret word was '%s'." % (secret_word)
		play_again()
	else:
		print "Nope. Back to the drawing board."


def guess_prompt():
	guess = raw_input('What\'s your guess?..> ')
	return guess

def letter_prompt():
	print "Please type a letter, or type a 0 to make a guess."
	input = raw_input('..> ')
	is_valid = validate_input(input)

	if not is_valid:
		print "That is not a valid input. Please try again."
		input = letter_prompt()
	else:
		print "You chose '%s'!" % (input)

	return input


def populate_word(secret_word, populated_word, guess_list):
	letters = list(secret_word)
	index = 0

	for letter in set(guess_list):
		index = 0
		while index < len(secret_word):
			index = secret_word.find(letter, index)
			if index == -1:
				break
			populated_word[index] = letter
			index +=1
	check_for_win(populated_word, secret_word)


def play_again():
	print "Play again? y/n"
	answer = raw_input('>> ')
	if answer == 'y':
		start_game()
	elif answer == 'n':
		raise SystemExit
	else:
		print "That is not one of the valid options. Enter either 'y' or 'n'."
		play_again()

def max_turns():
	print "You've used up your turns. You lose!"
	play_again()


def check_for_win(populated_word, secret_word):
	if not '_' in populated_word:
		print "You won!! The secret word was '%s'." % (secret_word)
		play_again()
	else:
		pass


def get_word():
	word_list = csv.reader(open('word_list.csv', 'r'))
	word_list = sum([i for i in word_list],[]) #To flatten the list
	return random.choice(word_list)


def take_turn(secret_word, populated_word, guess_list, turn_counter):
	maxed_out = MAX_TURNS - turn_counter < 1
	if maxed_out:
		max_turns()

	else:
		print "You have %s turns left." % (MAX_TURNS - turn_counter)
		print "Your secret word -> %s" % populated_word
		print "Your guesses so far -> %s" % guess_list
		
		chosen_letter = letter_prompt()

		is_guess = chosen_letter == "0"
		if chosen_letter and not is_guess:

			if chosen_letter in guess_list:
				print "You already guessed that letter! Give us a different one."
				take_turn(secret_word, populated_word, guess_list,turn_counter)
			else:
				guess_list.append(chosen_letter)
				turn_counter = turn_counter + 1

				if chosen_letter in list(secret_word):
					number_instances = list(secret_word).count(chosen_letter)

					if number_instances < 2:
						print "There is 1 %s in your secret word." % chosen_letter
					else:
						print "There are %s instances of %s in your secret word." % (number_instances, chosen_letter)

					populate_word(secret_word, populated_word, guess_list)

				else:
					print "No %s in that word." % chosen_letter

		elif chosen_letter and is_guess:
			guess = guess_prompt()
			validate_guess(secret_word, guess)


		take_turn(secret_word, populated_word, guess_list, turn_counter)


def start_game():
	name_prompt()
	guess_list = []
	turn_counter = 0
	secret_word = get_word()
	populated_word = ['_' for letter in list(secret_word) ]
	take_turn(secret_word, populated_word, guess_list, turn_counter)

MAX_TURNS = 10
start_game()

