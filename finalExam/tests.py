import unittest
from p3 import *
from p4 import *
from p5 import *

# Test cases
class TestCodeEdX(unittest.TestCase):
    def test_count(self):
        self.assertEqual(sum_digits('a;35d4'), 12)
        # self.assertEqual(sum_digits('a;d'), ValueError)
        # self.assertRaises(ValueError, sum_digits('a;d'))
        self.assertEqual(max_val((5, (1,2), [[1],[2]])), 5)
        self.assertEqual(max_val((5, (1,2), [[1],[9]])), 9)
        self.assertEqual(max_val([5, 3, 90, 10]), 90)
        self.assertEqual(max_val([5, 3, 90, 110]), 110)
        self.assertEqual(cipher("abcd", "dcba", "dab"), ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc'))
# Execute unit testing
if __name__ == '__main__':
    unittest.main()