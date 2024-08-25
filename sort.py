from score import *

# sort the records in alphabetical order
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
            elif line.startswith("Final Score:"):
                current_record["Final Score"] = int(line.replace("Final Score: ", ""))

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
                f.write(f"Final Score: {record['Final Score']}\n")
                f.write("\n")

        print(f"{filename} reorganized alphabetically by name successfully.")

    except Exception as e:
        print(f"Error reorganizing {filename}: {str(e)}")

#sort the records in the document based on high score 
def highscore(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()

        records = []
        current_record = {}

        for line in lines:
            line = line.strip()
            if line.startswith("Name:"):
                if current_record: #save the previous record
                    records.append(current_record)
                current_record = {"Name": line.replace("Name: ", "")}
            elif line.startswith("Wins:"):
                current_record["Wins"] = int(line.replace("Wins: ",""))
            elif line.startswith("Losses"):
                current_record["Losses"] = int(line.replace("Losses: ", ""))
            elif line.startswith("Ties:"):
                current_record["Ties"] = int(line.replace("Ties: ", ""))
            elif line.startswith("Final Score:"):
                current_record["Final Score"] = int(line.replace("Final Score: ", ""))

        if current_record: #Add the last record
            records.append(current_record)

        #sort the records alphabeticallty by name
        records.sort(key=lambda x: x["Final Score"], reverse=True)

        #write the sorted records back to the file
        with open(filename, 'w') as f:
            for record in records:
                f.write(f"Name: {record['Name']}\n")
                f.write(f"Wins: {record['Wins']}\n")
                f.write(f"Losses: {record['Losses']}\n")
                f.write(f"Ties: {record['Ties']}\n")
                f.write(f"Final Score: {record['Final Score']}\n")
                f.write("\n")

        print(f"{filename} reorganized by high score successfully.")

    except Exception as e:
        print(f"Error reorganizing {filename}: {str(e)}")