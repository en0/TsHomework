from typing import Iterable

import pygame
import math

from objects import Ball
from player import Player


SCREEN_X = 1920
SCREEN_Y = 1080
WALL_HEIGHT = 25000

TILE_SIZE = 60
QUALITY1 = TILE_SIZE / 16
QUALITY2 = TILE_SIZE / 256
FOV_MULTIP = 1

REACH = TILE_SIZE / 1


"""
class Player:
    rect: pygame.Rect

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)

    def __init__(self, x, y):
        self.rect = pygame.Rect(0, 0, TILE_SIZE // 2, TILE_SIZE // 2)
        self.rect.center = (x, y)
"""


class GridList:
    tw: int = TILE_SIZE
    columns: int = 32
    rows: int = 0
    offset_x: int = SCREEN_X // 2
    grid: list

    def __init__(self):

        # MAP_1

        self.grid = [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 3, 1, 3, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1,
            1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1,
            1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1,
            1, 2, 0, 0, 3, 0, 0, 1, 1, 1, 3, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1,
            1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1,
            1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1,
            1, 0, 0, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 9,
            1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        ]
        self.rows = len(self.grid) // self.columns

    def get_spawn(self) -> tuple:
        index = 0
        for row in range(self.rows):
            for column in range(self.columns):
                if self.grid[index] == 2:
                    return column * self.tw + (self.tw // 2), row * self.tw + (self.tw // 2)
                index += 1

    def get_objects(self) -> Iterable[tuple]:
        index = 0
        for row in range(self.rows):
            for column in range(self.columns):
                if self.grid[index] == 4:
                    yield column * self.tw + (self.tw // 2), row * self.tw + (self.tw // 2)
                index += 1

    def get_tile(self, x, y):
        grid_x = int(math.floor(x) // TILE_SIZE)
        grid_y = int(math.floor(y) // TILE_SIZE)
        index = grid_x
        index += grid_y * SCREEN_X // TILE_SIZE
        return self.grid[index]

    def replace_tile(self, x, y, new_tile):
        grid_x = int(x // TILE_SIZE)
        grid_y = int(y // TILE_SIZE)
        index = grid_x
        index += grid_y * SCREEN_X // TILE_SIZE
        self.grid[index] = new_tile

    def draw(self, screen: pygame.Surface):
        index = 0
        for row in range(self.rows):
            y = row * self.tw
            for column in range(self.columns):
                x = column * self.tw

                if self.grid[index] == 1:
                    pygame.draw.rect(screen, (128, 128, 128), (x, y, self.tw, self.tw))

                elif self.grid[index] == 2:
                    pygame.draw.rect(screen, (0, 0, 0), (x, y, self.tw, self.tw))

                elif self.grid[index] == 3:
                    pygame.draw.rect(screen, (0, 192, 0), (x, y, self.tw, self.tw))

                elif self.grid[index] == 9:
                    pygame.draw.rect(screen, (255, 255, 0), (x, y, self.tw, self.tw))

                index += 1


def main():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    grid = GridList()
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), pygame.FULLSCREEN | pygame.HWACCEL | pygame.DOUBLEBUF)
    raster_screen = screen.copy()
    # raster_screen.set_alpha(50)
    map_screen = pygame.Surface((grid.columns * TILE_SIZE, grid.rows * TILE_SIZE))
    map_zone = pygame.Rect(0, 0, 1200, 1200)
    x_limit, y_limit = map_screen.get_size()
    px, py = grid.get_spawn()
    pdir = 0
    player = Player(px, py)

    pelf = 0

    objects = list()
    for x, y in grid.get_objects():
        obj = Ball(x, y)
        objects.append(obj)

    clock = pygame.time.Clock()
    pressed_keys = set()
    relmouse = 0, 0
    mousewheel = 0
    pygame.event.set_grab(True)
    pygame.mouse.set_visible(False)

    wall_red = 0
    wall_grn = 0
    wall_blu = 0

    running = True
    while running:
        frame_delay = clock.tick(60) / 1000
        running = not bool(pygame.event.get(pygame.QUIT))

        relmouse = 0, 0
        mousewheel = 0

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed_keys.add(event.key)
            elif event.type == pygame.KEYUP:
                pressed_keys.remove(event.key)
            if event.type == pygame.MOUSEMOTION:
                relmouse = event.rel
            if event.type == pygame.MOUSEWHEEL:
                mousewheel = event.y

        running = not pygame.K_BACKSPACE in pressed_keys and not pygame.K_ESCAPE in pressed_keys

        player.turn(relmouse[0], frame_delay)

        player.turn(
            15 if pygame.K_RIGHT in pressed_keys else
            -15 if pygame.K_LEFT in pressed_keys else
            0,
            frame_delay
        )

        player.change_turn_speed(mousewheel * 0.001)
        player.move(
            forward=pygame.K_w in pressed_keys,
            backward=pygame.K_s in pressed_keys,
            strafe_right=0,
            strafe_left=0
        )

        player.update(grid, frame_delay)

        if pygame.K_LSHIFT not in pressed_keys:
            player.move(
                forward=pygame.K_w in pressed_keys,
                backward=pygame.K_s in pressed_keys,
                strafe_right=0,
                strafe_left=0
            )

        player.update(grid, frame_delay)

        player.change_turn_speed(mousewheel * 0.001)
        player.move(
            forward=0,
            backward=0,
            strafe_right=pygame.K_d in pressed_keys,
            strafe_left=pygame.K_a in pressed_keys
        )

        player.update(grid, frame_delay)

        if pygame.K_LSHIFT not in pressed_keys:
            player.move(
                forward=0,
                backward=0,
                strafe_right=pygame.K_d in pressed_keys,
                strafe_left=pygame.K_a in pressed_keys
            )

            player.update(grid, frame_delay)

        current_x, current_y = player.get_location()
        pdir = player.get_dir()


        if pygame.K_e in pressed_keys:
            pelf = 1
            temp1 = current_x
            temp2 = current_y
            temp1 += math.cos(pdir) * REACH
            temp2 += math.sin(pdir) * REACH

            tile = grid.get_tile(current_x + math.cos(pdir) * REACH, current_y + math.sin(pdir) * REACH)

            if tile == 3:
                grid.replace_tile(temp1, temp2, 0)
            elif tile == 9:
                running = 0
                print("you win i guess")

        raster_screen.fill((0, 0, 0))
        line_x = -8
        angle: float = -0.60
        while angle <= 0.60:
            angle += 0.01
            line_x += 16
            rx = current_x
            ry = current_y
            dist = 0
            rdir: float = (angle * FOV_MULTIP + pdir)
            wall_red = 0
            ray_run = 1

            dx = math.cos(angle) * QUALITY1
            while ray_run == 1:
                rx += math.cos(rdir) * QUALITY1
                ry += math.sin(rdir) * QUALITY1
                dist += dx

                if (grid.get_tile(rx, ry)) == 1:
                    ray_run = 0
                elif (grid.get_tile(rx, ry)) == 3:
                    ray_run = 0
                elif (grid.get_tile(rx, ry)) == 9:
                    ray_run = 0

            ray_run = 1

            dx = math.cos(angle) * QUALITY2
            tile = (grid.get_tile(rx, ry))
            if tile == 1 or tile == 3 or tile == 9:
                while ray_run == 1:
                    rx -= math.cos(rdir) * QUALITY2
                    ry -= math.sin(rdir) * QUALITY2
                    dist -= dx

                    tile = (grid.get_tile(rx, ry))
                    if tile != 1 and tile != 3 and tile != 9:
                        ray_run = 0
                    else:
                        ray_run = 1

            rx += math.cos(rdir) * QUALITY2
            ry += math.sin(rdir) * QUALITY2
            dist += QUALITY2

            if (grid.get_tile(rx, ry)) == 1 or 3 or 9:
                if dist <= 0:
                    dist = 1
                center_y = SCREEN_Y / 2
                wall_height = (1 / dist) * WALL_HEIGHT

                if (grid.get_tile(rx, ry)) == 1:
                    wall_red = 0
                    wall_grn = 0
                    wall_blu = 255
                elif (grid.get_tile(rx, ry)) == 3:
                    wall_red = 0
                    wall_grn = 192
                    wall_blu = 0
                elif (grid.get_tile(rx, ry)) == 9:
                    wall_red = 255
                    wall_grn = 255
                    wall_blu = 0


                pygame.draw.line(
                    raster_screen,
                    (wall_red, wall_grn, wall_blu),
                    (line_x, center_y - wall_height),
                    (line_x, center_y + wall_height),
                    width=16
                )

        for obj in objects:
            obj.draw(raster_screen, current_x, current_y, 0 - pdir)

        map_screen.fill((0, 0, 0))
        screen.fill((0, 0, 0))
        grid.draw(map_screen)
        player.draw(map_screen)

        map_zone.center = player.get_location()
        if map_zone.left < 0:
            map_zone.left = 0
        if map_zone.top < 0:
            map_zone.top = 0
        if map_zone.right > x_limit:
            map_zone.right = x_limit
        if map_zone.bottom > y_limit:
            map_zone.bottom = y_limit

        if pygame.K_m in pressed_keys:
            _map_screen = pygame.transform.scale(map_screen.subsurface(map_zone), (600, 600))
        else:
            _map_screen = pygame.transform.scale(map_screen.subsurface(map_zone), (300, 300))

        screen.blit(raster_screen, (0, 0))
        screen.blit(_map_screen, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()
