"""
last_element
Write a function called last_element. This function takes in one parameter (a list)
and returns the last value in the list. It should return None if the list is empty.

'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element():
    pass

"""


def last_element(my_list: list[int]) -> int or None:
    if not my_list:
        return None
    else:
        return my_list[-1]


print(last_element([1, 2, 3]))
print(last_element([21, 42, 53]))
print(last_element([]))  # None)


# First check to see if the list exists (if it has data in it).  If it does, return
# the -1 item (last item).  Otherwise, return None.

def last_element2(l):
    if l:
        return l[-1]
    return None
