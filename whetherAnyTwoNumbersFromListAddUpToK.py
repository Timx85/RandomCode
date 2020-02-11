# Problem #1 [Easy] 
# This problem was recently asked by Google. 
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k. 
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17. 
# Bonus: Can you do this in one pass? 

list = [1, 3, 5, 7, 9] 
testNr = 17

def addNrs(list,k):
    # getting length of list 
    length = len(list) 
    # Iterating the index 
    # same as 'for i in range(len(list))' 
    for i in range(length): 
        print(list[i]) 

print(addNrs(list,testNr))
  