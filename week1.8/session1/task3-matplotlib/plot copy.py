
import matplotlib.pyplot as plt  # import library

x = list(range(-5,6))   # create a range for the data
y = [ k*k for k in x ]      # create a simple function y=x^2

fig, axes = plt.subplots(2,1)
axes[0].plot(x,y)  # create a 2d plot
axes[0].set_title("Line plot")
plt.xlabel('x')
plt.ylabel('y=x^2')  # annotate

axes[1].plot(x,y)
plt.scatter(x, y)
axes[1].set_title("Scatter plot")

plt.tight_layout()
plt.show()  # display

# Test the example as is on the slides
# - Modify the data and the range
# - Plot in different ways
# Read matplotlib documentation
# - Test some other plotting functions
