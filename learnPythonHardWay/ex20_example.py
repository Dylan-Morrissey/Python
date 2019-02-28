from sys import argv

script, filename = argv

def print_all(file):
	print file.read()

def rewind(file):
	file.seek(0)

def print_a_line(line_count, file):
	print line_count, file.readline()

file = open(filename)

print print_all(file)

rewind(file)

line_count = 1
print_a_line(line_count, file)
line_count += 1
print_a_line(line_count, file)
line_count += 1
print_a_line(line_count, file)