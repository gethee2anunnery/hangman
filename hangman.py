import random
import csv


def prompt_name():
	print "Please enter your name."
	name = raw_input('> ')
	print "Welcome to hangman, %s! To get started, please choose a letter." % name

def validate_input(letter):
	input_valid = len(letter) == 1 and letter.isalpha()
	return input_valid

def prompt_letter():
	letter = raw_input('..> ')
	is_valid = validate_input(letter)

	if not is_valid:
		print "That is not a valid input. Please try again."
		letter = prompt_letter()
	else:
		print "You chose '%s'!" % (letter)

	return letter


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


def check_for_win(populated_word, secret_word):
	if not '_' in populated_word:
		print "You won!!"
		play_again()
		
	else:
		print "No win yet. Keep going!"


def get_word():
	word_list = csv.reader(open('word_list.csv', 'r'))
	word_list = sum([i for i in word_list],[]) #To flatten the list
	return random.choice(word_list)



def take_turn(secret_word, populated_word, guess_list, turn_counter):
	print "Your secret word -> %s" % populated_word
	print "Your guesses so far -> %s" % guess_list

	chosen_letter = prompt_letter()

	if chosen_letter:
		if chosen_letter in guess_list:
			print "You already guessed that letter! Give us a different one."
			take_turn(secret_word, populated_word, guess_list,turn_counter)
		else:
			turn_counter = turn_counter + 1
			guess_list.append(chosen_letter)
			if chosen_letter in list(secret_word):
				print "You got one right!"
				populate_word(secret_word, populated_word, guess_list)

			else:
				print "No %s in that word. Guess again." % chosen_letter

	take_turn(secret_word, populated_word, guess_list, turn_counter)


def start_game():
	prompt_name()
	guess_list = []
	turn_counter = 0
	secret_word = get_word()
	populated_word = ['_' for letter in list(secret_word) ]
	take_turn(secret_word, populated_word, guess_list, turn_counter)

MAX_TURNS = 10
start_game()

