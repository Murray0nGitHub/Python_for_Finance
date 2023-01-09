#You are given a list of house prices in a neighborhood, sorted in ascending order.
#There are an odd number of houses on the list.
#Create a function that calculates and returns the median house price.

#The given code defines and calls a function called "median()". Complete its definition to calculate and return the median value of its argument array.

#Hint: Since there is an odd number of houses], we can take the middle element of the array, which will represent the median value.
#To do that, divide the count of elements in the array by 2. This will result in the index of the middle element, like this:
#index = len(arr)//2
#return arr[index]

#Note, that we need to use the // operator, which is floor division which results in a whole number.


prices = [75000, 95000, 98000, 109000, 135500, 185000, 199000, 249000, 255000, 280000, 299000, 330000, 380000]


def median(arr):
    index = len(arr) // 2
    return arr[index]


res = median(prices)
print(res)