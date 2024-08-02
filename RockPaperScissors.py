import random, sys

def rockpaperscissors():
    print("Rock Paper Scissors")
    
    #These variables keep track of your records
    wins = 0
    losses = 0
    ties = 0

    while True:
        print("Press '0' for Rock Press '1' for Paper Press '2' for Scissors")
        print("Press q to quit")

        guess_str = input()

        #invalid input checking somewhere here

        #This section could be its own function
        if guess_str == 'q':
            winst = str(wins)
            lossest = str(losses)
            tiest = str(ties)

            print("Wins: " + winst)
            print("Losses: " + lossest)
            print("Ties " + tiest)
            sys.exit()
        #######################################


        guess = int(guess_str)

        print("Rock")
        print("Paper")
        print("Scissors!")

        #Make this its own function
        secretNumber = random.randint(0,2)

        if secretNumber == 0:
            print("Rock!")
        elif secretNumber == 1:
            print("Paper!")
        elif secretNumber == 2:
            print("Scissors!")

        if secretNumber == 0 and guess == 0:
            print("Tie!")
            ties = ties + 1

        elif secretNumber == 1 and guess == 1:
            print("Tie!")
            ties = ties + 1

        elif secretNumber == 2 and guess == 2:
            print("Tie!")
            ties = ties + 1

        elif secretNumber == 0 and guess == 1:
            print("Win!")
            wins = wins + 1

        elif secretNumber == 1 and guess == 2:
            print("Win!")
            wins = wins + 1

        elif secretNumber == 2 and guess == 0:
            print("Win!")
            wins = wins + 1

        elif secretNumber == 1 and guess == 0:
            print("Lose!")
            losses = losses + 1

        elif secretNumber == 2 and guess == 1:
            print("Lose!")
            losses = losses + 1

        elif secretNumber == 0 and guess == 2:
            print("Lose!")
            losses = losses + 1
        ##############################
    