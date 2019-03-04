largestnum = [11,21,32,41,54,56,76,83,23,10]

largest = 0
for i in largestnum:
	if i > largest:
		largest = i
	elif largest > i:
		largest = largest
		