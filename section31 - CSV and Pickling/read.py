from csv import reader, DictReader

# THIS DOES READ THE FILE BUT IT DOESN'T PARSE IT!
# BAD!!!!!!
with open("fighters.csv") as file:
    data = file.read()

# Using reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    next(csv_reader)  # To skip the headers
    for fighter in csv_reader:
        # Each row is a list
        # Use index to access data
        print(f"{fighter[0]} is from {fighter[1]}")

# Example where data is cast into a list
with open("fighters.csv") as file:
    csv_reader = reader(file)
    data = list(csv_reader)
    print(data)

# Reading/Parsing CSV Using a DictReader:
with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # Each row is an OrderedDict!
        print(row['Name'])  # Use keys to access data

# Specifying a delimiter
with open("fighters_semicolon.csv") as file:
    csv_reader = reader(file, delimiter=';')
    for row in csv_reader:
        # each row is a list
        print(row)
