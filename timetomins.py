# Script Name   : timetomins.py
# Author        : Dylan Morrissey
# Created       : 14th March 2019
# Description   : Simple programme which converts time into minutes and also lets you see how long you have left in work.

from datetime import datetime
import re

def currentTime():
	time = str(datetime.now().time())
	timesplit = re.findall(r"[\w]+", time)
	del timesplit[-1]
	return time, timesplit

def twentyFourHour(timesplit):
	if (int(timesplit[0]) <= 24) and (int(timesplit[1]) < 60) and (int(timesplit[2]) < 60):
		hourstomins = int(timesplit[0]) * 60 
		secondstomins = round(int(timesplit[2]) / 60.0, 2)
		return hourstomins + int(timesplit[1]) + secondstomins
	else:
		return 'Error not a valid 24 hour time.'

def twelveHour(timesplit):
	if int(timesplit[0]) < 12:
		if timesplit[2] == 'AM':
			hourstomins = int(timesplit[0]) * 60
			minstomins = int(timesplit[1])
			return hourstomins + minstomins
		elif timesplit[2] == 'PM':
			hourstomins = (int(timesplit[0]) +12) * 60  
			mintomins = int(timesplit[1])
			return hourstomins + mintomins
	else:
		return 'Error not a valid 12 hour time.\n'

def workleft():
	finishTime = raw_input("Print what time do you finish work? eg: 17:00 : ")
	timesplit = re.findall(r"[\w]+", finishTime)
	timesplit.insert(len(timesplit), '00')
	finishtimeinmins = twentyFourHour(timesplit)
	curentmins = twentyFourHour(currentTime()[1])
	timeleft = finishtimeinmins - curentmins
	return timeleft

def menu():
	print "1) Convert the current time to minutes.\n2) Convert a twenty four hour time to minutes.\n3) Convert a twelve Hour time to minutes.\n4) How much time you have left in work."
	option = raw_input("Please choose an option: ")
	try:
		if option == '1':
			time = currentTime()[0]
			mins = twentyFourHour(currentTime()[1])
			print "%s has %r minutes." % (time, mins)
			print "You are currently %.2f%% through the day.\n" % ((mins/1440)* 100)
		elif option == '2':
			time = raw_input("Please enter the time you want to know in minutes (HH:MM:SS): ")
			timesplit = re.findall(r"[\w]+", time)
			twentyFourHour(timesplit)
			print "%s has %r minutes.\n" % (time, twentyFourHour(timesplit))
		elif option == '3':
			time = raw_input("Please enter the time you want to know in minutes (HH:MM AM/PM): ")
			timesplit = re.findall(r"[\w]+", time)
			twelveHour(timesplit)
			print "%s has %r minutes.\n" % (time, twelveHour(timesplit))
		elif option == '4':
			timeleft = workleft()
			hours = str(timeleft / 60.0).split('.')
			hour = int(hours[0])
			mins = float(hours[1]) * 0.6
			print "You have %d hours and %d minutes left." % (hour, (round(mins/ 1000000000)))
			workday = int(raw_input("How many hours is your shift?"))
			print "You are %.2f%% through work.\n" % (100 - (timeleft/(workday*60) * 100))
		else:
			print "\nInvalid option try again!"
		menu()
	except TypeError, ValueError:
		menu()
menu()
