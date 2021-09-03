
#player choice
player = ["rock", "paper", "scissors"]

#computer choice 
from random import randint
computer = player[randint(0,2)]

#game
game = False
while game == False:
    player = input("rock, paper, scissors?\n")
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "scissors":
            print("You win!")
        else:
            print("Computer wins!")
    elif player == "paper":
        if computer == "scissors":
            print("Computer wins!") 
        else:
            print("You win!")     
    elif player == "scissors":
        if computer == "rock":
            print("Computer wins!") 
        else:
            print("You win!\n")
    else:
        print("Not a valid answer\n")

    game = False;
    computer = player[randint(0,2)]