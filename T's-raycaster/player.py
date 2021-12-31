import math
from pygame import Vector2, Surface, draw


SPEED = 2
SSPEED = 1.5


class Player:

    _location: Vector2 = Vector2(100, 100)
    _vector: Vector2 = Vector2(0, 0)
    _facing: float = 0
    _turn_speed = -0.005

    def change_turn_speed(self, value):
        self._turn_speed += value

    def get_dir(self) -> float:
        return self._facing

    def get_location(self) -> Vector2:
        return self._location

    def set_location(self, value: Vector2):
        self._location = value

    def move(self, forward: bool, backward: bool, strafe_left: bool, strafe_right: bool):
        self._vector = Vector2(0, 0)
        if forward:
            self._vector += Vector2(math.cos(self._facing), math.sin(self._facing)) * SPEED
        if backward:
            self._vector -= Vector2(math.cos(self._facing), math.sin(self._facing)) * SPEED
        if strafe_left:
            self._vector += Vector2(math.cos(self._facing - 1.57), math.sin(self._facing - 1.57)) * SSPEED
        if strafe_right:
            self._vector += Vector2(math.cos(self._facing + 1.57), math.sin(self._facing + 1.57)) * SSPEED
        # if self._vector:
            # self._vector.normalize_ip()

    def turn(self, amount: float, frame_delay):
        self._facing -= amount * self._turn_speed * 50 * frame_delay

    def draw(self, gfx: Surface):
        x, y = self._location
        x += math.cos(self._facing) * 50
        y += math.sin(self._facing) * 50

        draw.circle(gfx, (0, 0, 255), self._location, 25)
        draw.line(gfx, (255, 255, 0), self._location, (x, y), 5)

    def update(self, grid:"GridList", frame_delay):
        if self._vector:
            x, y = (self._location + (self._vector * 100 * frame_delay))
            tile = grid.get_tile(x, y)
            if tile == 3:
                tile = 1
            elif tile == 9:
                tile = 1

            if tile != 1:
                self._location = Vector2(x, y)

    def __init__(self, px, py):
        self._location = Vector2(px, py)
