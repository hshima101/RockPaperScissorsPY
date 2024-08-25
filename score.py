
#calculate the scores from the document 
def finalscore(wins, losses, ties):
    print()
    final = int(wins)*2 + int(losses)*-1 + int(ties)
    finalScore = str(final)
    return finalScore

    
    