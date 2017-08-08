def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception.
          For example, sum_digits("a;35d4") returns 12. """
    ans = 0
    ValueErrorCnt = 0
    for element in s:
        try:
            ans += int(element)
        except ValueError:
            ValueErrorCnt += 1
            if ValueErrorCnt == len(s):
                raise ValueError()
            else:
                continue
    return ans