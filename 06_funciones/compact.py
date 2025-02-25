"""
compact
Write a function called compact. This function accepts a list and returns a list of
values that are truthy values, without any of the falsey values.
1.	compact([0,1,2,"",[], False, {}, None, "All done"])     # [1,2, "All done"]


'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

def compact():
    pass

"""

def compact(lista):
    new_list = []
    for elemento in lista:
        if elemento:
            new_list.append(elemento)

    return new_list

print(compact([0,1,2,"",[], False, {}, None, "All done"]))

def compact2(l):
    return [val for val in l if val]