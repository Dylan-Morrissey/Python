# Script Name   : irishReg.py
# Author        : Dylan Morrissey
# Created       : 19th February 2019
# Description   : Simple use of pythons dictionarys to search for where an irish car registration city identifier is from and also allows you to play a quiz agains this city identifier.
import random, time

# Dictionary which assigns the plate apprviation to the countie its from
counties = { 
	'W': 'Waterford',
	'KK': 'Kilkenny',
	'D': 'Dublin',
	'G': 'Galway',
	'C': 'Cork',
	'WX': 'Wexford',
	'T': 'Tipperary',
	'WW': 'Wicklow',
	'KY': 'Kerry',
	'CE': 'Clare',
	'CW': 'Carlow',
	'OY': 'Offaly',
	'KE': 'Kildare',
	'M': 'Meath',
	'LH': 'Louth',
	'RN': 'Roscommon',
	'MO': 'Mayo',
	'SO': 'Sligo',
	'LM': 'Leitrim',
	'LD': 'Longford',
	'WM': 'Westmeath',
	'MN': 'Monaghan',
	'WD': 'Waterford District',
	'L': 'Limrick'
}

# assigns the provence to the registration plate 
provience = {
	'W': 'Munster',
	'KK': 'Lenister',
	'D': 'Lenister',
	'G': 'Connacht',
	'C': 'Munster',
	'L':'Munster',
	'WD': 'Munster',
	'WX': 'Lenister',
	'T': 'Munster',
	'WW': 'Lenister',
	'KY': 'Munster',
	'CE': 'Munster',
	'CW': 'Lenister',
	'OY': 'Lenister',
	'KE': 'Lenister',
	'M': 'Lenister',
	'LH': 'Lenister',
	'RN': 'Connacht',
	'MO': 'Connacht',
	'SO': 'Connacht',
	'LM': 'Connacht',
	'LD': 'Lenister',
	'WM': 'Lenister',
	'MN': 'Ulster'
}

# variable which will be use to place 40 - just for ux purpose 
spacing = '-' * 40

# function which takes in user input and then prints out the details about the reg and also asked if they want to know what provience the reg is from
def reginfo(reg, key):
	if (reg == key):
		print "%s\n%s registration is from %s\n" % (spacing, reg, counties[reg])
		userRes = raw_input("Would you like to know which provience the reg is from? Y/N \n").upper()

		if (userRes == ('Y' or 'YES')):
			print "%s is in the provience of %s\n%s" % (counties[reg], provience[reg], spacing)
			time.sleep(0.9)
			menu()		
		else:
			print spacing
			time.sleep(0.3)
			menu()

# function which s 
def regsearch():
	print "%s\n Example input: CW" % spacing
	reg = raw_input("Please enter the Reg you want to know: ").upper()
	for key in counties:
		reginfo(reg, key)		
	print "Invalid option."
	menu()
# this function formats the answer to match the dictionary format of capital first letter lower evrything else
def answerFormat(answer):
	return answer[0].upper() + answer[1:].lower()

# this is the function which runs the quiz 
def quiz():
	print spacing
	questions = int(raw_input("Please enter how many questions you would like to be asked? "))
	if questions > 24:
		questions = 10
		quizQuestions(questions)
	else:
		quizQuestions(questions)

def quizQuestions(questions):
	points = 0
	quizReg = dict(counties.items())	
	wrong = {}
	for i in range(questions):
		randomReg = random.choice(quizReg.keys())
		print "Question %d: Where is %s city code from?" % (i + 1, randomReg)
		try:
			answer = raw_input('> ')
			if answer == '':
				answer = 'pass'
			else:
				answer = answer

			answer = answerFormat(answer)
			if (quizReg[randomReg] == answer):
				points += 1
			else:
				wrong[randomReg] = answer
				del quizReg[randomReg]
		except (ValueError, IndexError):
			menu()
 		
 	score(points, wrong, questions)
	menu()
	

def score(points, wrong, questions):
	for q, w in wrong.items():
		print "%r was wrong for %r." % (w, q)
		
	floatscore = points/1.00
	floatquestions = questions/1.00	
	percent = (floatscore/floatquestions) * 100.00
	
	print "You got %d%%" % percent
	if (  40.00 <= percent < 55.00):
		print "You got a grade of D"
	elif (55.00 <= percent < 70.00):
		print "You got a grade of C"
	elif (70.00 <= percent < 85.00):
		print "You got a grade of B"
	elif (85 <= percent <= 100):
		print "Well Done you got a grade of A"
	else:
		print "Print you got a grade of F"
	print "You got %d/%d questions correct.\n%s" % (points, questions, spacing)	

# Function used to print the start menu
def menu():
	print "Welcome to the Irish Car Registration game.\n1. Want to know more about the city identifier of the car registration plate?\n2. Want to test your knowledge with a quiz?"
	option = raw_input("Please select an option: ")
	if (option == '1'):
		regsearch()
	elif (option == '2'):
		quiz()
	else: 
		print "\nInvalid Option Please Select again \n%s" % spacing
		time.sleep(0.5)
	menu()

menu()
