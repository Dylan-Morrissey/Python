# Sets the car varible to 100
cars = 100
# Sets the space_in_a_car to floating 4.0
space_in_a_car = 4.0
# Sets the Drives to 30
drivers = 30
# Sets the passengers to 90
passengers = 90
# Sets the cars_not_driven varible to cars minus drives
cars_not_driven = cars - drivers
# Sets the cars_driven varible to the drives
cars_driven = drivers
# Sets teh carpool_capacity to equal the cars driven by space in a car
carpool_capacity = cars_driven * space_in_a_car
# Sets the average_passenegers_per_car to passanges divided by cars_driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars_driven, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car."