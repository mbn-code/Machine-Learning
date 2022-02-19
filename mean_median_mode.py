# The Mean, Median, and Mode are techniques that are often used in Machine Learning, so it is important to understand the concept behind them.

import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
speed

# Printing out the mean of the speed array. The mean basically meaning the average value of the list.
speed_mean = numpy.mean(speed)

print(speed_mean)


# Getting and printing the median of the speed array
# If there are 2 numbers in the middle, divide the two numbers sum by 2 and you'll get your result
# This is just basic math

median = numpy.median(speed)

print(median)


# Getting and printing mode (the value which accurse the most in the array), this doesn't use numpy this uses stats from scipy 

mode = stats.mode(speed)

print(mode)

# This bothy returns the number which accurse the most and the amount of times it does.
