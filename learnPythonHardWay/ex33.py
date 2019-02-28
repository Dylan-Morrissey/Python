
numbers = []

def whilestudy(max, incriments):
	i = 0

	while i < max:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + incriments
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num


maxnum = int(raw_input("Enter an number: "))
incriments = int(raw_input("What is the incriments? "))
whilestudy(maxnum, incriments)

#for number in range(0,6):
#	print "At the top i is %d" % number
#	numbers.append(number)

#	print "Numbers now: ", numbers
#	print "At the bottom i is %d" % (number + 1)