# ASCII Codes Dictionary
# This is a bit different. Every character has an ASCII code (basically, a number that represents it).
# Python has a function called chr() that will return a string if you provide the corresponding integer ASCII code.
# For example:
# chr(65)  will return  'A'
# chr(66)  will return  'B'
# All the way up to:
# chr(90)  will return  'Z'
# Your task is to create dictionary that maps ASCII keys to their corresponding letters.
# Use a dictionary comprehension and chr() . Save the result to the answer variable.
# You only need to care about capital letters (65-90).
# The end result will look like this:
# {
#     65: 'A',
#     66: 'B',
#     67: 'C',
#     68: 'D',
#     69: 'E',
#     70: 'F',
#     71: 'G',
#     72: 'H',
#     73: 'I',
#     74: 'J',
#     75: 'K',
#     76: 'L',
#     77: 'M',
#     78: 'N',
#     79: 'O',
#     80: 'P',
#     81: 'Q',
#     82: 'R',
#     83: 'S',
#     84: 'T',
#     85: 'U',
#     86: 'V',
#     87: 'W',
#     88: 'X',
#     89: 'Y',
#     90: 'Z'
# }

answer = {number: chr(number) for number in range(65, 91)}
print("-" * 100)
print(answer)
