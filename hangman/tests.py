import unittest
from ps3_hangman import *

# Test cases
class TestCodeEdX(unittest.TestCase):
    def test_count(self):
        self.assertEqual(isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']), False)
        self.assertEqual(isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']), True)
        self.assertEqual(isWordGuessed('lettuce', ['k', 'n', 'd', 'e', 'i', 'm', 'v', 'h', 'a', 'g']), False)
        self.assertEqual(isWordGuessed('pineapple', ['p', 'a', 'i', 'x', 'z', 'c', 'q', 'e', 's', 'w']), False)
        self.assertEqual(isWordGuessed('pineapple', []), False)
        self.assertEqual(isWordGuessed('grapefruit', ['z', 'x', 'q', 'g', 'r', 'a', 'p', 'e', 'f', 'r', 'u', 'i', 't']), True)

# Execute unit testing
if __name__ == '__main__':
    unittest.main()