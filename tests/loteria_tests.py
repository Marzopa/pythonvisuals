import unittest
from loteria import calc_dimensions


class MyTestCase(unittest.TestCase):
    def test_calc_dimensions(self):
        self.assertEqual((380, 380), calc_dimensions(3, 3, 120, 120, 5))



if __name__ == '__main__':
    unittest.main()
