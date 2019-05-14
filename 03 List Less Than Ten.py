"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

varNumber = int(input("Give me a number: "))

#Solution in multiple lines
# for number in a:
#     if number < varNumber:
#         b.append(number)

#print(b)

# Can also be done in 1 line
print([number for number in a if number < varNumber])