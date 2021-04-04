from random import randint

player = input("What is your choice? ").lower()
computer = randint(0, 2)

if computer == 0:
    computer = "Rock"
elif computer == 1:
    computer = "Paper"
else:
    computer = "Scissors"

print(f"The computer chose {computer}")

if player.lower() == computer.lower():
    print("You and the computer chose the same option, this game is a draw")

elif player == "rock":
    if computer == "Scissors":
        print("You chose Rock and the computer chose Scissors. Your Rock Wins!")
    elif computer == "Paper":
        print("You chose Rock and the computer chose Paper. The Computer's Paper Wins!")

elif player == "paper":
    if computer == "Rock":
        print("You chose Paper and the computer chose Rock. Your Paper Wins!")
    elif computer == "Scissors":
        print(
            "You chose Paper and the computer chose Scissors. The Computer's Scissors Wins!")

elif player == "scissors":
    if computer == "Rock":
        print("You chose Scissors and the computer chose Rock. The Computer's Rock Wins!")
    elif computer == "Paper":
        print("You chose Scissors and the computer chose Paper. Your Scissors Wins!")

else:
    print("You entered something that wasn't Rock, Paper or Scissors")
