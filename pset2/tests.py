import unittest
from p1 import *
from p2 import *
from p3 import *

# Test cases
class TestCodeEdX(unittest.TestCase):
    def test_count(self):
        self.assertEqual(remainingBalance(42, 0.2, 0.04), 31.38)
        self.assertEqual(remainingBalance(484, 0.2, 0.04), 361.61)
        self.assertEqual(estimateLowestPayment(3329, 0.2, 10), 310)
        self.assertEqual(estimateLowestPayment(4773, 0.2, 10), 440)
        self.assertEqual(estimateLowestPayment(3926, 0.2, 10), 360)
        self.assertEqual(estimateLowestPaymentBisection(320000, 0.2), 29157.09)
        self.assertEqual(estimateLowestPaymentBisection(999999, 0.18), 90325.03)

# Execute unit testing
if __name__ == '__main__':
    unittest.main()