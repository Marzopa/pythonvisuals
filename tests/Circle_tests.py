import math
import unittest
import moviepy.editor as mpy
from PIL import Image, ImageDraw
import random as r
import numpy as np

from shapes.Circle import Circle


def test_circle():
    circle_list = [Circle(radius=75, color=(255, 0, 0), center=[960, 500],
                          velocity=(50, math.pi/4), collisions=(1920, 1080), friction=0.99)]
    for i in range(99):
        circle_list.append(Circle(radius=r.randint(50, 100),
                                  color=(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)),
                                  center=[960, 540],
                                  velocity=(r.randint(3, 20), r.randint(0,100)*math.pi/50),
                                  gravity=-0.2725, collisions=(1920, 1080), friction=0.99))

    frames = []
    for i in range(500):
        canvas = Image.new('RGB', (1920, 1080), 'black')
        draw = ImageDraw.Draw(canvas)
        for circle in circle_list:
            circle.draw_on_frame(draw)
            circle.update_frame()
        frames.append(np.array(canvas))

    clip = mpy.ImageSequenceClip(frames, fps=60)  # Set your desired fps

    clip.write_videofile('circle_test1.mp4', codec='libx264')


class MyTestCase(unittest.TestCase):
    pass
