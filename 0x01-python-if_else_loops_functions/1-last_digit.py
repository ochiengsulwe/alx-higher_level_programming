#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Get the string representation
num_str = repr(number)

# Access the last string of the digit string
ld_str = num_str[-1]

# Convert the last digit string to an integer
ld = int(ld_str)

#ld = number % 10

if number >= 0 and ld > 5:
    print(f"Last digit of {number} is {ld} and is greater than 5")

elif ld == 0:
    print(f"Last digit of {number} is {ld} and is 0")

else:
    print(f"Last digit of {number} is {ld} and is less than 6 and not 0")
