# Week 1.3, Session 1: Task 5a

course = "computer science"
chars = []


for ch in course:
	#print(ch)
	chars.append(ch)

print(chars)
print(sorted(chars))
#######
chars.sort()
print(chars)

#print(list(course))
# create a list data structure of the characters from the course string
# sort the list into alphabetical order
chars = list(course)
print(chars)