"""Advanced Task 2: Budget Breakdown
- Ask for three separate expense amounts (for example: travel, food, accommodation).
- Convert each input so you can add them together to get a total trip cost.
- Calculate the average spend per category and show each value with an f-string.
- Extension: format the totals so they always show two decimal places.
"""

travel_cost_input = input("Travel cost in pounds: ")
food_cost_input = input("Food cost in pounds: ")
accommodation_cost_input = input("Accommodation cost in pounds: ")

travel_cost = int(travel_cost_input)
food_cost = int(food_cost_input)
accommodation_cost = int(accommodation_cost_input)

total_spent = travel_cost + food_cost + accommodation_cost
average_spent = total_spent / 3
print(f"The travel cost is {travel_cost:.2f}, and the food cost is {food_cost:.2f}, the accomodation cost is {accommodation_cost:.2f} ")
print(f"The total spent is {total_spent:.2f}")
print(f"The average spent is {average_spent:.2f} per category")

# TODO: convert each value to a number type that supports decimals
# TODO: calculate the total and the average spend per category
# TODO: print the three costs, the total, and the average
# Extension: format the totals to two decimal places
