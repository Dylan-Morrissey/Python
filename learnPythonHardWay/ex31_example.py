
name = raw_input("Please enter your name? ")

if name == "":
	name = "User"

print "Hello, %s. What kind of food are you in the mood for tonight?" % name
print """
1) Chinese
2) American
3) Mexican
4) Italian
5) Japanise
6) Chipper
7) Home food

Please select the number what you would like.
""" 

cuisine = raw_input("> ")

if cuisine == "1":
	print "Chinese good choice."
	print "Please enter what you would like to order"
	corder = raw_input("Order: ")
	print "You order for %s has been placed." % corder
elif cuisine == "2":
	print "We only have two Americans in the area which one would you like?"
	print "option 1: Rockin' Joe's\noption 2: Eddie Rockets"
	aresturant = raw_input("Diner: ")
	if aresturant == "1":
		print "What would you like from rockin' joe's:"
		aorder1 = raw_input("order: ")
		print "Your order of %s from %s has been placed" % (aorder1, "Rockin' Joe's")

