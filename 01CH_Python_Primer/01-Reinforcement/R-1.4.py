# R-1.4 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

# MY algorithm:
# function Declaration 
# list Declaration
# variable to determine the current number 
# iterate through the current number backwards until we reach the value zero 
# then grab all the numbers from the current number to the zero and Square them and add them all

# # My solution:
# def Sum_Square():
#     current_num = Sum_Square[Sum_Square]
#     while current_num > 0:
#         return current_num[]

# correction: 
def sum_of_squares(n):
    total = 0
    # Start at the first number smaller than n
    current_num = n - 1  
    
    # Keep looping as long as current_num hasn't reached 0
    while current_num > 0:
        total += current_num ** 2  # Square it and add to total
        current_num -= 1           # Decrement to count down (crucial!)
        
    return total

print(sum_of_squares(5))  # Output: 30

# for loop approach:
def sum_of_squares(n):
    total = 0
    for i in range(1, n):
        # Python shorthand for: total = total + (i ** 2)
        total += i ** 2  
    return total

print(sum_of_squares(5)) # Output should be 30