from PIL import Image, ImageDraw
import numpy as np


def generate_frame(size: tuple[int, int] = (120, 120)):
    # Create an empty canvas
    width, height = size[0], size[1]
    canvas = Image.new('RGB', (width, height), 'black')
    draw = ImageDraw.Draw(canvas)

    # Draw some random lines
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

    return canvas

