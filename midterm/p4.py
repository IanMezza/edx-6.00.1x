"""Problem 4
Write a function is_triangular that meets the specification below. A triangular number is a number obtained by the continued summation of integers starting from 1. For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    triangular_number = 0
    for i in range(1, k+1):
        triangular_number = triangular_number + i
        if triangular_number == k:
            return True
        elif triangular_number > k:
            return False
        else:
            continue