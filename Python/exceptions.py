# Errors => Memory Errors, Logical Errors, Syntax Errors

# print(1/0)          ZeroDivisionError
# if True:
#     print("True")
# else:
#     print("False")  # IndentationError

# print(a)            NameError

# Tab error, IndentationError, SyntaxError => Types of errors

# Exceptions
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
# print(a/b)          # ZeroDivisionError
# print(a//b)         # ZeroDivisionError

# Exception handling with if-else
if b == 0:
    print("Cannot divide by zero")
else:
    print(a/b)

# keyword => try, except, else, finally, raise

# try and except
try:
    print(a/b)
except ZeroDivisionError:           # ZeroDivisionError is a class
    print("Cannot divide by zero")

try:
    print(a/b)
except Exception as err:              # Exception is a class
    print(err)

# Types of exceptions
# 1. Built-in exceptions eg: ZeroDivisionError, NameError
# 2. User-defined exceptions => custom exceptions eg: ValueError

# else keyword
try:
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:                                   # Executed if try block is successful and no exception is raised
    print("Division successful")

# finally keyword
try:
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:                                   # Executed if try block is successful and no exception is raised
    print("Division successful")
finally:                                # Executed always
    print("Finally block is always executed")

# raise keyword
age = int(input("Enter your age: "))

# if age < 10 or age > 18:
#     raise ValueError("Age should be between 10 and 18")         # ValueError is a class
# else:
#     print("Age is valid")

# print("The end")

# raise in try-except block
try:
    age = int(input("Enter your age: "))
    if age < 10 or age > 18:
        raise ValueError("Age should be between 10 and 18")
    else:
        print("Age is valid")
except ValueError as err:
    print(err)

print("The end")