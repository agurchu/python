import unittest
from smallest import smallest


class TestSmallest(unittest.TestCase):
    def test_smallest_positive(self):
        self.assertEqual(smallest([1, 2, 3]), 1)

    def test_smallest_negative(self):
        self.assertEqual(smallest([-1, -2, -3]), -3)


if __name__ == "__main__":
    unittest.main()
