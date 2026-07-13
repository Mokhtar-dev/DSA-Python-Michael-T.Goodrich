"""R-1.11: Demonstrate how to use Python's list comprehension syntax to produce the list:
[1, 2, 4, 8, 16, 32, 64, 128, 256]"""

# MY Logic:
# we need to create a list that contain the range function
# we generate from the range(0,9)
# and the generated number will be our exponents
# and we apply the mathematical exponent to the base value 2

result = [2**i for i in range(0, 9)]
print(list(result))
