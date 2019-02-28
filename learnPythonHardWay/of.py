user_input = raw_input("Enter Your word: ")
user_input = user_input.upper()
wordArray = list(user_input)

values_dict = {'A' : 1, 'E' : 1, 'I' : 1, 'O' : 1, 'U' : 1, 'L' : 1,
              'N' : 1, 'N' : 1, 'S' : 1, 'T' : 1, 'R' : 1,
              'D' : 2, 'G' : 2, 'B' : 3, 'C' : 3, 'M' : 3, 'P' : 3,
              'F' : 4, 'H' : 4, 'V' : 4, 'W' : 4, 'Y' : 4,
              'K' : 5, 'J' : 8, 'X' : 8, 'Q' : 10, 'Z' : 10,}

def get_word_value(wordArray, values_dict):
    word_pts = 0
    num = 0
    for letter in wordArray:
    	num = num + values_dict[letter]
      
    print "Word Points %d, Test Good." % num
get_word_value(wordArray, values_dict)