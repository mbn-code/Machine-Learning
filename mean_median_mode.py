# The Mean, Median, and Mode are techniques that are often used in Machine Learning, so it is important to understand the concept behind them.

import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
speed

# Printing out the mean of the speed array. The mean basically meaning the averaage value of the list.
speed_mean = numpy.mean(speed)

print(speed_mean)


# Getting and priting the median of the speed array
# If there are 2 numbers in the middle, devide te two numbers sum by 2 and youll get your result
# This is just basic math

median = numpy.median(speed)

print(median)


# Getting and printing mode (the value which accurs the most in the array), this doesn't use numpy this uses stats from scipy 

mode = stats.mode(speed)

print(mode)

# This bothy returns the number which accurs the most and the amount of times it does.
