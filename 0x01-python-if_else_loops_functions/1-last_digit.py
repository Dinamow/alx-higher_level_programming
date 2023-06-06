#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = number % -10
else:
    digit = number % 10
print(f"Last digit of {number:d} is {digit:d} and", end=' ')
if digit == 0:
    print("is 0")
elif digit > 5:
    print("is greater than 5")
else:
    print("is less than 6 and not 0")
