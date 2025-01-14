from PIL import Image, ImageDraw
import numpy as np
import moviepy.editor as mpy
from loteria import draw_loteria


def stitch_videos(clips: list[mpy.VideoFileClip], rows: int, cols: int, thickness: int = 20,
                  draw_inner: bool = True, draw_outer: bool = True) -> mpy.ImageSequenceClip:
    """
    :param clips: a list of videos opened from file, assumes are all same length and fps
    :param rows: number of rows in final video
    :param cols: number of columns in final video
    :param thickness: thickness of borders (default 20)
    :param draw_inner: whether to draw inner edges or not
    :param draw_outer: whether to draw outer edges or not
    :return: a video clip with the clips stitched in a loteria grid
    """
    if len(clips) != rows * cols:
        raise ValueError("Wrong number of clips")
    video_length = int(clips[0].duration * clips[0].fps)
    final_frames = []

    for i in range(video_length):
        frames = []
        for clip in clips:
            frames.append(Image.fromarray(clip.get_frame(i / clips[0].fps)))

        final_frames.append(draw_loteria(rows, cols, frames, thickness, draw_inner=draw_inner, draw_outer=draw_outer))

    frames = [np.array(img) for img in final_frames]
    return mpy.ImageSequenceClip(frames, fps=clips[0].fps)


def generate_numbers_video(rows: int, cols: int, duration: int, thickness: int = 20, fps: int = 24):
    """
    :param rows: number of rows in video
    :param cols: number of columns in video
    :param duration: duration of video in seconds
    :param fps: frames per second (duh)
    :param thickness: thickness of borders in pixels
    :return: a video clip with the clips stitched in a loteria grid
    """
    pass



