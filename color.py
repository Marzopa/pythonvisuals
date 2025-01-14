from PIL import Image, ImageDraw, ImageFilter
import numpy as np


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


def glow_modifier(frame: Image, radius: float = 10.0) -> Image:
    """
    Applies glow effect to Image object
    :param frame: An Image object (representing a frame of video)
    :param radius: the radius to apply blur with
    :return: the modified Image object with glow effect applied
    """
    # Create a blurred copy of the image
    blurred_image = frame.filter(ImageFilter.GaussianBlur(radius=radius))

    # Blend the original image with the blurred image
    glow_image = Image.blend(frame, blurred_image, 0.5)

    return glow_image


