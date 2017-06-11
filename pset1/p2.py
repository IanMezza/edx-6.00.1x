import unittest

# String -> Int
# Prints the number of times the string 'bob' occurs in s
def countBobs(s):
    index = 0
    stop = 3
    count = 0
    test = 'bob'
    rebanada = ''
    sobras = ''
    if (test in s):
        # There is at least one coincidence
        for n in s:
            rebanada = s[index : stop]
            sobras = s[index + 1 : len(s)]
            if(test in rebanada):
                count += 1
                if(test not in sobras):
                    # If there are not more coincidences just exit the loop
                    break   
            index += 1
            stop += 1
    print('Number of times bob occurs is: ', count)
    return count

# Test cases
# countBobs('azcbobobegghakl') should produce 2
# countBobs('azcbobegghakl') should produce 1
# countBobs('azcbobegghaklbobob') should produce 3
class TestCodeEdX(unittest.TestCase):
    def test_count(self):
        self.assertEqual(countBobs('azcbobobegghakl'), 2)
        self.assertEqual(countBobs('azcbobegghakl'), 1)
        self.assertEqual(countBobs('azcbobegghaklbobob'), 3)

# Execute unit testing
if __name__ == '__main__':
    unittest.main()