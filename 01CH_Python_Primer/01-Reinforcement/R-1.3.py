"""Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution"""

# def min_max(data):
#   max
#   min
#   data = list()
#   data.append(1)
#   data.append(2)
#   data.append(3)
#   data.append(4)
#   data.append(5) 
#   for max in data:      
#    if max > data.count:
#     return max

# min_max(1)     

# correct solution :
def min_max(data):
    # Base Case: Assume the very first number (index 0) is both the min and max
    current_min = data[0]
    current_max = data[0]
    
    # Loop through every single number in the sequence
    for number in data:
        if number < current_min:
            current_min = number  # Found a new smallest number!
        if number > current_max:
            current_max = number  # Found a new largest number!
            
    # Return the result as a tuple of length two
    return (current_min, current_max)

# --- Testing the implementation ---
test_sequence = [14, 3, 22, 1, 95, 40]
print(min_max(test_sequence))  # Output: (1, 95)