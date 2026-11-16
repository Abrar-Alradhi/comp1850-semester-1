import random

# Get user to input how many random numbers they want
how_many = int(input("Enter the number of random numbers"))
# Generate this many random numbers

# Write the random numbers to a file named random.txt, one number per line
with open("names.txt") as infile:
    names = [line.strip() for line in infile ]

print(names)