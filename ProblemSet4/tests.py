import unittest
from ps4a import *

# Test cases
class TestCodeEdX(unittest.TestCase):
    def test_count(self):
        # Only adding tests for functions that are not in tested in test_ps4a.py
        self.assertEqual(calculateHandlen({'a': 3, 'b':2, 'c':1}), 6)

# Execute unit testing
if __name__ == '__main__':
    unittest.main()