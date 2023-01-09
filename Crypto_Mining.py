#You decide to start a crypto mining business in January 2017. It requires an initial investment of $500K to buy the required mining hardware.
#Each year it will be able to mine 10 coins. So, your first return will be on January 1, 2018.
#The price of the coin for each year is given in an array in the code.

#Task
#Calculate the return for each year and output the IRR of the project.
#You can calculate how much 10 coins will be worth each year, add the values to an array and then use the npf.irr() function to calculate the IRR. Remember, the first value of the array should be the initial investment as a negative value.


import numpy_financial as npf

#price for 2018-2021
price = [-500000, 30000, 80000, 293000, 380000]

print(npf.irr(price))