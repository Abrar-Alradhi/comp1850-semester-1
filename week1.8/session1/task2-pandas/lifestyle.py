import pandas

data = pandas.read_csv("lifestyle_data.csv")

# What data type is `data` as output from the `read_csv()` method?
print(type(data))  # This will print the type of the `data` variable, which is a pandas DataFrame.
# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students
total_students = data.shape[0]
print(f"Total number of students: {total_students}")

# Find the mean average GPA of the students
mean_gpa = data["GPA"].mean()
print(f"Mean average GPA: {mean_gpa}")

# Find the standard deviation of how much sleep students get per day
sleep_std = data["Sleep_Hours_Per_Day"].std()
print(f"Standard deviation of sleep hours: {sleep_std}")

# Find the maximum amount of study hours per day
max_study_hours = data["Study_Hours_Per_Day"].max()
print(f"Maximum study hours per day: {max_study_hours}")

# Sort the students by social hours per day ascending (lowest -> highest)
data_sorted = data.sort_values("Social_Hours_Per_Day", ascending=True)

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one
data["Total_hours"] = data[["Sleep_Hours_Per_Day", "Study_Hours_Per_Day", "Social_Hours_Per_Day"]].sum(axis=1)

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
# Can you work out whether having a higher stress level leads to a higher GPA?
high_stress_students = data[data["Stress_Level"] == "high"]
low_stress_students = data[data["Stress_Level"] == "low"]

print(f"Number of students with high stress level: {len(high_stress_students)}")
print(f"Number of students with low stress level: {len(low_stress_students)}")

# Calculate the mean GPA for each group
mean_gpa_high_stress = high_stress_students["GPA"].mean()
mean_gpa_low_stress = low_stress_students["GPA"].mean()

print(f"Mean GPA for students with high stress level: {mean_gpa_high_stress}")
print(f"Mean GPA for students with low stress level: {mean_gpa_low_stress}")
