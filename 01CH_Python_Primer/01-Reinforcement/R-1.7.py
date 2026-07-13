"""Write a short Python function that takes a 
positive integer n and returns the sum of the squares 
of all the odd positive integers smaller than n. 
However, you must use Python's list comprehension syntax."""
# pseudo code:
# Declare a function 
# make a list that contains numbers
# iterate the list values backwards 
# check if the value is odd (if true return value)
# square the odd values
# add them all together 

def sum_squares_loop(n):
    return sum([i**2 for i in range(1, n) if i % 2 != 0])
print(sum_squares_loop(5))