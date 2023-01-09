#The given code declares an array which stores the monthly revenues of a company for 12 months.
#Each value corresponds to a month, the first value is for January, the second for February, etc.
#You need to calculate and output the average monthly revenue of the company for that year.
#Hint: Use the sum() function to calculate the sum of all values of the array and divide it by the count of the values.

revenue = [125000, 200000, 150000, 175000, 162000, 120000, 98000, 105400, 198000, 202500, 97000, 220500]

res = sum(revenue) / 12

print(res)