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
Part 1 

Write a function called has_duplicates that takes a string parameter and returns True if the string has any repeated characters. Otherwise, it should return False.  

Implement has_duplicates by creating a histogram using the histogram function above. Do not use any of the implementations of has_duplicates that are given in your textbook. Instead, your implementation should use the counts in the histogram to decide if there are any duplicates. 

Write a loop over the strings in the provided test_dups list. Print each string in the list and whether or not it has any duplicates based on the return value of has_duplicates for that string. For example, the output for "aaa" and "abc" would be the following. 

aaa has duplicates
abc has no duplicates 

Print a line like one of the above for each of the strings in test_dups. 
