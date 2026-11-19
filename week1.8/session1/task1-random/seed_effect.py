# See README.md for instructions on what to do this program

import random

#random.seed(10)

#The randint(start,stop) method returns an integer number selected from the specified range.
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print(num1, num2, num3)
print(random.getrandbits(4))
#The code produces the exact same sequence of "random" numbers every time it runs.
random.seed(10)
print(random.randint(1, 100)) 

print(random.randint(1, 100)) 
