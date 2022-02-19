# Scatter plot is a diagram wee each value in the data set is presented b a dot instead of boxes etc.

from platform import platform
import matplotlib.pyplot as plt

age = [5,7,8,7,2,17,2,9,4,11,12,9,6]

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# The scatter uses x and y axis as in a coordinate system.
# Thus making age = x speed = y
plt.scatter(age, speed)
plt.show()
# When we run we can see that the cars which are 2 year old are the fastest, and the 12 year old one is the slowest.


# When we close the window above with the "controlled" values, we see this next window. 
import numpy

# Using the technique from Data_Distribution_part1.py
# Because we are using the value 5 as the mean on the x axis, the numbers will be concentrated around that area on the x axis
x = numpy.random.normal(5.0, 1.0, 1000)
# And we use the mean 0 here, which means that they will be centralized around the 10 on the y axis
y = numpy.random.normal(10.0,2.0,1000) 

# Now scatter the x and y values, which could be anything in this case, and show it. 
plt.scatter(x,y)
plt.show()

# Also the spread is wider ont he y axis then on the x.