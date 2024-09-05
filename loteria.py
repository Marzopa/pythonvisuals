from PIL import Image, ImageDraw


def calc_dimensions(rows: int, cols: int, size: tuple[int, int], thickness: int = 20) -> tuple[int, int]:
    """
    :param rows: number of rows in the loteria
    :param cols: number of columns in the loteria
    :param size: a tuple (width, height) for size of each image
    :param thickness: thickness of lines drawn on the loteria (default 20px)
    :return: a tuple (width, height)
    """
    return size[0] * cols + (cols + 1) * thickness, size[1] * rows + (rows + 1) * thickness


def draw_edges(draw: ImageDraw, dimensions: tuple[int, int], img_size: tuple[int, int],
               rows: int, cols: int, thickness: int = 20) -> None:
    """
    :param draw: the draw object for a canvas
    :param dimensions: a tuple (width, height) for the entire, final image
    :param img_size: a tuple (width, height) for the size of each image
    :param rows: number of image rows
    :param cols: number of image columns
    :param thickness: thickness of lines drawn on the loteria (default 20px)
    """
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
        draw.line((c * (thickness + img_size[0]), 0, c * (thickness + img_size[0]), y), fill='white', width=thickness)

    # Draw inner row edges
    for r in range(1, rows):
        x = dimensions[0]
        draw.line((0, r * (thickness + img_size[1]), x, r * (thickness + img_size[1])), fill='white', width=thickness)


def draw_loteria(rows: int, cols: int, images: list[Image], thickness: int = 20) -> Image:
    """
    :param rows: number of rows in loteria
    :param cols: number of columns in loteria
    :param images: a list of image objects to draw loteria from, assumes all image dimensions are the same
    :param thickness: thickness of lines drawn on the loteria (default 20px)
    :return: an image of the loteria
    :raises: ValueError if number of images isn't the same as the number of squares in loteria
    :return: an image (canvas) of the loteria
    """
    if rows * cols != len(images):
        raise ValueError("Incorrect number of images")

    img_size: tuple[int, int] = images[0].size
    dimensions: tuple[int, int] = calc_dimensions(rows, cols, img_size, thickness)
    canvas = Image.new('RGB', dimensions, 'black')
    draw = ImageDraw.Draw(canvas)

    # Place images in grid place
    row_place = 0
    col_place = 0
    for image_index in range(len(images)):
        if col_place == cols:
            row_place += 1
            col_place = 0

        canvas.paste(images[image_index], ((col_place * (thickness + img_size[0]) + thickness),
                                           (row_place * (thickness + img_size[1]) + thickness)))

        col_place += 1

    draw_edges(draw, dimensions, img_size, rows, cols, thickness)

    return canvas
