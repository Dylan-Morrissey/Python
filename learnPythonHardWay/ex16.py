# imports argv from sys package
from sys import argv
# takes two arguments
script, filename = argv

print "We're going to erase %s" % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input(">")
# opens the file with write access
print "Opening the file..."
target = open(filename, "w")
# empties the entire file
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
# takes three lines of input
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
# writes the 3 lines given about to the file
target.write(("%s\n%s\n%s\n" % (line1, line2, line3))) 

print "And finally, we close it."
# closes the file
target.close()