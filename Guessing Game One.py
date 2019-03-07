#Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right

import random

random_no = str(random.randint(1, 10))
counter = 0

while  True:
    guess = str ( input( "Guess a number from 1 to 9 : "))
    if guess != "exit":      #conditon to ensure the continuality of the game
        while True:
            counter = counter + 1
            
            if guess < random_no:
                print ("Guess too low")
                break

            elif guess > random_no: 
                print("Guess too high ")
                break

            elif guess == random_no:
                print("CORRECT GUESS!!!!")
                break

    else:  #condition to end game
        print('Thank you for playing')
        break

print ("you guessed " + str(counter) + " times. ")











