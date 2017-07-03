"""Problem 7
Write a function called dict_invert that takes in a dictionary with immutable values and returns the inverse of the dictionary. The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d. The value for a key in the inverse dictionary is a sorted list (increasing order) of all keys in d that have the same value in d.

Here are two examples:

If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
"""

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    dict_inverted_keys = []
    dict_inverted_values = []
    dict_inverted = {}
    for value in d.values():
        if value in dict_inverted_keys:
            continue
        else:
            dict_inverted_keys.append(value)
    for k in d.keys():
        dict_inverted_values.append(k)
    for new_key in dict_inverted_keys:
        new_key_list_of_values = []
        for old_key in d.keys():
            if d[old_key] == new_key:
                new_key_list_of_values.append(old_key)
            else:
                pass
        new_key_list_of_values.sort()
        dict_inverted[new_key] = new_key_list_of_values
    return dict_inverted