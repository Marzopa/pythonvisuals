import unittest

import numpy as np
from PIL import Image
from color import *


class MyTestCase(unittest.TestCase):
    def test_pixel_changer(self):
        test_image = np.array(Image.open('small_image.jpg').convert('RGB'))
        for i in range(100):
            test_image = randomize_modifier(test_image, i)
            Image.fromarray(test_image).save(f'batch_tests/modified_image{i}.png')

