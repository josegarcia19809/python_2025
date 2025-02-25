"""
frequency
Write a function called frequency. This function accepts a list and a search_term
(this will always be a primitive value) and returns the number of times the
search_term appears in the list.


'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

def frequency():
    pass

"""


def frequency(lista, search_term):
    count = 0
    for item in lista:
        if item == search_term:
            count += 1

    return count


print(frequency([1, 2, 3, 4, 4, 4], 4))  # 3
print(frequency([True, False, True, True], False))  # 1


def frequency2(collection, search_term):
    return collection.count(search_term)
