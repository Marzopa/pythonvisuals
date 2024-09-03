from PIL import Image, ImageDraw


def calc_dimensions(rows: int, cols: int, img_width: int, img_height: int, thickness: int=20):
    """
    :param rows: number of rows in the loteria
    :param cols: number of columns in the loteria
    :param img_width: width of each image square (in px)
    :param img_height: height of each image square (in px)
    :param thickness: thickness of lines drawn on the loteria (default 20px)
    :return: a tuple (width, height)
    """
    return img_width*cols + (cols+1)*thickness, img_height*rows + (rows+1)*thickness


def draw_loteria(rows: int, cols: int, images: list[Image], thickness: int=20):
    """
    :param rows: number of rows in loteria
    :param cols: number of columns in loteria
    :param images: a list of image objects to draw loteria from, assumes all image dimensions are the same
    :param thickness: thickness of lines drawn on the loteria (default 20px)
    :return: an image of the loteria
    :raises: ValueError if number of images isn't the same as the number of squares in loteria
    """
    if rows*cols != len(images):
        raise ValueError("Incorrect number of images")

    canvas = Image.new('RGB', (1920, 1080), 'black')
    draw = ImageDraw.Draw(canvas)

