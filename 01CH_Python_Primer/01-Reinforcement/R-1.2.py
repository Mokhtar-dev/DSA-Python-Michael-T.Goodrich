"""Write a short Python function, is-even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators."""
# my solution:
# from math import fmod

# def Is_even(k):
#     if  fmod(k,2):
#         return True
#     else:
#         return False
    
    
# print(Is_even(9))

# correct solution:
def is_even(k):
    # k & 1 isolates the very last bit of the number.
    # If the last bit is 0, the number is even!
    return (k & 1) == 0

print(is_even(9))  # Output: False
print(is_even(8))  # Output: True