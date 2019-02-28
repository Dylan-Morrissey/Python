from sys import argv

script, filename = argv

txt = open(filename)
contents = txt.read()

print "Lets have a look inside %s: %s" % (filename, contents)

txt.close()
