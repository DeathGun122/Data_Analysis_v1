print("Hello World")    # 5 times
print("Hello World")    # 5 times
print("Hello World")    # 5 times
print("Hello World")    # 5 times
print("Hello World")    # 5 times

for i in range(5):      # 5 times
    print("Hello World")

# range function    => [start, stop, step]
range(5)    # [0, 1, 2, 3, 4]
range(1, 6) # [1, 2, 3, 4, 5]
range(1, 6, 2) # [1, 3, 5]

a = range(1,20,1)

for i in a:     # in is a keyword
    print(i)

# default start = 0, step = 1

# reverse
for i in range(20,51,1):    # 20 to 50
    print(i)

for i in range(16,0,-1):   # 16 to 1
    print(i)

for i in range(-3, -16, -1):   # 20 to 1
    print(i)

# table of 5
for i in range(1,11):
    print(f'5 x {i} = {i*5}')

# any table 
# n = int(input("Enter required table: "))
# for i in range(1,11):
#     print(f'{n} x {i} = {n*i}')

# Loops for strings

a = "Rohan"
for i in range(len(a)):     # method with range
    print(a[i])

for i in a:                 # method with characters
    print(i)

# break, continue, else
for i in range(1,11):
    if i == 5:
        break
    print(i)

for i in range(1,11):
    if i == 5:
        continue
    print(i)

for i in range(1,11):
    if i == 5:
        break
    print(i)
else:   # else is optional, executed if break is not executed
    print("Loop completed")

# pass
for i in range(1,11):
    pass

# Question 1
n = int(input("Enter no. of prints: "))
for i in range(n):
    print("Hello World")

# Question 2
n = int(input("Enter a number: "))
for i in range(n+1):
    print(i)

# Question 3
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(i)

# Question 4
n = int(input("Enter required table: "))
for i in range(1,11):
    print(f'{n} x {i} = {n*i}')


# Question 5
sum = 0
n = int(input("Enter a number: "))
for i in range(1, n+1):
    sum += i
print(sum)

# Question 6
fact = 1
n = int(input("Enter a number: "))
for i in range(1, n+1):
    fact *= i
print(fact)

# Question 7
l = int(input("Enter lower limit: "))
u = int(input("Enter upper limit: "))
evens = 0
odds = 0
for i in range(l, u+1):
    if i % 2 == 0:
        evens += 1
    else:
        odds += 1
print(f'No. of evens: {evens}')
print(f'No. of odds: {odds}')

# Question 8
n = int(input("Enter a number: "))
for i in range(1, n+1):
    if n % i == 0:
        print(i)

# Question 9
n = int(input("Enter a number: "))
sum_fact = 0
for i in range(1, n+1):
    if n % i == 0:
        sum_fact += i
if sum_fact == n:
    print(f'{n} is a perfect number')
else:
    print(f'{n} is not a perfect number')

# Question 10
n = int(input("Enter a number: "))
count = 0
for i in range(2, n):
    if n % i == 0:
        count += 1
if count == 0:
    print(f'{n} is a prime number')
else:
    print(f'{n} is not a prime number')

# Question 11
str = input("Enter a string: ")
str2 = ""
for i in range(len(str)-1, -1, -1):
    str2 += str[i]
print(str2)

# Question 12
str = input("Enter a string: ")
new_str = ""
for i in range(len(str)-1, -1, -1):
    new_str += str[i]
if str == new_str:
    print(f'{str} is a palindrome')
else:
    print(f'{str} is not a palindrome')

# Question 13
str = input("Enter a string: ")
char = 0
num = 0
spchar = 0
for i in str:
    if i.isdigit():
        num += 1
    elif i.isalpha():
        char += 1
    else:
        spchar += 1
print(f'No. of characters: {char}')
print(f'No. of numbers: {num}')
print(f'No. of special characters: {spchar}')