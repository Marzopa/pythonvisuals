import unittest
import moviepy.editor as mpy
from loteria import calc_dimensions, draw_loteria
from simple_frame import generate_frame
from video import stitch_videos


class MyTestCase(unittest.TestCase):
    def test_calc_dimensions(self):
        self.assertEqual((380, 380), calc_dimensions(3, 3, (120, 120), 5))

    def test_draw_loteria(self):
        images = []
        for _ in range(9):
            images.append(generate_frame())

        loteria = draw_loteria(3, 3, images, 5, draw_outer=False)
        loteria.show()

    def test_stitch_videos(self):
        videos = []
        for _ in range(4):
            videos.append(mpy.VideoFileClip("1.mp4"))
        video = stitch_videos(videos, 2, 2)
        video.write_videofile("shit.mp4", fps=24, codec="libx264")


if __name__ == '__main__':
    unittest.main()
