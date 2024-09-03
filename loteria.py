def calc_dimensions(rows, cols, img_width, img_height, thickness=20):
    """
    :param rows: number of rows in the loteria
    :param cols: number of columns in the loteria
    :param img_width: width of each image square (in px)
    :param img_height: height of each image square (in px)
    :param thickness: thickness of lines drawn on the loteria (default 20px)
    :return: a tuple (width, height)
    """
    return img_width*cols + (cols+1)*thickness, img_height*rows + (rows+1)*thickness
