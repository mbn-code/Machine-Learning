# part 2 of Linear_Regression.py

from scipy import stats

# Predicting a future value.

# Here we see that there are no 10 year old car, we will use the other values to predict a speed
age = [5,7,8,7,2,17,2,9,4,11,12,9,6]
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]



# Method to retun key values of linear regression.
            # r is the relationship between variables
slope, intercept, r, p, std_err = stats.linregress(age,speed)

# Function which uses slop eand intercept values to return x. The value represents where on the y axies the x value will be placed
def main(x):
    return slope * x + intercept

# This will predict the speed of a 10 year old car
speed = main(10) # Using the function paramenter x we can use the function to input a speed

print(speed)


import numpy

# As said r is the relationship between variables
# We can also output this value to the terminal to see the value for our selves.
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)