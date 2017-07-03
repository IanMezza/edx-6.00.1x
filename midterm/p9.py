"""Problem 9
20.0 points possible (graded)
Write a Python function that takes in two lists and calculates whether they are permutations of each other. The lists can contain both integers and strings. We define a permutation as follows:

    * the lists have the same number of elements
    * list elements appear the same number of times in both lists

If the lists are not permutations of each other, the function returns False. 
If they are permutations of each other, the function returns a tuple consisting of the following elements:

    * the element occuring the most times
    * how many times that element occurs
    * the type of the element that occurs the most times

If both lists are empty return the tuple (None, None, None). If more than one element occurs the most number of times, you can return any of them.
"""
def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    # Verify lists are both trhe same length
    if len(L1) == len(L2):
        # Check for empty lists
        if len(L1) == 0:
            return (None, None, None)
        else:
            # They're the same length, let's make frequency dictionaries
            freqDictL1 = {}
            freqDictL2 = {}
            for item in L1:
                if item in freqDictL1:
                    freqDictL1[item] += 1
                else:
                    freqDictL1[item] = 1
            for item in L2:
                if item in freqDictL2:
                    freqDictL2[item] += 1
                else:
                    freqDictL2[item] = 1
            # Check frecuencies are the same
            for dictKey in freqDictL1.keys():
                try:
                    if freqDictL2[dictKey] == freqDictL1[dictKey]:
                        continue
                    else:
                        return False
                except KeyError:
                    return False
            # Assigning return values
            most_occuring_times = max(freqDictL1.values())
            for dictKey in freqDictL1.keys():
                if freqDictL1[dictKey] == most_occuring_times:
                    most_occuring_element = dictKey
                    break
                else:
                    continue
            return (most_occuring_element, most_occuring_times, type(most_occuring_element))
    else:
        return False

# print(is_list_permutation([1,2,3,4,5,1,3], [1,5,1,4,3,2,3]))