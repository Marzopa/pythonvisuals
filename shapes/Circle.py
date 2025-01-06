import math

from PIL import ImageDraw


class Circle:
    def __init__(self, radius: float, color: tuple[int, int, int],
                 center: list[int], velocity: tuple[int, float] = None, scaling: int = 0):
        """
        :param radius: the radius of the circle
        :param color: a tuple with RGB values indicating the color of the circle
        :param center: a list with x and y coordinates of the center
        :param velocity: [magnitude in px/s, direction in radians], zero by default
        :param scaling: how many pixels the radius increases per frame, zero by default
        """
        self.color: tuple[int, int, int] = color
        self._radius: float = radius
        self._center: list[int] = center
        self._velocity: tuple[int, float] = velocity[0], velocity[1] % (2*math.pi) if velocity else (0,0)
        self._scaling: int = scaling

    def get_bounding_box(self) -> tuple[int, int, int, int]:
        x1 = int(self._center[0]-self._radius)
        y1 = int(self._center[1]-self._radius)
        x2 = int(self._center[0]+self._radius)
        y2 = int(self._center[1]+self._radius)
        return x1, y1, x2, y2

    def update_frame(self):
        self._center[0] += self._velocity[0] * math.cos(self._velocity[1])
        self._center[1] -= self._velocity[0] * math.sin(self._velocity[1])

        self._radius += self._scaling

    def draw_on_frame(self, draw: ImageDraw) -> None:
        draw.ellipse(self.get_bounding_box(), fill=self.color, outline=self.color)
