# if, if-else, if-elif-else
# 1. if
# 2. if-else
# 3. if-elif-else

a = 13

if a > 10:
    print("a is greater than 10")
else:
    print("a is less than 10")

if a > 10:
    print("a is greater than 10")
elif a == 10:
    print("a is 10")
else:
    print("a is less than 10")

# Question 1
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is less than", num2)
else:
    print(num1, "is equal to", num2)

# Question 2
gender = input("Enter your gender (m/f): ")
if gender == "m" or gender == "M":
    print("Good morning Sir")
elif gender == "f" or gender == "F":
    print("Good morning Ma'am")
else:
    print("Invalid input")

# Question 3
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# Question 4
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(f'hello {name}, you are eligible to vote')
else:
    print(f'hello {name}, you are not eligible to vote')

# Question 5
year = int(input("Enter a year: "))
if year % 100 == 0 and year % 400 == 0:
    print(year, "is a leap year")
elif year % 100 != 0 and year % 4 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# Question 6
temp = int(input("Enter the temperature: "))
if temp < 0:
    print("Freezing cold weather")
elif temp >= 0 and temp < 10:
    print("Very Cold weather")
elif temp >= 10 and temp < 20:
    print("Cold weather")
elif temp >= 20 and temp < 30:
    print("Pleasant weather")
elif temp >= 30 and temp < 40:
    print("It's Hot")
else:
    print("It's Very Hot")