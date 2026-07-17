"""R-1.13: Write a pseudo-code description of a function that reverses a list of n integers,
so that the numbers are listed in the opposite order than they were before, and compare this
method to an implementation of a function that can reverse a list of integers."""

# Pseudo-code:
# My thought is that we will need to use a Doubly-linked list
# this is because we can traverse the list from the start to the end or vice versa
# so i think it will be the best option

# Based on that :
# 1- instantiate the list
# 2- then we mark the start and the end of our elements
# 3- and then we start from the last element index
# 4- then -1 each time so we can get to the start position which will be index 0

# Note this is wrong !! but its going to be something similar following the list structure in python

# the right approach:
#     Initialize two pointers: left at index 0, and right at the last index (length - 1).
#     Loop while left is less than right:
#         Swap the element at left with the element at right.
#         Move left forward by 1 (left = left + 1).
#         Move right backward by 1 (right = right - 1).


def reverse_list(my_list):
    left = 0
    right = len(my_list) - 1
    
    while left < right: # Run while pointers haven't met in the middle
        my_list[left], my_list[right] = my_list[right], my_list[left] # Swap first
        left += 1 # Move inward
        right -= 1 # Move inward
        
    return my_list # Return the actual reversed list

# To see it in the terminal, we MUST wrap the call in a print statement!
print(reverse_list([1, 2, 3, 4, 5, 6, 7, 8]))

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

my_list.reverse()  # 1. Trigger the action to flip the list in-place
print(my_list)     # 2. Print the updated list container