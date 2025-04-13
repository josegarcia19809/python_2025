# using reader

from csv import reader

with open("fighters.csv") as file:
    csv_reader = reader(file)
    next(csv_reader)  # To skip the headers
    for fighter in csv_reader:
        # Each row is a list
        # Use index to access data
        print(f"{fighter[0]} is from {fighter[1]}")

print("-" * 100)

# Example where data is cast into a list
with open("fighters.csv") as file:
    csv_reader = reader(file)
    data = list(csv_reader)
    print(data)

print("-" * 100)

# Reading/Parsing CSV Using A DictReader
from csv import DictReader

with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # Each row is an OrderedDict
        print(row['Name'])  # Use keys to access data
        print(row)
