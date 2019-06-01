"""
Write a program (function!) that takes a list and 
returns a new list that contains all the elements 
of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using 
a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the 
solution for that in a different function.
"""
import random

def noDuplicateList(a):
    for item in a:
        if item not in newList:
            newList.append(item)
    return newList

inputList = random.sample(range(30), 10)
newList = []

#this one uses sets
def noDuplicateList_set(a):
    return list(set(a))

print(noDuplicateList(inputList))
print(noDuplicateList_set(inputList))