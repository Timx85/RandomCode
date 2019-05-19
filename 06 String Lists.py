"""
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
"""

word = str(input("Give me a word: "))
# s = word[0:len(word)]
# r = word[::-1]
# print(s)
# print(r)

# if s == r:
#     print("The given word is a palindrome")
# else:
#     print("The given word is NOT a palindrome")

if word[0:len(word)] == word[::-1]:
    print("The given word is a palindrome")
else:
    print("The given word is NOT a palindrome")