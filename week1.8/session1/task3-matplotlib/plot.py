
import matplotlib.pyplot as plt  # import library

x = list(range(-5,6))   # create a range for the data
y = [ k**2 for k in x ]      # create a simple function y=x^2

plt.figure()
plt.plot(x,y)  # create a 2d plot
plt.annotate(
    "x=2, y=4",
    xy =(2,4),
    xytext=(3,10),
    arrowprops= {"arrowstyle": "->"}
)
plt.title("Line plot")
plt.xlabel('x')
plt.ylabel('y=x^2')  # annotate



plt.figure()
plt.scatter(x, y)
plt.plot(x, y, "o--")
plt.title("Scatter plot") # points joined by dashed lines


plt.figure()
plt.bar(x, y)
plt.title("Scatter plot")

plt.show()  # display

# Test the example as is on the slides
# - Modify the data and the range
# - Plot in different ways
# Read matplotlib documentation
# - Test some other plotting functions
