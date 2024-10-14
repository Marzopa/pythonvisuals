from PIL import Image, ImageDraw
import numpy as np
import moviepy.editor as mpy
from loteria import draw_loteria

# Parameters
width, height = 120, 120
dur = 10  # Duration in seconds
fps = 24  # Frames per second
total_frames = dur * fps


def generate_frame(t):
    # Create an empty canvas
    canvas = Image.new('RGB', (width, height), 'black')
    draw = ImageDraw.Draw(canvas)

    # Draw some animated circles
    for _ in range(100):
        x, y = np.random.randint(0, width), np.random.randint(0, height)
        radius = int(5 + 45 * np.abs(np.sin(2 * np.pi * t)))
        color = (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256))
        draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=color)

    for _ in range(50):
        x1, y1 = np.random.randint(0, width), np.random.randint(0, height)
        x2, y2 = np.random.randint(0, width), np.random.randint(0, height)
        color = (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256))
        draw.line((x1, y1, x2, y2), fill=color, width=3)

    # Draw some random rectangles
    for _ in range(20):
        x1, y1 = np.random.randint(0, width), np.random.randint(0, height)
        x2, y2 = np.random.randint(x1, width), np.random.randint(y1, height)
        color = (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256))
        draw.rectangle((x1, y1, x2, y2), outline=color, width=3)

    return np.array(canvas)


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


# Create a video using moviepy
clip = mpy.VideoClip(lambda t: generate_frame(t), duration=dur)
clip.write_videofile("abstract_art.mp4", fps=fps)
