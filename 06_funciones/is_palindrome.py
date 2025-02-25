"""
is_palindrome
Write a function called is_palindrome. A Palindrome is a word, phrase, number, or other
sequence of characters which reads the same backward or forward. This function should
take in one parameter and returns True or False depending on whether it is a palindrome.
As a bonus, allow your function to ignore whitespace and capitalization so that
is_palindrome('a man a plan a canal Panama') returns True.
"""

'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''


def is_palindrome(text: str) -> bool:
    text = text.lower()
    text = text.replace(' ', '')
    return text == text[::-1]


print(is_palindrome('testing'))  # False
print(is_palindrome('tacocat'))  # True
print(is_palindrome('hannah'))  # True
print(is_palindrome('robert'))  # False
print(is_palindrome('amanaplanacanalpanama'))  # True

def is_palindrome2(string):
    return string == string[::-1]

def is_palindrome3(string):
    stripped = string.replace(" ", "").lower()
    return stripped == stripped[::-1]