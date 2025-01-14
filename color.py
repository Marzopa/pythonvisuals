from PIL import Image, ImageDraw
import numpy as np
from typing import Callable


def randomize_modifier(frame: np.ndarray, t: int = 10) -> np.ndarray:
    """
    Applies random noise to the RGB channels of an image while preserving the alpha channel if present.
    :param frame: A numpy array representing an image (or frame of a video)
    :param t: range for random noise level range to apply
    :return: A modified image array with random noise added to RGB channels.
    """
    if frame.shape[2] != 3:
        raise ValueError('Expected an RGB image with 3 channels.')
    if t == 0:
        return frame

    noise = np.random.randint(-t, t, frame.shape, dtype=np.int16)
    modified_frame = frame.astype(np.int16) + noise
    modified_frame = np.clip(modified_frame, 0, 255).astype(np.uint8)
    return modified_frame


def glow_modifier():
    pass

