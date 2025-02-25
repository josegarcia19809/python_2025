"""
number_compare
Write a function called number_compare. This function takes in two parameters
(both numbers). If the first is greater than the second, this function returns
"First is greater" If the second number is greater than the first, the function
returns "Second is greater" Otherwise the function returns "Numbers are equal"
"""

'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''


def number_compare(number_1: int, number_2: int) -> str:
    if number_1 > number_2:
        return "First is greater"
    elif number_1 < number_2:
        return "Second is greater"
    else:
        return "Numbers are equal"


print(number_compare(1, 1))  # "Numbers are equal"
print(number_compare(1, 0))  # "First is greater"
print(number_compare(2, 4))  # "Second is greater"
