import unittest
from p4 import *
from p5 import *
from p6 import *
from p7 import *
from p8 import *
from p9 import *

# Test cases
class TestCodeEdX(unittest.TestCase):
    def test_count(self):
        # Problem 4
        self.assertEqual(is_triangular(1), True)
        self.assertEqual(is_triangular(3), True)
        self.assertEqual(is_triangular(6), True)
        self.assertEqual(is_triangular(10), True)
        self.assertEqual(is_triangular(2), False)
        self.assertEqual(is_triangular(4), False)
        self.assertEqual(is_triangular(5), False)
        self.assertEqual(is_triangular(7), False)
        # Problem 5
        self.assertEqual(print_without_vowels('abuelita'), 'blt')
        self.assertEqual(print_without_vowels('abuelito'), 'blt')
        self.assertEqual(print_without_vowels('arbol'), 'rbl')
        self.assertEqual(print_without_vowels('ian'), 'n')
        self.assertEqual(print_without_vowels('arely'), 'rly')
        self.assertEqual(print_without_vowels('aletse'), 'lts')
        self.assertEqual(print_without_vowels('parangaricutirimicuaro'), 'prngrctrmcr')
        self.assertEqual(print_without_vowels('a'), '')
        # Problem 6
        self.assertEqual(largest_odd_times([2, 2]), None)
        self.assertEqual(largest_odd_times([2, 2, 4, 4]), None)
        self.assertEqual(largest_odd_times([3, 2]), 3)
        self.assertEqual(largest_odd_times([3, 3, 2, 0]), 2)
        self.assertEqual(largest_odd_times([3, 0, 5, 3, 5, 3]), 3)
        self.assertEqual(largest_odd_times([3, 9, 5, 3, 5, 3]), 9)
        self.assertEqual(largest_odd_times([6, 8, 6, 8, 6, 8, 6, 8, 6, 8]), 8)
        self.assertEqual(largest_odd_times([2, 4, 5, 4, 5, 4, 2, 2]), 4)
        # Problem 7
        self.assertEqual(dict_invert({1:10, 2:20, 3:30}), {10: [1], 20: [2], 30: [3]})
        self.assertEqual(dict_invert({1:10, 2:20, 3:30, 4:30}), {10: [1], 20: [2], 30: [3, 4]})
        self.assertEqual(dict_invert({4:True, 2:True, 0:True}), {True: [0, 2, 4]})
        # Problem 8
        self.assertEqual(general_poly([1,2,3,4])(10), 1234)
        self.assertEqual(general_poly([1,2,3,4])(-10), -1234)
        self.assertEqual(general_poly([1,2,3,4])(6), 335.2)
        # Problem 9
        self.assertEqual(is_list_permutation([1,2,3,4,5,1,3], [1,5,1,4,3,2,3]), (1, 2, type(1)))
        self.assertEqual(is_list_permutation(['a', 'a', 'b'], ['a', 'b']), False)
        self.assertEqual(is_list_permutation([1, 'b', 1, 'c', 'c', 1], ['c', 1, 'b', 1, 1, 'c']), (1, 3, type(1)))
        self.assertEqual(is_list_permutation([], []), (None, None, None))

# Execute unit testing
if __name__ == '__main__':
    unittest.main()