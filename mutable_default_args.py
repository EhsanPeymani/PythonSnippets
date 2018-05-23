# from talkpython


# default args are evaluated only once at the time of definition
# in this case, lst is shared between all calls to this function
def add_items_bad(item, lst=[]):
    lst.append(item)
    return lst


def add_items_good(item, lst=None):
    if lst is None:
        lst = []

    lst.append(item)
    return lst


list_1 = add_items_bad('a')
add_items_bad('b', list_1)
add_items_bad('c', list_1)
list_2 = add_items_bad('d')

print('list_1:', list_1)
print('list_2:', list_2)
print('list_1 == list_2:', id(list_1)==id(list_2))

print('\n\n')

list_3 = add_items_good('x')
add_items_good('xx', list_3)
add_items_good('yy', list_3)
list_4 = add_items_good('Q')

print('list_3:', list_3)
print('list_4:', list_4)
print('list_3 == list_4:', id(list_3)==id(list_4))