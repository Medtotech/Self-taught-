#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner
# and ask if the players want to start a new game)

#Remember the rules:
#Rock beats scissors
#Scissors beats paper
#Paper beats rock


player_1 = input("Enter either rock, paper,  scissors: ")
player_2 = input("Enter either rock, paper,  scissors: ")

while player_1 != player_2:
    if player_1 == "rock" and player_2 == "scissors":
        print( "Congratulations!!! Player 1, you are the winner")
        print("do you want to start a new game?")
        break

    elif player_2 == "rock" and player_1 == "scissors":
        print( "Congratulations!!! Player 2, you are the winner")
        print("do you want to start a new game?")
        break

    elif player_1 == "Scissors" and player_2 == "paper":
        print( "Congratulations!!! Player 1, you are the winner")
        print("do you want to start a new game?")
        break

    elif player_2 =="Scissors" and player_1 == "paper":
        print( "Congratulations!!! Player 2, you are the winner")
        print("do you want to start a new game?")
        break
        
    elif player_1 == "paper" and player_2 == "rock":
        print( "Congratulations!!! Player 1, you are the winner")
        print("do you want to start a new game?")
        break

    elif player_2 == "paper" and player_1 == "rock":
        print( "Congratulations!!! Player 2, you are the winner")
        print("do you want to start a new game?")
        break

    
        

