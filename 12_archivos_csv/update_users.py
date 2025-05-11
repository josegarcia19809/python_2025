"""
For this exercise, you'll be working with a file called users.csv . Each row of data consists of two columns: a user's first name, and a user's last name.

Implement the following function:

update_users : Takes in an old first name, an old last name, a new first name, and a new last name. Updates the users.csv file so that any user whose first and last names match the old first and last names are updated to the new first and last names. The function should return a count of how many users were updated.
"""

'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''

from csv import reader, writer


def update_users(old_name, old_lastname, new_name, new_lastname):
    users_list = []
    with open("users.csv") as file:
        csv_reader = reader(file)
        users_list = list(csv_reader)

    counter = 0
    with open("users.csv", "w") as file:
        csv_writer = writer(file)
        for user in users_list:
            if user[0] == old_name and user[1] == old_lastname:
                csv_writer.writerow([new_name, new_lastname])
                counter += 1
            else:
                csv_writer.writerow([user[0], user[1]])
                
    return f"Users updated: {counter}."


print(update_users("Grace", "Hopper", "Hello", "World"))  # Users updated: 1.)

print(update_users("Colt", "Steele", "Boba", "Fett"))

print(update_users("Not", "Here", "Still not", "Here"))

"""
Update Users Solution
import csv
 
def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
 
    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)
 
    return f"Users updated: {count}."
"""
