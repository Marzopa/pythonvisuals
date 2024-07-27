import numpy as np
import cv2
import moviepy.editor as mpy


def generate_frame(t):
    # Create an empty canvas
    width, height = 640, 480
    canvas = np.zeros((height, width, 3), dtype=np.uint8)

    # Draw some animated circles
    for _ in range(50):
        center = (np.random.randint(0, width), np.random.randint(0, height))
        color = (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256))
        radius = int(5 + 45 * np.abs(np.sin(t)))
        cv2.circle(canvas, center, radius, color, -1)

    return canvas

# Create a video
duration = 10  # Duration in seconds
fps = 24  # Frames per second
clip = mpy.VideoClip(lambda t: generate_frame(t), duration=duration)
clip.write_videofile("abstract_art.mp4", fps=fps)
