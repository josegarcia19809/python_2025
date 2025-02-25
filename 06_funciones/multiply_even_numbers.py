"""
multiply_even_numbers
Write a function called multiply_even_numbers. This function accepts a list of numbers
and returns the product of all even numbers in the list.


'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers():
    pass

"""

def multiply_even_numbers(list_of_numbers: list)->int:
    result = 1
    for number in list_of_numbers:
        if number % 2 == 0:
            result *= number

    return result

print(multiply_even_numbers([2,3,4,5,6]))