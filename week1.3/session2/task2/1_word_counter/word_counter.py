# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

# open and read the file
file_name = input("Enter file name: ")

with open(file_name, "r") as infile:
    content = infile.read()
words = content.split(" ")
print(len(words))
print(words)
# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

# display the wordcount

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210
#file_name = input("Enter file name: ")

#with open(file_name, "r") as infile:
    #for line in infile:
      #  print(line)
        #print(file_name.count(line))
        