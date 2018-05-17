'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''
from csv import reader, writer


def update_users(old_first_name, old_last_name, new_first_name, new_last_name):
    with open("users.csv") as csvfile:
        csv_reader = reader(csvfile)
        rows = list(csv_reader)
        print(rows)

    users_updated = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = writer(csvfile)
        csv_writer.writerow(rows[0])
        for row in rows[1:]:
            if row[0] == old_first_name and row[1] == old_last_name:
                csv_writer.writerow([new_first_name, new_last_name])
                users_updated += 1
            else:
                csv_writer.writerow(row)

    return "Users updated: {}.".format(users_updated)


print(update_users("Ricardo", "Oliveira", "Richard", "Sr"))
