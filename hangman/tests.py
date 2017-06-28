import unittest
from ps3_hangman import *

# Test cases
class TestCodeEdX(unittest.TestCase):
    def test_count(self):
        # isGuessedWord tests
        self.assertEqual(isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']), False)
        self.assertEqual(isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']), True)
        self.assertEqual(isWordGuessed('lettuce', ['k', 'n', 'd', 'e', 'i', 'm', 'v', 'h', 'a', 'g']), False)
        self.assertEqual(isWordGuessed('pineapple', ['p', 'a', 'i', 'x', 'z', 'c', 'q', 'e', 's', 'w']), False)
        self.assertEqual(isWordGuessed('pineapple', []), False)
        self.assertEqual(isWordGuessed('grapefruit', ['z', 'x', 'q', 'g', 'r', 'a', 'p', 'e', 'f', 'r', 'u', 'i', 't']), True)
        # getGuessedWord tests
        self.assertEqual(getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's']), '_ pp_ e')
        self.assertEqual(getGuessedWord('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']), 'durian')
        self.assertEqual(getGuessedWord('pineapple', ['s', 'f', 'g', 'v', 'c', 'w', 'y', 'e', 'z', 'j']), '_ _ _ e_ _ _ _ e')
        self.assertEqual(getGuessedWord('banana', ['o', 'x', 'u', 'd', 'a', 'q', 'f', 'p', 'v', 'j']), '_ a_ a_ a')
        self.assertEqual(getGuessedWord('coconut', []), '_ _ _ _ _ _ _ ')
        self.assertEqual(getGuessedWord('carrot', ['v', 'y', 'i', 't', 'f', 'k', 'j', 'c', 'r', 'u']), 'c_ rr_ t')


# Execute unit testing
if __name__ == '__main__':
    unittest.main()