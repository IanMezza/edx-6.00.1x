import unittest

# String -> String
# Prints the longest substring of s in which the letters occur in alphabetical order.
def printLongest(s):
    index = 0
    startPoint = 1
    aux1 = ''
    aux2 = ''
    aux3 = 0
    longest = ''
    for letra in s:
        temp = letra
        aux1 = letra
        aux2 = s[index + 1 : index + 2]
        startPoint = index + 1
        while aux1 <= aux2:
            temp = temp + aux2
            startPoint += 1
            aux1 = aux2
            aux2 = s[startPoint : startPoint + 1]
        if len(temp) > aux3:
            aux3 = len(temp)
            longest = temp
        index += 1
    print('Longest substring in alphabetical order is: ', longest)
    return longest

# Test cases
# printLongest('azcbobobegghakl') should produce 'beggh'
# printLongest('abcbcd') should produce 'abc'
class TestCodeEdX(unittest.TestCase):
    def test_count(self):
        self.assertEqual(printLongest('azcbobobegghakl'), 'beggh')
        self.assertEqual(printLongest('abcbcd'), 'abc')

# Execute unit testing
if __name__ == '__main__':
    unittest.main()