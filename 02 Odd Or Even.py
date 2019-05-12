"""
Ask the user for a number. 
Depending on whether the number is even or odd, 
print out an appropriate message to the user.
"""

number = int(input("Give me a number: "))
check = int(input("give me a number to divide by: "))

if number % 4 == 0:
    print("%i is a multiple of 4" % number)
elif number % 2 == 0:
    print("%i is an even number" % number)
else: 
    print("%i is NOT an even number" % number)

if number % check == 0:
    print(number, "divides evenly by", check)
else:
    print(number, "does not divide evenly by", check)