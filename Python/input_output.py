# Output
print("Hello World")

name = "Rohan"
age = 19

print("My name is", name)
print("My age is", age)

print(name, age)

# formatted string (f-string)
print(f"My name is {name} and my age is {age}")

# Raw string (not escape characters, like \n)
print(r"Hello\nWorld")

# Input
age = input("Enter your age: ") # input is always a string, convert to int if needed
print("Your age is", age)
print(type(age))

age = int(input("Enter your age: "))
print("Your age is", age)
print(type(age))