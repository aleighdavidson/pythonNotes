# we can create empty lists and tuples like this
my_list = []
my_tuple = ()
# for sets, can't use {} as it creates a dictionary
my_dict = {}
# need to use the set function
my_set = set()

# for lotto exercise
# random.sample() function could be used
# read documentation to understand whether it would give duplicates

# random.choices() method
# allows you to set different weights for the options
# wouldn't be unique numbers

# Ciara's dictionary for the calculator History function was a dict of dicts
histDict = {
    1: {'operator': '+', 'num list': [3, 4, 5, 6, 7], 'total': 28},
    2: {'operator': '/', 'num list': [3, 4, 5, 6, 7], 'total': 0.00033}
}

print(histDict[2]['operator'])
operators = []
for eq in histDict.values():
    operators.append(eq['operator'])

print(operators)


# function declaration, not actually doing anything
def print_hello():
    print("hello")


# function invocation, function call
print_hello()


def addition(num1, num2):
    print(num1+num2)


# can pass simple numbers, or expressions
# number of parameters passed needs to match number of parameters declared
addition(5, 6)
addition(4-7, 1+9)
# or can pass variables
var1 = 19
var2 = -4
addition(var1, var2)
# your function doesn't know what is going on with the rest of your code
# the scope of the function is just the function, NOT the rest of your code
# there is nothing stopping you naming the parameters inside the function the same as outside
# but remember they are not the same! even if they are named the same and have the same value
# may be confusing, but it is not a problem

# can also return result


def subtraction(num1, num2):
    return num1 - num2


# to catch the returned value, assign it to a variable
result = subtraction(5, 9)
print(result)
# or directly print it out
print(subtraction(5, 3))
# it is better to return rather than print within the function


def get_number():
    num = input("Give me a number!")
    while not num.isdecimal():
        print("That's not a number, try again!")
        num = input("Give me a number!")
    return int(num)


# first = get_number()
# second = get_number()
# print(first, second, first+second)


# once the function hits "return", it will leave
def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1/num2


# result = calculate(first, second, "+")
# print(result)

# can call functions within functions
# hold command and click on function name, it will jump you to the code where the function was declared


def change(a):
    a = 7


myVar = 8
change(myVar)  # this doesn't work to change the variable
print(myVar)


def change2(a):
    a += ['hello', 'there']


my_list = ['Martina']
change2(my_list)  # but this does work to change the list (in Python, may not in all languages)
print(my_list)

# pure functions - take values, do something, return values. DO ONE THING!
# functional programming paradigm


# can set default parameter value
# default parameters must always be on right hand side
def calculate_tax(price, tax=0.2):
    result = price * (1+tax)
    return result


book = 12
chocolate = 5
print(calculate_tax(book))  # if you don't pass the 2nd parameter, it will take the default value
print(calculate_tax(chocolate))
gin = 20
print(calculate_tax(gin, 0.3))  # if you DO pass a 2nd parameter, it takes that one instead

# when you have multiple defaults, specify which by using parameter name
# can also use names when parameters aren't default, but not generally required (positional parameters)
# to force use of parameter names, start with *, everything after the star will require name


def calculate_tax2(*, price, tax=0.2):
    result = price * (1+tax)
    return result


print(calculate_tax2(price=book))

