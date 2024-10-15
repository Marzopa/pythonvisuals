import unittest

import numpy as np
from PIL import Image
from color import *


class MyTestCase(unittest.TestCase):
    def test_pixel_changer(self):
        test_image = np.array(Image.open('small_image.jpg').convert('RGB'))

        Image.fromarray(randomize_modifier(test_image)).save('modified_image.png')
