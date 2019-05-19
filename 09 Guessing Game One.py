"""
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell 
them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)

Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import random

nrOfQuesses = 0

rightNumber = random.randint(1, 9)

while True:
    playerQuess = input("Guess a number between and including 1 and 9. Or type EXIT to stop: ")
    nrOfQuesses = nrOfQuesses + 1

    if playerQuess == '':
        print("Invalid choise")
    elif playerQuess.upper() == 'EXIT':
        break
    elif int(playerQuess) > rightNumber:
        print("%s is bigger than the right number" %playerQuess)
    elif int(playerQuess) < rightNumber:
        print("%s is smaller than the right number" %playerQuess)
    elif int(playerQuess) == rightNumber:
        print("You guessed the right number! Congratulations \n You guessed it right in %i tries" %nrOfQuesses)
        break
    else: print("Invalid choise")

