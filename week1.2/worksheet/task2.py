# Worksheet 1.2: Task 2 Solution
# Name: Abrar Alradhi, 202014910

import sys
from util import read_numbers
numbers = read_numbers()

def read_numbers():
    line = input("Enter some numbers, separated by spaces: ")
    numbers = [float(item) for item in line.split()]
    return numbers
if len(numbers) == 0:
    sys.exit("Error: no numbers provided")

maximum_number = max(numbers)
minimum_number = min(numbers)
mean = sum(numbers) / len(numbers)

numbers.sort()
n = len(numbers)

middle = n // 2

if n % 2 != 0:
    median = numbers[middle]
else:
    median = (numbers[middle - 1] + numbers[middle] ) / 2

print(f"Minimum = {minimum_number}")
print(f"Maximum = {maximum_number}")
print(f"Mean = {mean}")
print(f"Median = {median}")