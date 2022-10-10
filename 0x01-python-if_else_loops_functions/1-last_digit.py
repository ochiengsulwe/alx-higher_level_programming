#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# get the string representation of number
num = repr(number)

# access the last string of the digit string
ld_str = num[-1]

# convert the last digit string back to integer

ld = int(ld_str)

if ld > 5:
    print(f"Last digit of {number} is {ld} and is greater than 5")

elif ld == 0:
    print(f"Last digit of {number} is {ld} and is 0")

else:
    print(f"Last digit of {number} is {ld} and is less than 6 and not 0")
