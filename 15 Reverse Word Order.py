"""
Write a program (using functions!) that asks the user 
for a long string containing multiple words. 
Print back to the user the same string, except with 
the words in backwards order. 
"""

def reverseWord(inputWord):
    return ' '.join(inputWord.split()[::-1])

inputSencentce = input("Give me a sentence: ")
print(reverseWord(inputSencentce))

