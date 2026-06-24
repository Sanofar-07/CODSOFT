import random

user = input("Choose rock, paper, scissors: ")

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("It is a tie!")

elif  user == "rock" and computer == "scissors":
    print("You win!")

elif user == "paper" and computer == "rock":
    print("You win!")

elif user == "scissors" and computer == "paper":
    print("You win!")

else:
    print("Computer wins!")