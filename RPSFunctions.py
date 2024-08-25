import random, sys
from sort import *
from score import *
from filewrite import *

#general function will encapsulate other functions
#this function will also keep score
def rps():
    wins = 0
    losses = 0
    ties = 0

    while True:
        print("Press '0' for Rock Press '1' for Paper Press '2' for Scissors")
        print("Press q to quit")

        guess_str = input()
        if not inputCheck(guess_str):
            print("invalid input. please try again")
            continue
        
        if guess_str == 'q':
            final = finalscore(wins, losses, ties)
            name = input("Enter your name: ")
            print_results(wins, losses, ties, name, final)
            #scores will be organized in alphabetical order
            write('scores.txt', wins, losses, ties, name, final)
            #scores will be organized by score (highest to lowest)
            write('highscore.txt', wins, losses, ties, name, final)
            alphabetical('scores.txt')
            highscore('highscore.txt')
            del wins, losses, ties, name, final
            sys.exit()
        
        result, wins, losses, ties = guess(guess_str, wins, losses, ties)
        print(result)

#function will do input checking before sending input to 
#program 
def inputCheck(input):
    return input in ['0', '1', '2', 'q']

def print_results(wins, losses, ties, name, final):
    print(name)
    print("Wins: " + str(wins))
    print("Losses: " + str(losses))
    print("Ties: " + str(ties))
    print("Final Score: " + str(final))

def guess(guess_str, wins, losses, ties):
     
    choices = ["Rock", "Paper", "Scissors"]
    secret_number = random.randint(0, 2)
    comp_choice = choices[secret_number]
    user_choice = choices[int(guess_str)]

    result_message = f"COMP: {comp_choice}! You: {user_choice}"

    if comp_choice == user_choice:
        result_message += " Tie!"
        ties += 1
    elif (comp_choice == "Rock" and user_choice == "Paper") or \
         (comp_choice == "Paper" and user_choice == "Scissors") or \
         (comp_choice == "Scissors" and user_choice == "Rock"):
        result_message += " You win!"
        wins += 1
    else:
        result_message += " You lose!"
        losses += 1

    return result_message, wins, losses, ties
            


