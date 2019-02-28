# Imports sys module and argv from that module
from sys import argv
# Takes in two arguments from the cmd
script, filename = argv
# opens the file name specififed in arg 2
txt = open(filename)
# prints the file name
print "Here's your file %s:" % filename
# prints the contents of the txt file.
print txt.read()
txt.close()
# Takes user input for the file name again
print "Type the filename again:"
file_again = raw_input("> ")
# opens the file the user inputted
txt_again = open(file_again)
# prints the contentes of the file 
print txt_again.read()
txt_again.close()

#script, filename = argv

#print "File: %s" % filename

#txt = open(filename)
#contents = txt.read()
#print "Here's what's inside %s:\n %s" % (filename, contents)
