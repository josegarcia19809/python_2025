"""
For this exercise, you'll be working with a file called users.csv . Each row of data consists of two columns: a user's first name, and a user's last name.

Implement the following function:

delete_users : Takes in a first name and a last name. Updates the users.csv file so that any user whose first and last names match the inputs are removed. The function should return a count of how many users were removed.
"""

'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''

from csv import reader, writer


def delete_users(name, lastname):
    users_list = []
    with open("users.csv") as file:
        csv_reader = reader(file)
        users_list = list(csv_reader)

    counter = 0
    with open("users.csv", "w") as file:
        csv_writer = writer(file)
        for user in users_list:
            if user[0] == name and user[1] == lastname:
                counter += 1
            else:
                csv_writer.writerow([user[0], user[1]])

    return f"Users deleted: {counter}."


print(delete_users("Grace", "Hopper"))
print(delete_users("Colt", "Steele"))
print(delete_users("Not", "Here"))

"""
Delete Users CSV Solution
import csv
 
def delete_users(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
 
    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == first_name and row[1] == last_name:
                count += 1
            else:
                csv_writer.writerow(row)
 
    return f"Users deleted: {count}."
"""
