"""
partition
Write a function called partition. This function accepts a list and a callback function
(which you can assume returns True  or False  ).
The function should iterate over each element in the list and invoke the callback
function at each iteration.
•	If the result of the callback function is True , the element should go into the
first list (i.e. the "truthy" list).
•	If the result of the callback function is False , the element should go into the
second list (i.e. the "falsy" list).
When it's finished, partition should return both lists inside of one larger list, like so:
[truthy_list, falsy_list]
'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''

def partition():
    pass

"""


def is_even(num):
    return num % 2 == 0


def partition(lista, callback):
    lista_1 = []
    lista_2 = []
    for num in lista:
        if callback(num):
            lista_1.append(num)
        else:
            lista_2.append(num)
    return [lista_1, lista_2]


print(partition([1,2,3,4], is_even))

def partition2(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]

def partition3(l, callback):
    return [[l.pop(l.index(i)) for i in l[:] if callback(i)], l]