from pygame import Surface, draw
import math


SCREEN_X = 1920
SCREEN_Y = 1080
WALL_HEIGHT = 25000


class Ball:
    x = 0
    y = 0
    rota_x = 0
    rota_y = 0

    def __init__(self, st_x, st_y):
        self.x = st_x
        self.y = st_y

    def draw(self, gfx: Surface, px, py, p_rota):
        sx = self.x - px
        sy = self.y - py
        x_dist = abs(sx - self.x)
        y_dist = abs(sy - self.y)
        dist = math.sqrt((x_dist ** 2) + (y_dist ** 2))

        if dist < 2000:
            self.rota_x = (sy * math.sin(p_rota)) + (sx * math.cos(p_rota))
            self.rota_y = (sy * math.cos(p_rota)) - (sx * math.sin(p_rota))

            rota_y = 300 / self.rota_y
            dist2 = dist * 2
            draw.circle(gfx, (255, 255, 0), (self.rota_x * rota_y, SCREEN_Y / 2), 150000 // dist2)
