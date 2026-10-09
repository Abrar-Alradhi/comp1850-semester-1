# Worksheet 1.2: Task 1 Solution
#Name: Abrar Alradhi, 202014910
import sys

grade_input = input("Enter your grade: ")

if not grade_input.isdecimal():
    sys.exit("Error:Grade must be an integer between 0 and 100")

grade = int(grade_input)

if 100 < grade < 0:
    sys.exit("Error:Grade must be an integer between 0 and 100")

if 0 < grade < 39:
    print(f"{grade} is a Fail")
elif 40 < grade < 69:
    print(f"{grade} is a Pass")
else:
    print(f"{grade} is a Distinction")

    