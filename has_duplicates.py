# import the histogram function ,alphabet,test_miss and test_dups variables from
# the histogram.py file as shown below

from histogram import test_dups,histogram

# define a function has_duplicates that accepts a string as a parameter
def has_duplicates(s):
    # Loop through each of the words in the passes string
     for d in s:
         # For each word in the string,pass it as parameter for the histogram function
         # then create an object from the function histogram with the word as a parameter 
          dx = histogram(d)
          # loop through the key and value items in the object created from the histogram function
          # check if the value is more than 1 which establishes that the word has a duplicate(s)
          if set(v for k,v in dx.items() if v >1):
              print ("{} has duplicates".format(d))
          # However if the value is less than 1,the word has no duplicate,hence we print no duplicates
          elif set(v for k,v in dx.items() if v <=1):
              print ("{} has no duplicates".format(d))
# Call the has_duplicates function with test_dups list as a parameter
has_duplicates(test_dups)

