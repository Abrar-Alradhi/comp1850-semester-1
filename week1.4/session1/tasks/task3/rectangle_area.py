
# function implementation

def rectangle_area(width, height):  # define suitable input data
     """ Calculate the area of a rectangle"""        
    area = width * height # implement the function
    return area              # return an appropriate value

# testing the function

print(f"Area is {rectangle_area(2,4)}")   # provide suitable data matching your inputs
# return width * height

#find the even values up to some limit
def even_numbers(limit):
    evens = []
    for n in range(limit +1):
        if n % 2 == 0:
            evens.append(n)
    return evens

print(even_numbers(20))

# other ay to do in a shorter way
def even_numbers(limit):
    return [ n for n in range(limit + 1) if n % 2 == 0]

print(even_numbers(20))