name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.00 * 2.54 # CM 
weight = 180 / 2.2 # Kgs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Lets talk about %s." % name
print "He's %d CM tall." % height
print "He's %d Kgs heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usally %s depending on the coffee." % teeth

# this line is tricky to get it exactly right 
print "If I add %d, %d and %d I get %d." % (age, height, weight, age + height + weight)