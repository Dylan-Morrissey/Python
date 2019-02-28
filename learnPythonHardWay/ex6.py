
# Sets x variable to string with format of 10 
x = "There are %d types of people." % 10
# Sets binary = to string 
binary = "binary"
# Sets variable to string
do_not = "don't"
# Sets y to String with two formatters from binary and dont
y = "Those who know %s and those who %s" % (binary, do_not)
#Print the x and y varible
print x
print y
# Prints the x and y varible again but adds them to a string using %r formatter
print "I said: %r." % x
print "I also said: %r." %y 
# Sets varible to boolean false
hilarious = False 
# Sets varible to string with formatterd to add varible above
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
# Creates new strings
w = "This is the left side of..."
e = "a string with a right side."
# Adds the new string together
print w + e
