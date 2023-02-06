# # syntax
# # if <<condition>>:
# #   <<statements>>
#
# # my_num = int(input("Give me a number: "))
# # if my_num >5:
# #     print("You gave me a number greater than five!")
# #     print("This is part of the if statement")
# # print("This is NOT part of the if statement")
#
# # my_num = int(input("Give me a number: "))
# # if my_num >5:
# #     print("You gave me a number greater than five!")
# # else:
# #     print("Number is not greater than five!")
#
# my_input = input("Give me a number: ")
# if my_input.isdecimal():
#     my_num = float(my_input)
#     if my_num >5:
#         print("You gave me a number greater than five!")
#     else:
#         print("Number is not greater than five!")
# else:
#     print("That is not a number!")
#
# ask user to input two numbers
# input_1 = input("Enter a number:")
# if input_1.isdecimal():
#     number1 = int(input_1)
# else:
#     print("That's not a number")
#
# input_2 = input("Enter another number:")
# if input_2.isdecimal():
#     number2 = int(input_2)
# else:
#     print("That's not a number")
#
# sumOfInputs = number1 + number2
# print("Sum of previous two numbers: " + str(sumOfInputs))
#
# elif - for more than 2 options
# == check for equality with double equals
# light = "green"
# if light == 'red':
#     print("STOP!")
# elif light == "amber":
#     print("Watch out!")
# elif light == "green":
#     print("GO!")
#
# user_input = input("Type something: ")
# if user_input:
#     print(user_input.upper())
# else:
#     print("You didn't type anything!")

# can check if a value is in a list
# case sensitive, so you can convert the input to all lowercase to avoid problems
my_list = ['chocolate', 'tea', 'scones']
# if 'CHOcolaTe'.lower() in my_list:
#     print("we are good")
# else:
#     print("put chocolate on the list immediately!")
#
# # logical operators - and, or
# bus = 100
# if bus == 67 or bus == 100:
#     print("I am getting on")
# else:
#     print("I'm still waiting")

# <not> or <!> can be used to mean the opposite

# while loops
# i = 0
# while i < 7:
#     print(i)
#     i += 1

# my_input = input("Give me a number: ")
# while not my_input.isdecimal():
#     print("That is not a number!")
#     my_input = input("Give me a number: ")
#
# my_num = float(my_input)
# if my_num >5:
#     print("You gave me a number greater than five!")
# else:
#     print("Number is not greater than five!")

# for loops
# for every element in my list, do something. Refer to "every element" with the letter e
for e in my_list:
    print(e)

# loop counter variable
i = 0
# while i < 5:
#     print("hello")
#     i += 1

# can use a for loop, with a range
# range (1,6) means list [1, 2, 3, 4, 5] note: not inclusive of the end point!
for i in range(1,5):
    print("hello")
    i += 1

# continue
# if i / 2 has remainder 0, print it out, else go back to the beginning
for i in range (1, 5):
    if i % 2 == 0:
        print(i)
    else:
        continue
    print("hello")
