# can use the map function to convert string list to integer list
# the map function is applying the function int() to every element in the collection
string = "1, 2, 3, 4, 5"
strList = string.split(",")
# print(string)
# print(strList)
# intList = list(map(int, strList))
# print(intList)

map(int, strList)
# can be written as
for el in strList:
    int(el)
print(strList)
# but it isn't captured anywhere - doesn't change original list, doesn't create new list
# list() is capturing the output of the map() function

# here's another application
shopList = ['milk', 'bread', 'lipstick']
lenList = list(map(len, shopList))
print(lenList)

# strings are immutable, like tuples
my_str = "Martina"
print(my_str)
print(my_str[4])
new_str = my_str.replace("i", "x")
print(my_str)
print(new_str)

# four functions that apply to many collections
# min, max, len, sum
# myNumList = [3, 6, 9, 2, 3]
# print(myNumList)
# print(max(myNumList))
# print(min(myNumList))
# print(len(myNumList))
# print(sum(myNumList))

# what if you include a string? it doesn't work
# myNumList = [3, 6, 9, 2, "string"]
# print(myNumList)
# print(max(myNumList))
# print(min(myNumList))
# print(len(myNumList))
# print(sum(myNumList))

# what if the list is all strings?
myNumList = ["elisa", "alex", "martina", "ian"]
print(myNumList)
print(max(myNumList))
print(min(myNumList))
print(len(myNumList))
# print(sum(myNumList))
# where is the min coming from??

# tuples indicated by regular round brackets
# myTuple = (5, 7, 2)
# tuple with a single element, follow it by a comma
# myTupleOne = (5,)
# the brackets aren't actually required!
myTuple = 5, 7, 2
myTupleOne = 5,
print(type(myTuple))
# except if you need an empty tuple, then use empty brackets
emptyTuple = ()
print(type(emptyTuple))

# can assign multiple variables at once
# "unpacking a tuple"
# a, b, c = myTuple
# print(a, b, c)
# can also go the other way
a, b, c = myTuple
a, b, c = 5, 7, 2
print(myTuple)
# need to have the same number of variables as there are elements in the tuple
# otherwise there will be an error because it is expecting something else

# swapping values
d = 6
e = 9
# to swap, you would need an empty variably
f = d
d = e
e = f
# Python specific way to swap
d, e = (e, d)
# first it creates the tuple (e, d) which is (9, 6)
# then it unpacks the new tuple to the variables d, e
# now d = 9 and e = 6
# again, don't actually need the brackets
d, e = e, d

# indexing from the right-hand side uses negative numbers
my_list = ['milk', 'bread', 'chocolate', 'cheese', 'onions']
print(my_list[-1])
# slicing
print(my_list[2:4])
# will print positions 2 and 3 (not inclusive of the stop value)

# when un-packing, can include * to account for extra elements
a, *b, c = my_list
print(a)
print(b)
print(c)
# idea: take end ends off a list again and again?

# adding to lists
# "prepend" - add to beginning
# it is creating an empty slice at the beginning and assigning this new list in there
my_list[:0] = ['shoes', 'tea']
print(my_list)
# alternative to append
# my_list += ['dog food', 'fish']
# my_list.extend(['dog food', 'fish'])
# append can only be used for a single item
# my_list.append('beans', 'cereal') will produce a TypeError
# my_list.append(['beans', 'cereal']) will append the string "['beans', 'cereal']" to the end as a single item
print(my_list)
# insert, adds item to that position
my_list.insert(3, 'rice')
print(my_list)
# can you also insert by slicing?
# this actually replaced bread which was on position 4
# my_list[4:5] = ['tofu']
# this one worked, with the same start and end position in the slice
my_list[4:4] = ["tofu"]
print(my_list)

# removing items
# the method pop will remove the last item by default (LIFO)
# can retrieve the removed element by assigning to a variable
last_elem = my_list.pop()
print(my_list)
print(last_elem)
# or you can specify position
my_list.pop(5)
print(my_list)
# also the method del, but the removed element is not retrievable
# remove method can remove a matching value (the first occurrence from the left)
my_list.remove("chocolate")
print(my_list)
# will raise an error if you try to remove something that doesn't exist

# sorting
# all collections have built-in sort functions
# sorted() returns a sorted list (assign to new variable)
# list.sort() sorts the list in place
# optional parameter of sort key
nums = ['1001', '34', '3', '77', '42', '9', '87']
# these numbers are strings so they will go alphabetically by default
sortNums = sorted(nums)
print(sortNums)
# add the sort key to treat them as numbers
sortNums = sorted(nums, key=int)
print(sortNums)

# sets are mutable but only contain unique values and are unordered
my_set = {4, 7, 2, 4, 7, 2, 5, 6, 8}
# when you print, it will reject duplicates
print(my_set)
# can add/remove, no append/insert as there are no positions so it doesn't matter
my_set.add(12)
my_set.add(1)
print(my_set)
# remove and discard seem to do the same...
my_set.remove(7)
print(my_set)
my_set.discard(2)
print(my_set)
# pop removes the "next" item in the list
my_set.pop()
print(my_set)

# can change lists to sets and back using list() and set() functions
# e.g. to remove duplicates from a list
cheese = ['cheddar', 'leicester', 'brie', 'cheddar', 'stilton', 'stilton']
print(cheese)
uniqueCheese = list(set(cheese))
print(uniqueCheese)

# set operations
# set1.union(set2), represented by |, returns every value in both sets
# set1.intersection(set2), represented by &, returns items that appear in both sets
# set1.difference(set2), represented by -, returns items in the first set that aren't in the 2nd
# set1.symmetric_difference(set2), represented by ^, returns items in one set only (either set)

# dictionaries, not ordered
# keys need to be unique
# dict.keys method, returns keys as a set (since there is no order)
# dict.items returns the key-value pairs as a tuple
