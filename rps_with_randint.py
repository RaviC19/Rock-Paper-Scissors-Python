from random import randint

computer_wins = 0
player_wins = 0
winning_score = 5

while computer_wins < winning_score and player_wins < winning_score:
    player = input("What is your choice? ").lower()
    computer = randint(0, 2)

    if computer == 0:
        computer = "Rock"
    elif computer == 1:
        computer = "Paper"
    else:
        computer = "Scissors"

    if player.lower() == computer.lower():
        print(
            f"You and the computer chose the same option, this game is a draw. The score is you have {player_wins} whilst the computer has {computer_wins}")

    elif player == "rock":
        if computer == "Scissors":
            player_wins += 1
            print(
                f"You chose Rock and the computer chose Scissors. Your Rock Wins! The score is you have {player_wins} whilst the computer has {computer_wins}")
        elif computer == "Paper":
            computer_wins += 1
            print(
                f"You chose Rock and the computer chose Paper. The Computer's Paper Wins! The score is you have {player_wins} whilst the computer has {computer_wins}")

    elif player == "paper":
        if computer == "Rock":
            player_wins += 1
            print(
                f"You chose Paper and the computer chose Rock. Your Paper Wins! The score is you have {player_wins} whilst the computer has {computer_wins}")
        elif computer == "Scissors":
            computer_wins += 1
            print(
                f"You chose Paper and the computer chose Scissors. The Computer's Scissors Wins! The score is you have {player_wins} whilst the computer has {computer_wins}")

    elif player == "scissors":
        if computer == "Rock":
            computer_wins += 1
            print(
                f"You chose Scissors and the computer chose Rock. The Computer's Rock Wins! The score is you have {player_wins} whilst the computer has {computer_wins}")
        elif computer == "Paper":
            player_wins += 1
            print(
                f"You chose Scissors and the computer chose Paper. Your Scissors Wins! The score is you have {player_wins} whilst the computer has {computer_wins}")

    else:
        print("You entered something that wasn't Rock, Paper or Scissors")

if computer_wins > player_wins:
    print("The computer reached 5 before you could so unfortunately you lost!")
elif player_wins > computer_wins:
    print("Congratulations! You got to 5 wins before the computer could and you won!")
