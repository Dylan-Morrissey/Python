# makes the function cheese and crackers which has two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes_of_crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"


print "We can just give the function number directly:"
# passes 20 and 30 as arguments
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
# sets variable with values below
amount_of_cheese = 10
amount_of_crackers = 50
# passes variables to the function 
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# passes numbers to the functon which need maths
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
# passes variables with addition to function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def twenty_percent(wage):
	netwage = (wage / 100) * 20
	print "\n20 percent of your wage %d is: %d" % (wage, netwage)
	
twenty_percent(10000)
yearly = 20000
twenty_percent(yearly)
twenty_percent(1400 * 12)
twenty_percent(35000 - 5000)
bonus = 10000
twenty_percent(yearly + bonus)
twenty_percent(35000 / 12)
twenty_percent(35000 / 56)
twenty_percent(20000 + 20000)
twenty_percent(10000 + 10000 + 10000 / 4000)
