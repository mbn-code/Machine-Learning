from scipy import stats
import matplotlib.pyplot as plt


# This just scatters age and speed. x = age, y = speed as mentioned in Scatter_plot.py
age = [5,7,8,7,2,17,2,9,4,11,12,9,6]

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]


# Method to retun key values of linear regression.
slope, intercept, r, p, std_err = stats.linregress(age,speed)

# Function which uses slop eand intercept values to return x. The value represents where on the y axies the x value will be placed
def main(x):
    return slope * x + intercept

# use this function now to run each value of the x array. This iwll give a new array with new values for the y axies.
model = list(map(main, age))

            # x, y
plt.scatter(age, speed)
plt.plot(age, model )
plt.show()



