people = 30 
cars = 40 
buses = 15


if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else: 
	print "We still can't decide"

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay at home then."
# (cars > people) and (buses > cars)
if cars > people and buses > cars:
	print "People and buses"