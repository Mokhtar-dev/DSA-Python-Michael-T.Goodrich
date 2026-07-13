"""Python allows negative indices to look up elements in a sequence from the end. 
If a string s has length n, and we look up an item at a negative index k (where -n \le k < 0), 
what is the equivalent positive index that points to the exact same element?"""

# the answer will n+k
# for example   s = "python" which have 6 character with indices with range of (0-5)
# and k equals -1 
# so based on that information the answer will be n + K
# no code this is a conceptual answer