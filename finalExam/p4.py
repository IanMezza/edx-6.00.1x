def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    flatten_list = []
    maximum = 0
    for item in t:
        if isinstance(item, list) or isinstance(item, tuple):
            inner_maximum = max_val(item)
            if inner_maximum > maximum:
                maximum = inner_maximum
                continue
            else:
                continue
        else:
            if item > maximum:
                maximum = item
                continue
            else:
                continue
    return maximum