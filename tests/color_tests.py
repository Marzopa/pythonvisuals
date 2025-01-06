import unittest

import numpy as np
from PIL import Image
from color import *
import moviepy.editor as mpy


class MyTestCase(unittest.TestCase):
    def test_pixel_changer(self):
        test_image = np.array(Image.open('small_image.jpg').convert('RGB'))
        for i in range(1000):
            test_image = randomize_modifier(test_image, i//10)
            Image.fromarray(test_image).save(f'batch_tests/modified_image{i}.png')

        image_files = [f'batch_tests/modified_image{i}.png' for i in range(1000)]
        clip = mpy.ImageSequenceClip(image_files, fps=24)  # Set your desired fps

        clip.write_videofile('derangeify.mp4', codec='libx264')

