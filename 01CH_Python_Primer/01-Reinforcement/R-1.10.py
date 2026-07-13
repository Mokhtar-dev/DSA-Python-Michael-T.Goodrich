"""What parameters should be sent to the range() constructor to produce a range object
that generates the sequence: 8, 6, 4, 2, 0, -2, -4, -6, -8?"""

# my answer:
# the_sequence = range(-8, 9, 1)
# print(list(the_sequence))

# correct answer:
# Start at 8, count down toward -10, skipping by -2 each time
the_sequence = range(8, -10, -2)
print(list(the_sequence))