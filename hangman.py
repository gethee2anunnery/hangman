import random
import csv


def prompt_name():
	print "enter your name"
	name = raw_input('> ')
	print "welcome to hangman, %s! To get started, please choose a letter." % name
	return name

def prompt_letter():
	letter = raw_input('..> ')
	print "you chose '%s'!" % (letter)

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
	if not '_' in populated_word:
		print "YOU WON!!"
		play_again()
		
	else:
		take_turn(secret_word, populated_word)


def get_word():
	word_list = csv.reader(open('word_list.csv', 'r'))
	word_list = sum([i for i in word_list],[]) #To flatten the list
	return random.choice(word_list)

def take_turn(secret_word, populated_word, win=False):
	chosen_letter = prompt_letter()
	guess_list.append(chosen_letter)
	print "guess list %s" % guess_list

	if not win:
		if chosen_letter in list(secret_word):
			print "you got one!"
			populate_word(secret_word,populated_word,guess_list)
		else:
			print "no %s in that word, try again" % chosen_letter

		take_turn(secret_word,populated_word)


def start_game():
	prompt_name()
	guess_list = []
	secret_word = get_word()
	populated_word = ['_' for letter in list(secret_word) ]
	take_turn(secret_word, populated_word)

guess_list = []
start_game()

