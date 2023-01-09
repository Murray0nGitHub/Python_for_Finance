#The Standard deviation is a measure of how spread out numbers are.
#You are given an array of house prices and need to calculate the standard deviation of the prices.
#Import the correct package and use the corresponding function to calculate the standard deviation of the array and output it using the print statement.


prices = [75000, 95000, 98000, 109000, 135500, 185000, 199000, 249000, 255000, 280000, 299000, 330000, 380000]

import numpy as np
res = np.std(prices)

print(res)