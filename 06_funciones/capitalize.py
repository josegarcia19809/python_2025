"""
capitalize
Write a function called capitalize. This function accepts a string and returns
the same string with the first letter capitalized.  You may want to use slices
to help you out.
1.	capitalize("jamaica") # "Jamaica"
2.	capitalize("chicken") # "Chicken"


'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

def capitalize():
    pass

"""


def capitalize(word: str) -> str:
    return word[0].upper() + word[1:]


print(capitalize("jamaica"))
print(capitalize("chicken"))


def capitalize2(string):
    return string[:1].upper() + string[1:]
