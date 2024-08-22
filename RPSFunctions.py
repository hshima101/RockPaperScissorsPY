import random, sys

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
            name = input("Enter your name: ")
            print_results(wins, losses, ties, name)
            write('scores.txt', wins, losses, ties, name)
            alphabetical('scores.txt')
            sys.exit()
        
        result, wins, losses, ties = guess(guess_str, wins, losses, ties)
        print(result)
        


#function will do input checking before sending input to 
#program 
def inputCheck(input):
    return input in ['0', '1', '2', 'q']

def print_results(wins, losses, ties, name):
    print(name)
    print("Wins: " + str(wins))
    print("Losses: " + str(losses))
    print("Ties: " + str(ties))

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

def score(wins, loses, ties, name):
    print()
            
def write(filename, wins, losses, ties, name):
    try: 
        with open(filename, 'a') as f: #'w' for write mode, 'a' for append mode
            f.write(f"Name: {name}\n")
            f.write(f"Wins: {wins}\n")
            f.write(f"Losses: {losses}\n")
            f.write(f"Ties: {ties}\n")
            f.write("\n") 
        print(f"Data written to {filename} successfully")
    except Exception as e:
        print(f"Error writing to {filename}")

def load(filename):
    try:
        with open(filename, 'r') as file:
            data = [int(line.strip()) for line in file]
        return data
    except Exception as e:
        print(f'Error loading data from {file}: {str(e)}')
        return []

def alphabetical(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()

        # Parse the contents into a list of dictionaries 
        records = []
        current_record = {}

        for line in lines:
            line = line.strip()
            if line.startswith("Name:"):
                if current_record: 
                    records.append(current_record)
                current_record = {"Name": line.replace("Name: ", "")}
            elif line.startswith("Wins:"):
                current_record["Wins"] = int(line.replace("Wins: ",""))
            elif line.startswith("Losses"):
                current_record["Losses"] = int(line.replace("Losses: ", ""))
            elif line.startswith("Ties:"):
                current_record["Ties"] = int(line.replace("Ties: ", ""))

        if current_record: #Add the last record
            records.append(current_record)

        #sort the records alphabeticallty by name
        records.sort(key=lambda x: x["Name"])

        #write the sorted records back to the file
        with open(filename, 'w') as f:
            for record in records:
                f.write(f"Name: {record['Name']}\n")
                f.write(f"Wins: {record['Wins']}\n")
                f.write(f"Losses: {record['Losses']}\n")
                f.write(f"Ties: {record['Ties']}\n")
                f.write("\n")

        print(f"{filename} reorganized alphabetically by name successfully.")

    except Exception as e:
        print(f"Error reorganizing {filename}: {str(e)}")

    

