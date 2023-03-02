"""
1:How to import modules
2:Using random module
"""
# if u import math directly, u have to use its functions like this => math.func_name()
# if u use from math import *, u can use math functions without math.
import math
from random import randint, random, uniform

x = 25
print(math.ceil(x))

y = randint(3, 9)    # Returns an integer number between 3 and 9 (both included)
print(y)
z = random()         # Returns a random float number between 0 and 1
print(z)
a = uniform(10, 43)  # Returns a random float number between two given parameters
print(a)

# Using for loop to fill the list with 10 random numbers between 1 and 5
my_list = [randint(1, 5) for i in range(1, 10)]
print(my_list)
my_list.sort()       # Sorts the list
print(my_list)
