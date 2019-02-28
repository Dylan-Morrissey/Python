import random
import time

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']

def start(): 
	print "Welcome to Dylan's blackjack.\nTo continue press any key."
	raw_input("Any key: ")
	firsthand()
	print "\n"

def firsthand():
	card1 = randomcard()
	card2 = randomcard()
	c1, c1v = cardValue(card1)
	c2, c2v = cardValue(card2)
	hc1, hc2, houseScore = houseCards()
	num = c1v + c2v
	print "\nDealing cards...\n"
	time.sleep(2)
	print "Your two cards are %r and %r" % (c1, c2)
	print "You have %d points" % num
	print "The house's two cards are %r and %r with a score of %d" % (hc1, hc2, houseScore)
	print "Do you want to hold or hit?"
	choice = raw_input("> ")
	if choice == "hit":
		secondhand(num, c1, c2, houseScore)
	elif choice == "hold":
		score(num, houseScore)
	else:
		print "What was that?"
		firsthand()

def secondhand(num , c1, c2, houseScore):
	card3 = randomcard()
	c3, c3v = cardValue(card3)
	print "You now have the following cards %r, %r and %r" % (c1, c2, c3)
	num = num + c3v
	if num < 21:
		print "you have a score of %d" % num
		print "Do you want to hit or hold?"
		choice = raw_input("> ")
		if choice == 'hit':
			thirdhand(num, c1, c2, c3, houseScore)
		elif choice == 'hold':
			score(num, houseScore)
		else:
			print "Invalid option restarting game."
			start()
	else :
		score(num, houseScore)

def thirdhand(num, c1, c2, c3, houseScore):
	card4 = randomcard()
	c4, c4v = cardValue(card4)
	print "You now have the following cards %r, %r, %r and %r" % (c1, c2, c3, c4)
	num = num + c4v
	print "You have a total score of %d" % num
	score(num, houseScore)

def score(points, houseScore):
	if (points > 21):
		print "Bust"
		exit(0)
	elif (points == 21):
		print "BlackJack!!!!!!!!!!!!!!!"
		exit(0)
	elif (points > houseScore):
		print "Concratulations you won the round!"
	elif (points == houseScore):
		print "Draw!"
	else:
		print "You lost this round!"

def randomcard():
	card = random.choice(cards)
	return card

 
def cardValue(card):
	if card == 'A':
		card = 'Ace'
		cardval = 11
	elif card == 'J':
		card = 'Jack'
		cardval = 10
	elif card == 'Q':
		card = 'Queen'
		cardval = 10
	elif card == 'K':
		card = 'King'
		cardval = 11
	else:
		cardval = card

	return (card, cardval)


def houseCards():
	card1 = randomcard()
	card2 = randomcard()
	c1, c1v = cardValue(card1)
	c2, c2v = cardValue(card2)
	houseNum = c1v + c2v
	return (c1, c2, houseNum)

start()