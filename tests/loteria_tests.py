import unittest
from loteria import calc_dimensions, draw_loteria
from simple_frame import generate_frame


class MyTestCase(unittest.TestCase):
    def test_calc_dimensions(self):
        self.assertEqual((380, 380), calc_dimensions(3, 3, (120, 120), 5))

    def test_draw_loteria(self):
        images = []
        for _ in range(9):
            images.append(generate_frame())

        loteria = draw_loteria(3, 3, images, 5)
        loteria.show()


if __name__ == '__main__':
    unittest.main()
