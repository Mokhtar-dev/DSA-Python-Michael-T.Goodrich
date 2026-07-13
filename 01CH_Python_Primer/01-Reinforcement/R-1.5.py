"""Give a single command that computes the sum from Exercise R-1.4, rely-
ing on Python's comprehension syntax and the built-in sum function."""

# 1. The Standard Loop Way (What you know)
def sum_squares_loop(n):
    return sum([i**2 for i in range(1, n)])
print(sum_squares_loop(5))