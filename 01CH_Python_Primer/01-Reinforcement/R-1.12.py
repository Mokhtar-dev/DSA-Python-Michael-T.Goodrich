"""Python’s random module includes a function randrange(start, stop)
that returns a random integer from the given range.
Use this tool to write a function that returns a random element from a non-empty sequence.
"""
# first of all import the module
# second create a list that contain and set of elements 
# use the function to randomly return a random element from the list

import random

def get_random_element(my_sequence):
    # 1. Get the total length of the sequence
    total_items = len(my_sequence)  
    # 2. Use randrange to pick a random index from 0 to total_items
    random_index = random.randrange(0, total_items)
    # 3. Return the element at that random index
    
    return my_sequence[random_index]
    
print(get_random_element([1,2,3,6,4,8,9,7]))