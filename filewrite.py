#functions for file management

def write(filename, wins, losses, ties, name, final):
    try: 
        with open(filename, 'a') as f: #'w' for write mode, 'a' for append mode
            f.write(f"Name: {name}\n")
            f.write(f"Wins: {wins}\n")
            f.write(f"Losses: {losses}\n")
            f.write(f"Ties: {ties}\n")
            f.write(f"Final Score: {final}\n")
            f.write("\n") 
        print(f"Data written to {filename} successfully")
    except Exception as e:
        print(f"Error writing to {filename}")
    f.close()

def load(filename):
    try:
        with open(filename, 'r') as file:
            data = [int(line.strip()) for line in file]
        return data
    except Exception as e:
        print(f'Error loading data from {file}: {str(e)}')
        return []