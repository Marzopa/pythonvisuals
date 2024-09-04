from PIL import Image, ImageDraw


def calc_dimensions(rows: int, cols: int, size: tuple, thickness: int = 20):
    """
    :param rows: number of rows in the loteria
    :param cols: number of columns in the loteria
    :param size: a tuple (width, height) for size of each image
    :param thickness: thickness of lines drawn on the loteria (default 20px)
    :return: a tuple (width, height)
    """
    return size[0] * cols + (cols + 1) * thickness, size[1] * rows + (rows + 1) * thickness


def draw_loteria(rows: int, cols: int, images: list[Image], thickness: int = 20):
    """
    :param rows: number of rows in loteria
    :param cols: number of columns in loteria
    :param images: a list of image objects to draw loteria from, assumes all image dimensions are the same
    :param thickness: thickness of lines drawn on the loteria (default 20px)
    :return: an image of the loteria
    :raises: ValueError if number of images isn't the same as the number of squares in loteria
    """
    if rows * cols != len(images):
        raise ValueError("Incorrect number of images")

    img_size: tuple = images[0].size
    dimensions = calc_dimensions(rows, cols, img_size, thickness)
    canvas = Image.new('RGB', dimensions, 'black')
    draw = ImageDraw.Draw(canvas)

    thick_adjustment = thickness * 2  # This is so thickness of borders is respected

    # This section creates the top and left edges
    draw.line((0, 0, dimensions[0], 0), fill='white', width=thick_adjustment)
    draw.line((0, 0, 0, dimensions[1]), fill='white', width=thick_adjustment)
    # This one the bottom and right edges
    draw.line((0, dimensions[1], dimensions[0], dimensions[1]), fill='white', width=thick_adjustment)
    draw.line((dimensions[0], 0, dimensions[0], dimensions[1]), fill='white', width=thick_adjustment)

    # Draw inner column edges
    for c in range(1, cols):
        y = dimensions[1]
        draw.line((c*(thickness+img_size[0]), 0, c*(thickness+img_size[0]), y), fill='white', width=thickness)

    # Draw inner row edges
    for r in range(1, rows):
        x = dimensions[0]
        draw.line((0, r*(thickness+img_size[1]), x, r*(thickness+img_size[1])), fill='white', width=thickness)

    for image in images:
        canvas.paste(image)
    return canvas
