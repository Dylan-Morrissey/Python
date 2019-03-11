# Script Name   : passwordGenerator.py
# Author        : Dylan Morrissey
# Created       : 11th March 2019
# Description   : Script which is used to randomly generate a password of your specifications.
import random

def passwordGen(passlen, option):
	password = ''	
	pwchars = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
 	['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 
 	['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ], 
 	['!', '"', '#', '$', '&', '%', "'", ')', '(', '*', '+', ',', '-', '.', '/', ';', ':', '<', '=', '>', '?', '@', '[', ']', '{', '}', '_', '`', '|', '\\', '^', '~']]

	for i in range(passlen):
		if option == 1:
			ran = random.choice(pwchars[:-3])
			ranchar = random.choice(ran)
			password = password + ranchar
		elif option == 2:
			ran = random.choice(pwchars[1:-2])
			ranchar = random.choice(ran)
			password = password + ranchar
		elif option == 3:
			ran = random.choice(pwchars[:-2])
			ranchar = random.choice(ran)
			password = password + ranchar
		elif option == 4:
			ran = random.choice(pwchars[:-1])
			ranchar = random.choice(ran)
			password = password + ranchar
		elif option == 5:
			ran = random.choice(pwchars)
			ranchar = random.choice(ran)
			password = password + ranchar

	print "Your password is: %s\n" % password
	raw_input("Press any key to continue.")

print '-' * 50
print "Welcome to the password generator."
print '-' * 50
def menu():
	try:
		print "1) Generate a password with only uppercase characters.\n2) Generate a password with only lowercase characters.\n3) Generate a password with uppercase and lowercase characters.\n4) Generate a password with uppercase, lowercase and numbers.\n5) Generate a password with uppercase, lowercase, numbers and special characters."
		option = int(raw_input("Please select one of the options: "))
		passlen = int(raw_input("Please enter how long you want the password to be? 12-24 : "))	
		passwordGen(passlen, option)
		menu()
	except (ValueError, IndexError):
		print "Error with input generating password of lenght 24 with upper lower number and special characters!"
		passlen = 24
		option = 5
		passwordGen(passlen, option)
		menu()

menu()
 		

