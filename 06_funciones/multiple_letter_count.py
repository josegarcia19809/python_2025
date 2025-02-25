"""
multiple_letter_count
Write a function called multiple_letter_count. This function takes in one parameter
(a string) and returns a dictionary with the keys being the letters and the values being
the count of the letter.  Hint: use a dictionary comprehension and count().

Here's how it should work:

multiple_letter_count("awesome")   # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
"""

'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''


# flesh out multiple_letter count:
def multiple_letter_count(text: str) -> dict:
    cuenta = {}
    for letter in text:
        if letter not in cuenta:
            cuenta[letter] = 1
        else:
            cuenta[letter] += 1

    return cuenta


print(multiple_letter_count("awesome"))


def multiple_letter_count2(string):
    return {letter: string.count(letter) for letter in string}