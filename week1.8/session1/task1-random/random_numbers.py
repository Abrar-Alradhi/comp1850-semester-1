import random

# Get user to input how many random numbers they want
how_many = int(input("Enter the number of random numbers: "))
# Generate this many random numbers

# Write the random numbers to a file named random.txt, one number per line
# Generate and write this many random integers, one number per line
with open("random.txt", "w") as outfile:
    for _ in range(how_many):
        num = random.randint(1, 100)
        outfile.write(str(num) + "\n" )

