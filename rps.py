### ROCK PAPER SCISSORS ###
import random

# Welcome message
print("WELCOME TO ROCK PAPER SCISSORS!\n")
print("You can type 'r', 'p', or 's' when making your choice and to play again.")

#Set variables
rpsdict = {"r":"rock","p":"paper","s":"scissors"}
playagain = "y"
newchoice = ""
playerwins = 0
computerwins = 0
draws = 0

# Game loop
while playagain == "y":
    
# Prompt user for choice
    if newchoice in ["r","p","s"]:
        playerchoice = newchoice
    else:
        playerchoice = ""
        while playerchoice not in ["rock", "r", "paper", "p", "scissors", "s"]:
            playerchoice = input("Please select rock, paper, or scissors. (r/p/s):  \n").lower()
        playerchoice = playerchoice[0]
    
    computerchoice = random.choice(["r","p","s"])

# Print choices
    playerstring = rpsdict[playerchoice]
    computerstring = rpsdict[computerchoice]
    print(f"You selected {playerstring} and the computer selected {computerstring}.")

# Draw Conditions    
    if playerchoice == computerchoice:
        print("It is a draw.")
        draws += 1
    
# Rock Conditions  
    if playerchoice == "r" and computerchoice == "p":
        print("YOU LOSE.")
        computerwins +=1
    elif playerchoice == "r" and computerchoice == "s":
        print("YOU WIN.")
        playerwins += 1

# Paper Conditions  
    if playerchoice == "p" and computerchoice == "r":
        print("YOU WIN.")
        playerwins += 1
    elif playerchoice == "p" and computerchoice == "s":
        print("YOU LOSE.")
        computerwins +=1

#Scissor Conditions  
    if playerchoice == "s" and computerchoice == "r":
        print("YOU LOSE.")
        computerwins +=1
    elif playerchoice == "s" and computerchoice == "p":
        print("YOU WIN.")
        playerwins += 1
    
# Print overall stats       
    print(f"Your record is {playerwins}-{computerwins}-{draws} (W-L-D)")
    
# Determine if user wants to play again
    playagain = ""
    while playagain not in ["yes", "y", "no", "n", "r", "p", "s"]:
        playagain = input("Do you want to play again? (y/n or r/p/s):  \n").lower()
        
        newchoice = ""
        if playagain in ["r","p","s"]:
            newchoice = playagain
            playagain = "y"
        elif playagain == "yes":
            playagain == "y"
            print("")