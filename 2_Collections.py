# list - mutable ordered collection, positions start at 0
my_list = [1, 2, 3, 4]
print(my_list)
print(my_list[2])
my_list[2] = -4
print(my_list)
my_list.append(9)
print(my_list)

# lists can be heterogeneous
my_list_2 = [1, 'Martina', [2, 4, 5]]
print(type(my_list_2))
print(my_list_2[2][1])
print(len(my_list_2))

# tuple - immutable ordered collection, positions start at 0
my_tuple = (1, 2, 3)
print(type(my_tuple))
print(my_tuple[1])
# immutable so my_tuple[1] = -9 will throw up an error
# immutable so my_tuple.append(9) will throw up an error

# set - mutable, unordered, UNIQUE elements
my_set = {1, 2, 3}
print(type(my_set))
my_set.add(7)
print(my_set)
my_set.add(1)
print(my_set)
# UNORDERED so my_set[1] won't work

# dictionaries - key/value pairs, unordered
my_dict = {'first_name': 'Martina', 'last_name': 'Yusef', 'address': 'Brighton'}
print(my_dict['first_name'])
#can be mix of types
my_dict_2 = {'first_name': 'Alex', 'list': [1, 2, 3], 3: 4.5}
print(my_dict_2['list'][1])
print(my_dict_2[3])
