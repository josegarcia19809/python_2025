# For this exercise, you'll be working with a file called users.csv . Each row of data consists of two columns: a user's first name, and a user's last name.
#
# Implement the following function:
#
# add_user : Takes in a first name and a last name and adds a new user to the users.csv file.


'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
'''

from csv import writer, DictWriter


def add_user(name="Dwayne", lastname="Johnson"):
    with open("users.csv", "a+") as file:
        csv_writer = writer(file)
        csv_writer.writerow([name, lastname])


add_user()


"""
Add User CSV Solution
import csv
 
def add_user(first_name, last_name):
    with open("users.csv", "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([first_name, last_name
"""
