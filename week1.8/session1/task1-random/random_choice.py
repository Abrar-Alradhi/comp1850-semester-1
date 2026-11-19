import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
how_many = int(input("Enter the number of names?"))
choices = random.sample(names, how_many)
for choice in choices:
    print(choice)

# Display the chosen names, one per line
