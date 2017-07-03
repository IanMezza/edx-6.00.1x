"""Problem 6
Write a function that satisfies the following docstring:
"""
def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """

    # Set frequency dictionary
    freqDict = {}
    for item in L:
        if item in freqDict:
            freqDict[item] += 1
        else:
            freqDict[item] = 1
    
    # Remove even frequency keys
    keys_to_be_removed = []
    for k in freqDict:
        if freqDict[k] % 2 == 0:
            keys_to_be_removed.append(k)
        else:
            continue
    for k in keys_to_be_removed:
        freqDict.pop(k)
    # Convert iterable view to list
    odd_times_values = []
    for item in freqDict.keys():
        odd_times_values.append(item)
    if len(odd_times_values) > 0:
        return max(odd_times_values)
    else:
        return None