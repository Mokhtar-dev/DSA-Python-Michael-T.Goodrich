"""write a short Python function, is-multiple(n, m), that takes two integer
Values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise."""
# MY solution:
# def Is_multiple(n,m):
#     I = print(input("Enter the number I: "))
#     if n == m*I:
#         return True
#     else:
#         return False
    
# print(Is_multiple(8,4))

# Correct solution:
def is_multiple(n, m):
    # If n divided by m has a remainder of 0, then n is a multiple of m!
    if n % m == 0:
        return True
    else:
        return False

# Test cases
print(is_multiple(8, 4))   # Output: True (because 8 = 4 * 2)
print(is_multiple(10, 3))  # Output: False (because 10 / 3 leaves a remainder of 1)