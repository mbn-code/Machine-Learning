# The Standard Deviation and Variance are terms that are often used in Machine Learning, so it is important to understand how to get them, and the concept behind them.

import numpy

# Using an array which doesn't have a wide arrange of car speeds

speed_1 = [86,87,88,86,87,85,86]

# And here using an array which has a wider range of speeds
speed_2 = [32,111,138,28,59,77,97]

deviation_1 = numpy.std(speed_1)
deviation_2 = numpy.std(speed_2)

print("------------ Deviation ------------")
print(deviation_1)
print(deviation_2)

# Findingn the mean without moduel

# Get the mean
Variance_raw_num = (32+111+138+28+59+77+97) / 7

# Get the mean with numpy
mean_spd2 = numpy.mean(speed_2)
print("------------ Mean ------------")
print(Variance_raw_num)
print(Variance_raw_num)

Variance_array = [32,111,138,28,59,77,97]

print("------------ Difference spd2 ---------------")
for dif in Variance_array:
    # Get the differnce between two numbers
    difference_spd2 = (dif - Variance_raw_num)

    # Print out "difference for {difference_spd2}" so the user knows which squlare value the differnce is for
    print(f"difference for {difference_spd2}:")
    # Get the squared value of the differnce
    square_dif_spd2 = difference_spd2**2
    # And print out the squared value
    print(square_dif_spd2)

    print("------------ Variance square ------------")
    # The Variance squared are just the numbers added together and devidede by the amount of numbers
    Variance_square = (2061.16+1128.96+3672.36+2440.36+338.56+0.16+384.16) / 7
    print(Variance_square)

    # To automate all that, we can also just use the var() function in numpy, but all of that above was to understand how it works, tho it is simple math

    print("------------ Variation automated with numpy ------------")
    Variance_array_var = numpy.var(Variance_array)
    print(Variance_array_var)

    # Standard Deviation is often represented by the symbol Sigma: σ 
    # Variance is often represented by the symbol Sigma Square: σ2 