# convention: use verbs to name functions
# e.g. get, validate, generate

# when deciding how much to include in a single function consider:
# smaller parts may make future improvements easier
# if they are too small, calling the functions uses more lines of code

# lots of different solutions - may need to justify and discuss with team

# recursive function - when a function calls itself
# equivalent to using a loop
# def get_user_choice():
#     choice = input()
#     if choice in choices_list:
#         return choice
#     else:
#         print("Wrong")
#         return get_user_choice()

# unpacking
my_tuple = (4, 5, 6)
num1, num2, num3 = my_tuple


def do_sum(a, b, c):
    return a + b + c


# can unpack tuple in function, put *tuple as parameter
print(do_sum(*my_tuple))


# variadic function, variable number of parameters
# kind of opposite of unpacking - the variable number of parameters are packed into a tuple
def do_printing(name, *stuff):
    print("Hello " + name)
    print(stuff)


do_printing("martina", "Hello", "there", "chocolate")

# * can be used in different places
# when calling function - unpack the tuple as multiple parameters
# when defining parameters, *parameter will pack into a tuple
# when defining parameters, *, parameter will force named parameters
# same for default parameters, named parameters, and variadic functions
    # it has to be the furthest right in the parameter lists


# keyword parameters, prefix parameter with ** in def
# packs the key/value pairs of the parameters that you pass the function into a dictionary
def print_vat(**kwargs):
    print(kwargs)


print_vat(vatpc=15, gross=9.55, message='Summary')


def keep_count(user, comp, status):
    if status == 'user':
        user += 1
    else:
        comp += 1
    return user, comp  # this is returning a tuple


running_total_u = 1
running_total_c = 1

result_tuple = keep_count(running_total_u, running_total_c, 'user')
running_total_u, running_total_c = result_tuple  # unpacking the tuple

# above 2 lines can be done in 1
running_total_u, running_total_c = keep_count(running_total_u, running_total_c, 'comp')

print(running_total_u)
print(running_total_c)


def double(a):
    print(a*2)

def triple(a):
    print(a*3)

# def my_fun3(f):
#     f(2)  # invoking any function that you pass into it (parameter f)


def my_fun3(f, num):
    f(num)


my_fun3(double, 7)
my_fun3(triple, 12)

# lambda functions aka anonymous function
# use keyword lambda instead of def, and remove the name
# lambda a: print(a)
# cannot call lambda functions as they have no name
# can pass it to another function, assign it to a variable

my_fun3(lambda a: print(a), 8)
my_anon_func = lambda a: print(a*4)
my_anon_func(43)

# use lambda functions if they only need to be used once so you don't pollute the code with defs
# also could have benefit of code running faster
# only useful for simple functions, like one line of code
# commonly used with map() and filter() built-in functions
# so you can map or filter more complicated rules
