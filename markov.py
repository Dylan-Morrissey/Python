import numpy as np
import random

transition = {"AP1":{"AP1AP1" : 0.6, "AP1AP2" : 0.2, "AP1AP3" : 0.2}, "AP2":{"AP2AP1": 0.2, "A2AP2" : 0.6, "AP2AP3" : 0.2}, "AP3":{"AP3AP1" : 0.4,"A3AP2" : 0.2, "AP3AP3" : 0.4}}

for i in transition:
	if float(sum(transition[i].values())) > 1.0:
		print "Error with transitionMatrix %d Probability > 1" % i
		exit()
	elif float(sum(transition[i].values())) < 1.0:
		print "Error with transitionMatrix %d Probability < 1" % i
		exit()


def movement(time):
	# Starting accesspoint 	
	ap = np.random.choice(transition.keys())
	print "Starting accesspoint: %s" % ap

	# Shall store the sequence of states taken. So, this only has the starting state for now.
	movementlist = [ap]
	prob = 1.0
	for i in range(time):
		if ap == "AP1":
			change = np.random.choice(transition[ap].keys(),replace=True, p=transition[ap].values())
			print "change : %r" % change
			if change == "AP1AP1":
				prob = prob * transition[ap][change]
				movementlist.append(ap)
			elif change == "AP1AP2":
				prob = prob * transition[ap][change]
				ap = "AP2"
				movementlist.append(ap)
			else:
				prob = prob * transition[ap][change]
				ap = "AP3"
				movementlist.append(ap)
		elif ap == "AP2":
			change = np.random.choice(transition[ap].keys(),replace=True, p=transition[ap].values())
			if change == "AP2AP2":
				prob = prob * transition[ap][change]
				movementlist.append(ap)
			elif change == "AP2AP1":
				prob = prob * transition[ap][change]
				ap = "AP1"
				movementlist.append(ap)
			else:
				prob = prob * transition[ap][change]
				ap = "AP3"
				movementlist.append(ap)
		elif ap == "AP3":
			change = np.random.choice(transition[ap].keys(),replace=True, p=transition[ap].values())
			if change == "AP3AP3":
				prob = prob * transition[ap][change]
				movementlist.append(ap)
			elif change == "AP3AP1":
				prob = prob * transition[ap][change]
				ap = "AP1"
				movementlist.append(ap)
			else:
				prob = prob * transition[ap][change]
				ap = "AP2"
				movementlist.append(ap)
		else:
			print "Error"

	print "Movements: %s" % movementlist
	print "End state after %d hours: %s" % (time, ap)
	print "Probability of the possible sequence of states: %d%%" % (int (prob*100))

movement(2)