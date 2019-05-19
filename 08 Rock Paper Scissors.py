"""
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner, 
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
choises =	{
  1: "Rock",
  2: "Paper",
  3: "Scissors"
}

again = 'Y'
print("Welcome to Rock Paper Scissors")

while again.upper() == 'Y': 
    print("Pick a number \n 1 = Rock \n 2 = Paper \n 3 = Scissors")

    player1 = int(input("Choise player 1: "))

    while player1 not in choises:
        print("Not a valid choise! Pick again: ")
        player1 = int(input("Choise player 1: "))

    player2 = int(input("Choise player 2: "))

    while player2 not in choises:
        print("Not a valid choise! Pick again: ")
        player2 = int(input("Choise player 2: "))

    if player1 == player2:
        print("Draw!")
        print("Both picked the same")
    elif player1 == 1 and player2 == 3:
        print("Player 1 wins!")
        print("Rock beats Scissors")
    elif player1 == 1 and player2 == 2:
        print("Player 2 wins!")
        print("Paper beats Rock")
    elif player1 == 2 and player2 == 1:
        print("Player 1 wins!")
        print("Paper beats Rock")
    elif player1 == 2 and player2 == 3:
        print("Player 2 wins!")
        print("Scissors beats Paper")
    elif player1 == 3 and player2 == 1:
        print("Player 2 wins!")
        print("Rock beats Scissors")
    elif player1 == 3 and player2 == 2:
        print("Player 1 wins!")
        print("Scissors beats Paper")
    else:
        print("Invalid choises")

    again = input("Want to play again? Y/N ")
