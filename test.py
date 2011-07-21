"""Test fail
"""

import unittest

class TestExample(unittest.TestCase):
    """
        test class

    """
    def test_always_true(self):
        self.assertEqual(2, 1)

if __name__ == '__main__':
    unittest.main()


