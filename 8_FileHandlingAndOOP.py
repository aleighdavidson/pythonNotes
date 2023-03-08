# file = open("testFile.txt", 'r')
#
# # .readlines() returns a list, line by line, with the line breaks \n
# lineList = file.readlines()
# print(lineList)
#
# # .splitlines() returns a list, line by line, with NO line breaks
# splitList = file.splitlines()
# print(splitList)
#
# # .read() returns lines as they are in the file
# readFile = file.read()
# print(readFile)
#
# # if files are really big, you wouldn't want a huge list
# # can loop through the lines
# # for line in file:
# #     print(line, end="")
# #
# # # safer way using with
# # with open("testFile.txt", "r") as file:
# #     for line in file:
# #         print(line, end="")
#
# f = open("testFile.txt", "w")
# char_write = f.write("Hello\n")
# # returns # of characters
# # (didn't need to capture the function call in a variable here, just did to see the return)
# print(char_write)
# list1 = ['apples\n', 'bananas\n', "oranges\n"]
# list_write = f.writelines(list1)
# # doesn't return anything
# print(list_write)  # prints None

from oopCat import Cat
from oopDog import Dog
# instantiating a class, creating an instance = object
catObj = Cat("Bentley", "black & white")
# need to do <object>.<method>()
# NOTE <class>.<method>()
catObj.purr()
catObj.hunt("mouse")
print(catObj.get_name())
catObj.set_height(45)

dogObj = Dog("Fletcher")
dogObj.bark()
