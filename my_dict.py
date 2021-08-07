# Import the required packages including json for serializing objects, arrays, numbers, strings, booleans etc
import json
from histogram import alphabet,test_dups,test_miss,histogram

# use json.dumps() function to convert a Python object into a json string
# this is done to enable the histogram function to hash the data without
# throwing errors
john = json.dumps({'platform':('Udacity','Cousera')})
kim = json.dumps({'platform':'Udacity'})
ronny = json.dumps({'platform':'freecodecamp'})
alice = json.dumps({'platform':'freecodecamp'})
damian = json.dumps({'platform':('Udacity','Cousera')})

# create a dictionary and assign values serialized using json.dumps()
students_dict = {'John':john,'Kim':kim,'Ronny':ronny,'Alice':alice,'Damian':damian}

# define a function invert_dict that accepts a dictionary as a parameter
def invert_dict(d):
     # assign a new variable 'inverse' to an empty dictionary
     inverse = dict()
     # Loop through each key in the dictionary
     # and for each extract the value
     for key in d:
          val = d[key]
          # Check if the value exists in the new dictionary
          # turn each of the list items into separate keys in 
          # the inverted dictionary. 
          if val not in inverse:
               inverse[val] = [key]
          else:
               inverse[val].append(key)
     # return a list of values for each key
     return inverse
# Print the Original Dictionary
print("Original Dictionary \n\n {}".format(students_dict))
print("")
# Print the Inverted Dictionary
print("Inverted Dictionary \n\n {}".format(invert_dict(students_dict)))


