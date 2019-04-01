# Script Name   : GymApp.py
# Author        : Dylan Morrissey
# Created       : 29th March 2019
# Description   : Using Classes in python to build an app which could improve the productivity of a gym.
import json, time
class Person(object):

	def __init__(self, name):
		self.name = name
		self.email = ''
		self.address = 'Unknown'
		self.gender = 'Unspecified'

	def setEmail(self):
		self.email = raw_input("Please enter the email address for %s: " % self.name).lower()
	
	def setAddress(self):
		self.address = raw_input("Please enter the address for %s: " % self.name)

	def setGender(self):
		gender = list(raw_input("Please enter your gender: ").upper())
		if gender[0] == 'M':
			self.gender = 'M'
		elif gender[0] == 'F':
			self.gender = 'F'
		else:
			self.gender = "Unspecified"

	def toString(self, name):
		print "Name: %s, Email: %s, Address: %s, Gender: %s" % (self.name, self.email, self.address, self.gender)

	def getEmail(self):
		return self.email

class Member(Person):
	
	def __init__(self, name):
		super(Member, self).__init__(name)

		self.package = 'Unspecified'
		self.height = 0
		self.startweight = 0

	def heightinput(self):
		height = int(raw_input(("Please enter the height of %s in cm: " % self.name)))
		if (100 <= height <= 300):
			self.height = height
		else:
			print "Invalid Option make sure the height is between 100 and 300 cm."
			self.heightinput()

	def startweightinput(self):
		startweight = int(raw_input("Please enter the startweight in KG: "))
		if (35 <= startweight <= 250):
			self.startweight = startweight
		else:
			print "Invalid Option make sure weight is between 35 and 250 kg."
			self.startweightinput()	
	
	def bodyMassIndex(self):
		heightinmeters = self.height / 100.0
		self.bmi = round(self.startweight/((heightinmeters)**2), 2)

	def determineBMICategory(self):
		bmi = self.bmi
		if bmi < 15.0:
			print "Very Severly underweight."
		elif (15.0 <= bmi <16.0):
			print "Severely Underweight."
		elif (16.0 <= bmi < 18.5):
			print "Underweight."
		elif (18.5 <= bmi < 25.0):
			print "Normal."
		elif (25.0 <= bmi < 30.0):
			print "Overweight."
		elif (30.0 <= bmi < 35.0):
			print "Moderately Obese."
		elif (35.0 <= bmi < 40.0):
			print "Severely Obese."
		elif bmi >= 40.0:
			print "Very Severely Obese"
		else:
			print "Error"

	def isIdealBodyWeightCalc(self):
		fiveFeet = 60.0
		isIdealBodyWeight = 0.0
		heighttoinches = (self.height * 0.3937008)

		if (heighttoinches <= fiveFeet):
			if(self.gender == 'M'):
				isIdealBodyWeight = 50.0
			else:
				isIdealBodyWeight = 45.5
		else:
			if (self.gender == 'M'):
				isIdealBodyWeight = 50 + ((heighttoinches - fiveFeet) * 2.3)
			else:
				isIdealBodyWeight = 45.5 + ((heighttoinches - fiveFeet) * 2.3)

		self.isIdealBodyWeight = isIdealBodyWeight

	def memberToString(self, name):
		print "%s, package: %s, height: %s, Starting weight: %s" % (super(Member, self).toString(name), self.package, self.height, self.startweight)

class PremiumMember(Member):

	def __init__(self, name):
		super(PremiumMember, self).__init__(name)

	def chosenPackage(self, package):
		self.package = package
		
class StudentMember(Member):

	def __init__(self, name):
		super(StudentMember, self).__init__(name)
		self.studentid = 'XXXXXXXX'
		self.college = 'Unspecified'

	def collegeNameInput(self):
		college = raw_input("Please enter the name of your college: ")
		if len(college) > 40:
			collegeNameList = list(college)
			collegeName = ''
			for letter in collegeNameList[:40]:
				collegeName += letter

			self.college = collegeName
		else:
			self.college = college
	
	def studentIdInput(self):
		studentid = raw_input("Please enter your Student ID: ")
		if len(studentid) < 8:
			id = list(studentid)
			xtoadd = int(8 - len(id))
			i = 0
			while i < xtoadd:
				id.append('X')
				i += 1
			
			self.studentid = ''.join(id)
		elif len(studentid) > 8:
			studentidlist = list(studentid)
			self.studentid = ''.join(studentidlist[:8])
		else:
			self.studentid = studentid
		
	def chosenPackage(self, package):
		self.package = package

class Trainer(Person):

	def __init__(self, name):
		super(Trainer, self).__init__(name)

	def specialityInput(self):
		self.speciality = raw_input("Please enter %s's speciality: " % self.name)

class Assessment(StudentMember or PremiumMember):

	def __init__(self, name, trainer):
		super(Assessment, self).__init__(name)
		self.trainer = trainer
	
	def weightinput(self):
		weight = int(raw_input("Please enter the weight in Kg: "))
		if (35 <= weight <= 250):
			self.weigth = weight
		else:
			print "Invalid Input weight must be between 35 - 250 kg"
			self.weightinput()

	def chestinput(self):
		chest = int(raw_input("Please enter the chest size in cm: "))
		if 25 <= chest <= 150:
			self.chest = chest
		else:
			print "Invalid Input chest size must be between 25-150cm."
			self.chestinput()

	def thighinput(self):
		thigh = int(raw_input("Please enter the thigh size in cm: "))
		if 15 <= thigh <= 90:
			self.thigh = thigh
		else:
			print "Invalid Input thigh size must be between 15-90cm."
			self.thighinput()

	def upperarminput(self):
		upperarm = int(raw_input("Please enter the upper-arm size in cm: "))
		if 10 <= upperarm <= 70:
			self.upperarm = upperarm
		else:
			print "Invalid Input upper-arm size must be between 10-70cm."
			self.upperarminput()

	def waistinput(self):
		waist = int(raw_input("Please enter the waist size in cm: "))
		if 20 <= waist <= 150:
			self.waist = waist
		else:
			print "Invalid Input waist size must be between 20-150cm."
			self.waistinput()
	
	def hipsinput(self):
		hips = int(raw_input("Please enter the hips size in cm: "))
		if ((25 <= hips <= 170) and (hips >= self.waist)):
			self.hips = hips
		else:
			print "Invalid Input hips size must be between 20-150cm."
			self.hipsinput()

	def commentinput(self):
		comment = raw_input("Add your comment: ")
		if len(list(comment)) > 100:
			commentlen = list(comment)
			self.comment = ''.join(commentlen[:100])
		else:
			self.comment = comment

