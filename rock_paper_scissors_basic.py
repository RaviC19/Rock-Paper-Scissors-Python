player1 = input("Player1, what is your choice? ")
player2 = input("Player2, what is your choice? ")

if player1 and player2:
    if player1 == player2:
        print("You both chose the same option, this game is a draw")
    elif player1 == "Rock" and player2 == "Scissors":
        print("Player 1 chose Rock and Player 2 chose Scissors. Player 1's Rock Wins!")
    elif player1 == "Rock" and player2 == "Paper":
        print("Player 1 chose Rock and Player 2 chose Paper. Player 2's Paper Wins!")
    elif player1 == "Scissors" and player2 == "Rock":
        print("Player 1 chose Scissors and Player 2 chose Rock. Player 2's Rock Wins!")
    elif player1 == "Scissors" and player2 == "Paper":
        print("Player 1 chose Scissors and Player 2 chose Paper. Player 1's Scissors Wins!")
    elif player1 == "Paper" and player2 == "Rock":
        print("Player 1 chose Paper and Player 2 chose Rock. Player 1's Paper Wins!")
    elif player1 == "Paper" and player2 == "Scissors":
        print("Player 1 chose Paper and Player 2 chose Scissors. Player 2's Scissors Wins!")
    else:
        print("You chose something that wasn't Rock, Paper or Scissors")
else:
    print("It looks like y'all don't want to play Rock, Paper, Scissors?")
