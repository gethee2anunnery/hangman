import random
import csv


def prompt_name():
	print "enter your name"
	name = raw_input('> ')
	print "welcome to hangman, %s! To get started, please choose a letter." % name

def validate(letter):
	input_valid = len(letter) == 1 and letter.isalpha()
	return input_valid


def prompt_letter():
	print "prompting letter..."
	letter = raw_input('..> ')
	is_valid = validate(letter)

	if not is_valid:
		print "That is not a valid input. Please try again."
		letter = prompt_letter()
		
	else:
		print "you chose '%s'!" % (letter)
		
	return letter


def populate_word(secret_word, populated_word, guess_list):
	print "populating word..."
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
	print "Your word ---> %s"  % populated_word
	check_for_win(populated_word, secret_word)

def play_again():

	print "play again? y/N"
	answer = raw_input('>>')
	if answer=='y':
		start_game()
	elif answer=='N':
		raise SystemExit
	else:
		print "that is not one of the valid options."
		play_again()


def check_for_win(populated_word, secret_word):
	print "checking for win..."
	if not '_' in populated_word:
		print "YOU WON!!"
		play_again()
		
	else:
		print "no win! going again"


def get_word():
	print "getting word..."
	word_list = csv.reader(open('word_list.csv', 'r'))
	word_list = sum([i for i in word_list],[]) #To flatten the list
	return random.choice(word_list)

def take_turn(secret_word, populated_word, guess_list):
	print "taking turn..."

	print "your guesses so far -> %s" % guess_list
	chosen_letter = prompt_letter()

	if chosen_letter:
		if chosen_letter in guess_list:
			print "You already guessed that letter! Give us a different one."
			take_turn(secret_word,populated_word, guess_list)
		else:
			guess_list.append(chosen_letter)
			if chosen_letter in list(secret_word):
				print "You got one right!"
				populate_word(secret_word,populated_word,guess_list)

			else:
				print "No %s in that word. Guess again." % chosen_letter

	take_turn(secret_word,populated_word, guess_list)


def start_game():
	print "starting game..."
	prompt_name()
	guess_list = []

	secret_word = get_word()
	populated_word = ['_' for letter in list(secret_word) ]
	take_turn(secret_word, populated_word, guess_list)

guess_list = []
start_game()

