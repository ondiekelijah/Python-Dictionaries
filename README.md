# Python-Dictionaries

```
alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 
```
From Section 11.2 of: 

Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 
```
def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d 
```

Copy the code above into your program but write all the other code for this assignment yourself. Do not copy any code from another source. 
## Part 1 

Write a function called has_duplicates that takes a string parameter and returns True if the string has any repeated characters. Otherwise, it should return False.  

Implement has_duplicates by creating a histogram using the histogram function above. Do not use any of the implementations of has_duplicates that are given in your textbook. Instead, your implementation should use the counts in the histogram to decide if there are any duplicates. 

Write a loop over the strings in the provided test_dups list. Print each string in the list and whether or not it has any duplicates based on the return value of has_duplicates for that string. For example, the output for "aaa" and "abc" would be the following. 

aaa has duplicates
abc has no duplicates 

Print a line like one of the above for each of the strings in test_dups. 

## Part 2 

Write a function called missing_letters that takes a string parameter and returns a new string with all the letters of the alphabet that are not in the argument string. The letters in the returned string should be in alphabetical order. 

Your implementation should use a histogram from the histogram function. It should also use the global variable alphabet. It should use this global variable directly, not through an argument or a local copy. It should loop over the letters in alphabet to determine which are missing from the input parameter. 

The function missing_letters should combine the list of missing letters into a string and return that string. 

Write a loop over the strings in list test_miss and call missing_letters with each string. Print a line for each string listing the missing letters. For example, for the string "aaa", the output should be the following. 

```aaa is missing letters bcdefghijklmnopqrstuvwxyz```

If the string has all the letters in alphabet, the output should say it uses all the letters. For example, the output for the string alphabet itself would be the following. 

```abcdefghijklmnopqrstuvwxyz uses all the letters ```

Print a line like one of the above for each of the strings in test_miss. 

Submit your Python program. It should include the following. 

The provided code for ```alphabet, test_dups, test_miss, and histogram```. 
Your implementation of the has_duplicates function. 
A loop that outputs duplicate information for each string in test_dups. 
Your implementation of the **missing_letters** function. 
A loop that outputs missing letters for each string in test_miss. 
Also submit the output from running your program. 

Your submission will be assessed using the following Aspects.

* Does the program include a function called has_duplicates that takes a string parameter and returns a boolean?
* Does the has_duplicates function call the histogram function? 
* Does the program include a loop over the strings in test_dups that calls has_duplicate on each string? 
* Does the program correctly identify whether each string in test_dups has duplicates? 
* Does the program include a function called missing_letters that takes a string parameter and returns a string? 
* Does the missing_letters function call the histogram function?
* Does the missing_letters function use the alphabet global variable directly?
* Does the program include a loop over the strings in test_miss that calls missing_letters on each string?
* Does the program correctly identify the missing letters for each string in test_miss, including each string that "uses all the letters"?


Create a Python dictionary that returns a list of values for each key. The key can be whatever type you want. 

Design the dictionary so that it could be useful for something meaningful to you. Create at least three different items in it. Invent the dictionary yourself. Do not copy the design or items from some other source. 

Next consider the invert_dict function from Section 11.5 of your textbook. 

> From Section 11.5 of: 
> Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 
```
def invert_dict(d):
     inverse = dict()
     for key in d:
          val = d[key]
          if val not in inverse:
               inverse[val] = [key]
          else:
               inverse[val].append(key)
     return inverse 
  ```

Modify this function so that it can invert your dictionary. In particular, the function will need to turn each of the list items into separate keys in the inverted dictionary. 

Run your modified invert_dict function on your dictionary. Print the original dictionary and the inverted one. 

Include your Python program and the output in your Learning Journal submission. 

Describe what is useful about your dictionary. Then describe whether the inverted dictionary is useful or meaningful, and why.
