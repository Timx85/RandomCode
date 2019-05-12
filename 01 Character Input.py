"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them 
the year that they will turn 100 years old.
"""
import datetime

# Ask for name and age
now = datetime.datetime.now()
name = input("What is your name? ")
age = int(input("What is your age? "))

#calculate till 100
tempAge = 100 - age
hunderYear = now.year + tempAge

print("Your name is: %s" % name)
print("You reach the age of 100 in the year %i" % hunderYear)
end = input("Press enter to close program")