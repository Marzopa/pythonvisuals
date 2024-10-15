from PIL import Image, ImageDraw
import numpy as np
from typing import Callable


def pixel_changer(frame: np.array, modifier: Callable[[np.array], np.array]) -> None:
    """
    :post: modifies the image
    :param frame: a np array representing an image (or frame of a video)
    :param modifier: a pixel modifier function
    """
    height, width = frame.shape[:2]
    for y in range(height):
        for x in range(width):
            old_pixel = frame[y, x]
            new_pixel = modifier(old_pixel)
            frame[y, x] = np.clip(new_pixel, 0, 255).astype(np.uint8)


def randomize_modifier(pixel: np.ndarray) -> np.ndarray:
    """
    Randomly modifies the RGB channels of a pixel while keeping the alpha channel unchanged.
    :param pixel: A 4-element array representing RGBA pixel values.
    :return: A modified RGBA pixel value.
    """
    if pixel.shape[0] == 3:  # RGB
        r, g, b = pixel
        r = np.clip(r + np.random.randint(-100, 100), 0, 255)
        g = np.clip(g + np.random.randint(-10, 10), 0, 255)
        b = np.clip(b + np.random.randint(-10, 10), 0, 255)
        return np.array([r, g, b], dtype=np.uint8)

    else:
        raise ValueError('Wrong pixel format')

