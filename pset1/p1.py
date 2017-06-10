import unittest

# String -> None
# counts up the number of vowels contained in the string s and print the result

def countVowels(s):
    count = 0
    for n in s:
        if(n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u'):
            count += 1
    print('Number of vowels:',count)
    return count


# Test cases
# countVowels('abuelita') should print 'Number of vowles 5'
# countVowels('azcbobobegghakl') should print 'Number of vowles 5'

class TestCodeEdX(unittest.TestCase):
    def test_count(self):
        self.assertEqual(countVowels('abuelita'), 5)
        self.assertEqual(countVowels('azcbobobegghakl'), 5)

if __name__ == '__main__':
    unittest.main()