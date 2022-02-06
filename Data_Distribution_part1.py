# A data distribution is a function or a listing which shows all the possible values (or intervals) of the data - https://www.statisticshowto.com/data-distribution/

import numpy

                            # Here the 0.0 is representing the lowest value
                                    # The 2.0 is the highest value
                                     # And the 250 is the amount of different data
random_uniform = numpy.random.uniform(0.0,2.0,250)
print(random_uniform)


# Creating a histogram with random data generation
# For this example we use matplotlib 

import matplotlib.pyplot as plt

# Generating the data for the histogram
random_uniform_histogram = numpy.random.uniform(0.0,5.0,250)

# Making the histogram with matplotlib
plt.hist(random_uniform_histogram, 5) # The random_uniform_histogram is the data we want to display, and the second value -> 5 is the amount of bars
plt.show()

