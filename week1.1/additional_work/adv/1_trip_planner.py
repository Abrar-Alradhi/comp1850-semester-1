"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""
import sys
destination = input("Where are you going to? ")

distance_miles_input = input("How many miles will you travel? ")
time_hours_input = input("How many hours will the journey take? ")

try:
    distance_miles = int(distance_miles_input)
    time_hours = int(time_hours_input)
    if (distance_miles <= 0) or (time_hours <= 0):
        print("please enter a valid number")
    else:
        distance_miles = int(distance_miles_input)
        time_hours = int (time_hours_input)
        speed = distance_miles / time_hours
        print(f"You are going to {destination} with a speed of {speed:.2f} miles/hour")
except:
    print("Please enter numbers only")




# TODO: convert distance_miles_input and time_hours_input to numbers
# TODO: calculate the average speed in miles per hour
# TODO: print a summary message using an f-string
# Extension: add validation for zero or negative values
