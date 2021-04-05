from random import choice
for i in range(3):
    player = input("What is your choice? ").lower()
    options = ["Rock", "Paper", "Scissors"]

    computer = choice(options)

    print(player)
    print(f"The Computer chose {computer}")

    if player.lower() == computer.lower():
        print("You and the computer chose the same option, this game is a draw")

    elif player == "rock":
        if computer == "Scissors":
            print("You chose Rock and the computer chose Scissors. Your Rock Wins!")
        elif computer == "Paper":
            print(
                "You chose Rock and the computer chose Paper. The Computer's Paper Wins!")

    elif player == "paper":
        if computer == "Rock":
            print("You chose Paper and the computer chose Rock. Your Paper Wins!")
        elif computer == "Scissors":
            print(
                "You chose Paper and the computer chose Scissors. The Computer's Scissors Wins!")

    elif player == "scissors":
        if computer == "Rock":
            print(
                "You chose Scissors and the computer chose Rock. The Computer's Rock Wins!")
        elif computer == "Paper":
            print("You chose Scissors and the computer chose Paper. Your Scissors Wins!")

    else:
        print("You entered something that wasn't Rock, Paper or Scissors")
