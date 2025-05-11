"""
For this exercise, you'll be working with a file called users.csv . Each row of data consists of two columns: a user's first name, and a user's last name.

Implement the following function:

find_user : Takes in a first name and a last name and searches for a user with that first and last name in the users.csv file. If the user is found, find_user  returns the index where the user is found. Otherwise it returns a message stating that the user wasn't found.
"""

'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''
from csv import reader


def find_user(name, lastname):
    with open("users.csv") as file:
        csv_reader = reader(file)
        next(csv_reader)  # To skip the headers
        index = 1
        for user in csv_reader:
            if user[0] == name and user[1] == lastname:
                return index
            index += 1
    return f"{name} {lastname} not found."


print(find_user("Colt", "Steele"))  # 1
print(find_user("Alan", "Turing"))  # 3
print(find_user("Not", "Here"))  # 'Not Here not found.'


"""
Find User CSV Solution
import csv
 
def find_user(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        for (index, row) in enumerate(csv_reader):
            first_name_match = first_name == row[0]
            last_name_match = last_name == row[1]
            if first_name_match and last_name_match:
                return index
        return f"{first_name} {last_name} not found."
"""