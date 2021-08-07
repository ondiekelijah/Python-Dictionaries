# import the histogram function ,alphabet,test_miss and test_dups variables from
# the histogram.py file as shown below. We only import the required 

from histogram import alphabet,test_miss

# define a function missing_letters that accepts a string as a parameter
def missing_letters(string):
    # assign a new variable 'result' the values from alphabet
    result = alphabet
    # create and assing a new variable 'compare',the passed string converted into a
    # set(to store multiple items in a single variable) and sorted
    compare = set(sorted(string))
    # Begin comparison
    # Check if a key in the sorted version also appears among the listed characters in the 
    # alphabet variable
    for key in compare:
        if key in alphabet:
            # If the key exists in both,then in the new variable 'result',replace that key with an empty value
            result = result.replace(key, "")
    # return the results which is a list of those missing characters,not found in the alphabet variable
    return result

# Loop through eaach letter in the test_miss list and 
# call missing_letters with each string. 
# Print a line for each string listing the missing letters.
for letters in test_miss:
    if len(missing_letters(letters)) == 0:
        print("{} uses all the letters".format(letters))
    else:
        print("{} is missing {}".format(letters, missing_letters(letters)))

# Create an object from the missing_letters function,with a list of strings
# passed to it
all_missing_letters = missing_letters(test_miss)
# Print the results from the object
print(all_missing_letters)
