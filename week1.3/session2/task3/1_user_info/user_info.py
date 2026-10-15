# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.
name = input("enter your name: ")
age = input("Enter ypur age:")
fav_colour = input("what is your favourite colour?")
# Open a file called 'user_info.txt' for writing

# Write each piece of information to the file, each on a new line.
with open ("user_info.txt", "w") as outfile:
    outfile.write(name +"\n")
    outfile.write(age + "\n")
    print(fav_colour, file = outfile)


# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'


#close, flush