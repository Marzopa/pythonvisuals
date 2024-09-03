import unittest
from loteria import calc_dimensions, draw_loteria
from simple_frame import generate_frame


class MyTestCase(unittest.TestCase):
    def test_calc_dimensions(self):
        self.assertEqual((380, 380), calc_dimensions(3, 3, 120, 120, 5))

    def test_draw_loteria(self):
        images = [generate_frame(), generate_frame(), generate_frame(), generate_frame()]
        loteria = draw_loteria(2, 2, images, 10)
        loteria.show()


if __name__ == '__main__':
    unittest.main()
