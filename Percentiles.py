# Topic is, "What are percentiles"

import numpy


ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

# Getting the percentile of 75
percentile_age = numpy.percentile(ages, 75)

print(percentile_age)# This means that 75% are 43 or younger

# Now when we put in more numbers which are different, we get a higher or lower number depending on which numbers we put in
ages2 = [5,31,43,48,50,78,32,41,7,11,15,39,80,82,32,2,34,1,76,32,8,6,25,36,27,61,31]
percentile_age2 = numpy.percentile(ages2, 75)
print(percentile_age2)


# Here the age taht 90% of them are unger then is 61.
ages3 = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

percentile_age3 = numpy.percentile(ages3, 90)

print(percentile_age3) 


# Again, percentile is for getting the % of numbers which are under that percentile number