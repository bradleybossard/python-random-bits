import random

# Find the maximum value of the largest subarray.

# https://en.wikipedia.org/wiki/Maximum_subarray_problem

def max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

scale = 100

array = [int(random.random() * scale - scale/2) for i in range(10)]
print(array)
print(max_subarray(array))
