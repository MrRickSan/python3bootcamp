from csv import writer
'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johonson
'''


def add_user(first_name, last_name):
    with open('users.csv', 'a') as file:
        csv_writer = writer(file)
        csv_writer.writerow([first_name, last_name])


add_user('Ricardo', 'Oliveira')
