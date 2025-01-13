import math

from PIL import ImageDraw


class Circle:
    def __init__(self, radius: float, color: tuple[int, int, int],
                 center: list[int], velocity: tuple[int, float] = None, scaling: int = 0,
                 gravity: float = 0, collisions: tuple[int, int] = (0, 0), friction: float = 1):
        """
        :param color: a tuple with RGB values indicating the color of the circle
        :param radius: the radius of the circle
        :param center: a list with x and y coordinates of the center
        :param velocity: [magnitude in px/s, direction in radians], zero by default
        :param scaling: how many pixels the radius increases per frame, zero by default
        :param gravity: gravitational force applied to the circle in pixels/frame^2, zero by default
        :param collisions: width and height of screen for collisions, zero by default
        :param friction: between zero and one (default) a multiplier by which to multiply the velocities after each frame
        """
        if friction < 0 or friction > 1:
            raise ValueError("Friction must be between 0 and 1")
        if radius <= 0:
            raise ValueError("Radius must be positive")
        if len(center) != 2:
            raise ValueError("Center must have exactly two elements")

        self.color: tuple[int, int, int] = color
        self._radius: float = radius

        self._center: list[int] = center
        if collisions != (0, 0) and (center[0] <= 0 or center[0] >= collisions[0]) or (center[1] <= 0 or center[1] >= collisions[1]):
            self._center = [collisions[0]//2, collisions[1]//2]

        self._scaling: int = scaling
        self._gravity: float = gravity
        self._collisions: tuple[int, int] = collisions
        # Number of frames the circle has been alive
        self._time: int = 0
        self._friction: float = friction
        self._horizontal_velocity: float = 0
        self._vertical_velocity: float = 0
        if velocity:
            self._horizontal_velocity = velocity[0] * math.cos(velocity[1])
            self._vertical_velocity = velocity[0] * math.sin(velocity[1])

    def get_bounding_box(self) -> tuple[int, int, int, int]:
        x1 = int(self._center[0]-self._radius)
        y1 = int(self._center[1]-self._radius)
        x2 = int(self._center[0]+self._radius)
        y2 = int(self._center[1]+self._radius)
        return x1, y1, x2, y2

    def detect_border_collision(self) -> tuple[int, ...]:
        """
        :return: [1 if no collision or -1 if collision,
        1 if no collision or 0 if collision against gravity surface or -1 if collision against non-gravity surface]
        """
        x1, y1, x2, y2 = self.get_bounding_box()
        ans: list[int] = [1, 1]
        if self._collisions == (0, 0):
            return tuple(ans)
        # Horizontal collision
        if x1 <= 0 or x2 >= self._collisions[0]:
            ans[0] = -1

        # Vertical collision
        if self._gravity == 0 and (y2 >= self._collisions[1] or y1 <= 0):
            ans[1] = -1

        if (self._gravity > 0 and y2 >= self._collisions[1]) or (self._gravity < 0 and y1 <= 0):
            ans[1] = -1

        if (self._gravity < 0 and y2 >= self._collisions[1]) or (self._gravity > 0 >= y1):
            ans[1] = 0

        return tuple(ans)

    def update_frame(self):
        if self._radius < 0:
            self._radius = 0

        self._radius += self._scaling
        border_collision: tuple[int, ...] = self.detect_border_collision()

        self._horizontal_velocity *= border_collision[0]

        # Horizontal component of displacement
        if border_collision[0] == -1:
            # Adjust the position to prevent jitter
            if self._center[0] - self._radius <= 0:
                self._center[0] = self._radius
            elif self._center[0] + self._radius >= self._collisions[0]:
                self._center[0] = self._collisions[0] - self._radius
        self._center[0] += self._horizontal_velocity

        # Vertical component of displacement
        if border_collision[1] == -1:
            # Adjust position to prevent jitter
            self._vertical_velocity *= -1
            if self._center[1] + self._radius <= 0:
                self._center[1] = self._radius
        elif border_collision[1] == 0:
            self._vertical_velocity *= -(self._friction/1.25)
            if abs(self._vertical_velocity) < 5:  # Threshold for rest
                self._vertical_velocity = 0
                # self._center[1] = self._collisions[1] - self._radius
        elif border_collision[1] == 1:
            self._vertical_velocity += self._gravity
        self._center[1] -= self._vertical_velocity

        if self._vertical_velocity == 0:
            self._horizontal_velocity *= self._friction

        self._time += 1

    def draw_on_frame(self, draw: ImageDraw) -> None:
        if self._radius > 0:
            draw.ellipse(self.get_bounding_box(), fill=self.color, outline=self.color)
