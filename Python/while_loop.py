a = 1
while a <= 30:      # runs till condition is true
    print(a)
    a = a + 1

# Question 1
n = int(input("Enter a number: "))
while n > 0:
    print(n % 10)
    n = n // 10

# Question 2
n = int(input("Enter a number: "))
r = 0
while n > 0:
    r = r * 10 + n % 10
    n = n // 10
print(r)

# Question 3
n = int(input("Enter a number: "))
copy = n
r = 0

while n > 0:
    r = r * 10 + n % 10
    n = n // 10

if r == copy:
    print("Palindrome")
else:
    print("Not a palindrome")

# Question 4
import random
num = random.randint(1, 10)
guess = int(input("Guess a number (1-10): "))
tries = 0
while True:
    if guess == num:
        tries += 1
        print("You guessed it in", tries, "tries")
        break
    elif guess > num:
        print("Too high")
    else:
        print("Too low")
    guess = int(input("Guess again: "))
    tries += 1