class GymAPI(object):
	def __init__(self):
		# Loads the json files upon strating
		self.members = self.loadMembers()
		self.trainers = self.loadTrainers()

	def addMember(self):
		member = int(raw_input("1) Premium Member\n2) Student Member\n"))

		if member == 1:
			premem = PremiumMember((raw_input("Please enter your full name: ")))
			premem.email = raw_input("Please enter your email address: ")
			premem.address = raw_input("Please enter your address: ")
			premem.gender = raw_input("Please enter your Gender: ")
			premem.chosenPackage(raw_input("Please enter your chosen package: "))
			premem.startweightinput()
			premem.heightinput()
			premem.bodyMassIndex()
			premem.determineBMICategory()
			premem.isIdealBodyWeightCalc()
			self.members.append([premem.name, premem.email, premem.address, premem.gender, premem.package, premem.startweight, premem.height, premem.bmi, premem.isIdealBodyWeight])
			self.save()

		elif member == 2:
			studentmem = StudentMember(raw_input("Please enter your full name: "))
			studentmem.email = raw_input("Please enter your email address: ")
			studentmem.address = raw_input("Please enter your address: ")
			studentmem.gender = raw_input("Please enter your Gender: ")
			studentmem.chosenPackage(raw_input("Please enter your chosen package: "))
			studentmem.collegeNameInput()
			studentmem.studentIdInput()
			studentmem.startweightinput()
			studentmem.heightinput()
			self.members.append([studentmem.name, studentmem.email, studentmem.address, studentmem.gender, studentmem.package, studentmem.college, studentmem.studentid, studentmem.startweight, studentmem.height])
			self.save()

		else:
			print "Invalid option"
			self.addMember()
		
	def addTrainer(self):
		newtrainer = Trainer(raw_input("Please enter the trainers name: "))
		newtrainer.specialityInput()
		newtrainer.setEmail()
		newtrainer.setAddress()
		newtrainer.setGender()

		self.trainers.append([newtrainer.name, newtrainer.email, newtrainer.address, newtrainer.gender, newtrainer.speciality])
		self.save()

	def numberofMembers(self):
		if len(self.members) == 0:
			print "We currently have 0 members..."
		else:
			print "We currently have %d members " % len(self.members)
		
	def numberofTrainers(self):
		if len(self.trainers) == 0:
			print "We currently have 0 trainers..."
		else:
			print "We currently have %d trainers " % len(self.trainers)
	# This function prints the list of members/trainers you might notice a u before some values but this is python saying the string is of type unicode. 	
	def allMembers(self):
		for member in self.members:
			print member
	
	def allTrainers(self):
		for trainer in self.trainers:
			print trainer

	def searchMemberByEmail(self):
		emailsearch = raw_input("Please enter the email of the member you are looking for: ").lower()
		for mem in self.members:
			if emailsearch == mem[1]:
				print mem
				raw_input("Press Enter to Contine:")

	def searchTrainerByEmail(self):
		emailsearch = raw_input("Please enter the email of the trainer you are looking for: ").lower()
		for train in self.trainers:
			if emailsearch == train[1]:
				print train
				raw_input("Press Enter to Contine:")


	def listMemberswithIdealWeight(self, members):
		for membr in members:
			if int(membr[8]) == int(membr[5]):
				print membr


	def loadMembers(self):
		file = open('members.json', 'r')
		members = json.load(file)
		return members

	def loadTrainers(self):
		file = open('trainers.json', 'r')
		trainers = json.load(file)
		return trainers

	def save(self):
		file = open('members.json', 'w')
		json.dump(self.members, file)
		file = open('trainers.json', 'w')
		json.dump(self.trainers, file)

def Menu():
	option = int(raw_input("1) Add a new member\n2) Add a new trainer\n3) Number of members\n4) Number of trainers\n5) Retrieve all members\n6) Retrieve all trainers\n7) Search Members by email\n8) Search trainers by email\n9) Save\nPlease select an option:  "))

	if option == 1 :
		GymAPI().addMember()
		print "Member added!" 
		time.sleep(1)
	elif option == 2:
		GymAPI().addTrainer()
		print "Trainer added!"
		time.sleep(1)
	elif option == 3:
		GymAPI().numberofMembers()
		time.sleep(1)
	elif option == 4:
		GymAPI().numberofTrainers()
		time.sleep(1)
	elif option == 5:
		GymAPI().allMembers()
		time.sleep(5)
	elif option == 6:
		GymAPI().allTrainers()
		time.sleep(5)
	elif option == 7:
		GymAPI().searchMemberByEmail()
	elif option == 8:
		GymAPI().searchTrainerByEmail()
	elif option == 9:
		GymAPI().save()
		print "Saving"
		time.sleep(1)
	else:
		print "Invalid Option please select again."

	Menu()

Menu()
