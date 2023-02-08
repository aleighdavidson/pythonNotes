# range(start, stop, stepSize*) *optional (default step size 1)
# start, start+1, start+2, ..., stop-1
# for i in range(0, 3):
#     print(i)
#
# for i in range(0, 21, 5):
#     print(i)
# import emoji

# variables start with lower case
# starting with a capital indicates that it is a class (e.g. String)
# also name projects/folders with lowercase

# loops in Python can have an else stateuemtn
# for i in range(0, 3):
#     print(i)
# else:
#     # only run when the loop is exhausted (it stops naturally)
#     print("I'm done!")

# conditional expression can be used as shortcut
# a = int(input("Give me a number: "))
# b = int(input("Give me another number: "))
# maxNum = 0
# if a > b:
#     maxNum = a
# else:
#     maxNum = b
# print(maxNum)
# equivalent conditional expression gets it done in 1 line
# maxNum = a if a > b else b

# String Handling
# \Unnnn (two-byte unicode character) \Unnnnnnnn (four-byte) or \N{name}
print("\U0001F600")
print("\N{winking face}")

# pip install emoji (type in terminal, will install the module for emoji handling)
# print(emoji.emojize(robot))   # didn't work

# the print function automatically concatenates comma-separated values
# optional arguments sep and end
# default sep = " ", default end = "\n" (new line)
# can change the separator and end character

print("Alex", "Davidson")
#print("Alex", "Davidson", sep=*: end=!!)

# quotes can be single or double, just stick to one
# if you need to print a special character within a string, precede with backslash
lastName = "O'Neill"
lastName1 = 'O\'Neil'

# long strings, can include \n and \t within to have new lines and tabs
# rawString, precede with r\ to stop python from interpreting special characters and print exactly as it is
# strings are immutable
# when concatenating strings, you are creating a new string
# bad idea to concatenate in a loop, use join() function instead

# can replace words in string, but it is creating a new string
myStr = "I like chocolate more than cheese."
newStr = myStr.replace("cheese", "wine")
print(myStr)
print(newStr)

# can search for something in a string
print(myStr.find("cheese"))
# returns the position of the first character in the string
# if you search for something that doesn't exist, it returns -1
print(myStr.find("tooth"))
# can do something similar with the in operator
if "cheese" in myStr:
    print("Yes, cheese is there")

# f string, interpolated string
# this is a way to concatenate strings/integers without changing types
# precede the string with f" ", then anything in {} will be interpreted
# (i.e. will print value of the variable a rather than the character "a")

a = 5
b = 3
result = f"{a} + {b} = {a+b}"
print(result)

# string slicing
# can print a portion of a string (starts counting at position 0, 9 not included)
print(myStr[2:9])
# doesn't work backwards like this
print(myStr[9:2])
# but can count from the end as well (starting at -1)
print(myStr[-4:-1])
# could use it to cut off a final character for example
myUrl = "localhost:8080/hello/"
print(myUrl[0:-1])
# if you don't include the end positions it will include the final
print(myUrl[:-1])
# can create a copy using a slice
myUrlCopy = myUrl[:]

# string.split() creates a list out of a string, default delimiter is " "
my_list = myStr.split()
print(my_list)
# can include a specific delimiter
my_list2 = myUrl.split("/")
print(my_list2)

# can also create a string out of a list with join()
myList = ["wine", "cheese", "biscuits", "cat food"]
# <"delimiter">.join(<list>)
myListStr = "*".join(myList)
print(myListStr)