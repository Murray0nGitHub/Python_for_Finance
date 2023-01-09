#You need to calculate the monthly payments on a loan of $500,000 over 30 years. The annual interest rate is 4%, and interest is calculated monthly.
#Write a program to calculate and output the result.

#Hint: Use the pmt() function of the NumPy Financial package. It has the following syntax:
#pmt(rate, nper, pv, fv)

#Note that your future value (fv) should be 0, while the present value (pv) is 500,000.
#Remember, the nper and rate arguments need to be monthly, meaning that the rate should be divided by 12, while the nper period should be in months (years*12).


import numpy_financial as npf

res = npf.pmt(rate=0.04/12, nper=30*12, pv=500000, fv=0)
print(res)