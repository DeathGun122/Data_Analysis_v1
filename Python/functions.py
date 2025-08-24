print("Hello World")        # inbult function
print(len("Hello World"))   # inbuilt function

# User defined function (Block of code which is written to perform a specific task and can be called multiple times)
def hello():                # function definition
    print("Hello World")        # function body

hello()     # function call

# Parameters and Arguments

# Positional arguments
def sum(a, b):              # passing arguments
    print(f'Sum of {a} and {b} is {a + b}')

sum(10, 20)                 # function call
sum(20, 30)                 # function call with different arguments

# Keyword arguments
def sum(a, b):              # passing arguments
    print(f'Sum of {a} and {b} is {a + b}')

sum(b=10, a=20)                 # function call with keyword arguments, can be passed in any order

# Default arguments
def sum(a, b=10):              # passing arguments
    print(f'Sum of {a} and {b} is {a + b}')

sum(10)                         # function call with 1 argument
sum(10, 20)                     # function call with 2 arguments

# Question
def palindrome(str):
    new_str = ""
    for i in range(len(str)-1, -1, -1):
        new_str += str[i]
    if str == new_str:
        print(f'{str} is a palindrome')
    else:
        print(f'{str} is not a palindrome')

str = input("Enter a string: ")
palindrome(str)

# return statement
def sum(a, b):
    return a + b

print(sum(10, 20))