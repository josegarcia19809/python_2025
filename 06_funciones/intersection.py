"""
intersection
Write a function called intersection. This function should accept two lists and return
a list with the values that are in both input lists.
1.	intersection([1,2,3], [2,3,4])    #[2,3]
2.	intersection(['a','b','z'], ['x','y','z']) .  # ['z']


# flesh out intersection pleaseeeee
def intersection():
    pass

"""


def intersection(lista_1, lista_2):
    lista_3 = []
    for elemento in lista_1:
        if elemento in lista_2:
            lista_3.append(elemento)

    return lista_3


print(intersection([1, 2, 3], [2, 3, 4]))
print(intersection(['a', 'b', 'z'], ['x', 'y', 'z']))


def intersection2(l1, l2):
    return [val for val in l1 if val in l2]

def intersection3(list1, list2):
    return [val for val in set(list1) & set(list2)]