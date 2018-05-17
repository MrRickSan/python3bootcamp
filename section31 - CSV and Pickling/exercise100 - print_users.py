from csv import DictReader
'''
print_users() # None
# prints to the console:
# Colt Steele
'''


def print_users():
    with open('users.csv') as file:
        csv_reader = DictReader(file)
        for row in csv_reader:
            print(f"{row['First Name']} {row['Last Name']}")


print_users()
