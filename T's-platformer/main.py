import pygame
import math


SCREEN_X = 960
SCREEN_Y = 720
TILE_SIZE = 60

PLAYER_WIDTH = TILE_SIZE // 4

SPEED = TILE_SIZE // 8
JUMP_H = 12
GRAVITY = 1
WHEEL_SPEED = TILE_SIZE // 16


class Player:
    rect: pygame.Rect

    # get collision
    @staticmethod
    def get_collisions(ex, why, grid):

        x = math.floor(ex) % 960
        y = math.floor(why) % 720
        collision = 0
        if grid.get_tile(x, y + PLAYER_WIDTH) == 1:
            collision = 1
        elif grid.get_tile(x, y - PLAYER_WIDTH) == 1:
            collision = 1
        elif grid.get_tile(x + PLAYER_WIDTH, y) == 1:
            collision = 1
        elif grid.get_tile(x - PLAYER_WIDTH, y) == 1:
            collision = 1
        elif grid.get_tile(x + PLAYER_WIDTH, y + PLAYER_WIDTH) == 1:
            collision = 1
        elif grid.get_tile(x - PLAYER_WIDTH, y - PLAYER_WIDTH) == 1:
            collision = 1
        elif grid.get_tile(x - PLAYER_WIDTH, y + PLAYER_WIDTH) == 1:
            collision = 1
        elif grid.get_tile(x + PLAYER_WIDTH, y - PLAYER_WIDTH) == 1:
            collision = 1

        if grid.get_tile(x, y + PLAYER_WIDTH) == 3:
            collision = 3
        elif grid.get_tile(x, y - PLAYER_WIDTH) == 3:
            collision = 3
        elif grid.get_tile(x + PLAYER_WIDTH, y) == 3:
            collision = 3
        elif grid.get_tile(x - PLAYER_WIDTH, y) == 3:
            collision = 3

        if grid.get_tile(x, y + PLAYER_WIDTH) == 4:
            collision = 4
        elif grid.get_tile(x, y - PLAYER_WIDTH) == 4:
            collision = 4
        elif grid.get_tile(x + PLAYER_WIDTH, y) == 4:
            collision = 4
        elif grid.get_tile(x - PLAYER_WIDTH, y) == 4:
            collision = 4
        elif grid.get_tile(x + PLAYER_WIDTH, y + PLAYER_WIDTH) == 4:
            collision = 4
        elif grid.get_tile(x - PLAYER_WIDTH, y - PLAYER_WIDTH) == 4:
            collision = 4
        elif grid.get_tile(x - PLAYER_WIDTH, y + PLAYER_WIDTH) == 4:
            collision = 4
        elif grid.get_tile(x + PLAYER_WIDTH, y - PLAYER_WIDTH) == 4:
            collision = 4

        if grid.get_tile(x, y) == 5:
            collision = 5

        if grid.get_tile(x, y + PLAYER_WIDTH) == 7:
            collision = 7
        elif grid.get_tile(x, y - PLAYER_WIDTH) == 7:
            collision = 7
        elif grid.get_tile(x + PLAYER_WIDTH, y) == 7:
            collision = 7
        elif grid.get_tile(x - PLAYER_WIDTH, y) == 7:
            collision = 7
        elif grid.get_tile(x + PLAYER_WIDTH, y + PLAYER_WIDTH) == 7:
            collision = 7
        elif grid.get_tile(x - PLAYER_WIDTH, y - PLAYER_WIDTH) == 7:
            collision = 7
        elif grid.get_tile(x - PLAYER_WIDTH, y + PLAYER_WIDTH) == 7:
            collision = 7
        elif grid.get_tile(x + PLAYER_WIDTH, y - PLAYER_WIDTH) == 7:
            collision = 7

        if grid.get_tile(x, y + PLAYER_WIDTH) == 8:
            collision = 8
        elif grid.get_tile(x, y - PLAYER_WIDTH) == 8:
            collision = 8
        elif grid.get_tile(x + PLAYER_WIDTH, y) == 8:
            collision = 8
        elif grid.get_tile(x - PLAYER_WIDTH, y) == 8:
            collision = 8
        elif grid.get_tile(x + PLAYER_WIDTH, y + PLAYER_WIDTH) == 8:
            collision = 8
        elif grid.get_tile(x - PLAYER_WIDTH, y - PLAYER_WIDTH) == 8:
            collision = 8
        elif grid.get_tile(x - PLAYER_WIDTH, y + PLAYER_WIDTH) == 8:
            collision = 8
        elif grid.get_tile(x + PLAYER_WIDTH, y - PLAYER_WIDTH) == 8:
            collision = 8

        if grid.get_tile(x, y + PLAYER_WIDTH) == 9:
            collision = 9
        elif grid.get_tile(x, y - PLAYER_WIDTH) == 9:
            collision = 9
        elif grid.get_tile(x + PLAYER_WIDTH, y) == 9:
            collision = 9
        elif grid.get_tile(x - PLAYER_WIDTH, y) == 9:
            collision = 9
        elif grid.get_tile(x + PLAYER_WIDTH, y + PLAYER_WIDTH) == 9:
            collision = 9
        elif grid.get_tile(x - PLAYER_WIDTH, y - PLAYER_WIDTH) == 9:
            collision = 9
        elif grid.get_tile(x - PLAYER_WIDTH, y + PLAYER_WIDTH) == 9:
            collision = 9
        elif grid.get_tile(x + PLAYER_WIDTH, y - PLAYER_WIDTH) == 9:
            collision = 9

        if grid.get_tile(x, y + PLAYER_WIDTH) == "(":
            collision = "("
        elif grid.get_tile(x, y - PLAYER_WIDTH) == "(":
            collision = "("
        elif grid.get_tile(x + PLAYER_WIDTH, y) == "(":
            collision = "("
        elif grid.get_tile(x - PLAYER_WIDTH, y) == "(":
            collision = "("
        elif grid.get_tile(x + PLAYER_WIDTH, y + PLAYER_WIDTH) == "(":
            collision = "("
        elif grid.get_tile(x - PLAYER_WIDTH, y - PLAYER_WIDTH) == "(":
            collision = "("
        elif grid.get_tile(x - PLAYER_WIDTH, y + PLAYER_WIDTH) == "(":
            collision = "("
        elif grid.get_tile(x + PLAYER_WIDTH, y - PLAYER_WIDTH) == "(":
            collision = "("

        return collision

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)

    def __init__(self, x, y):
        self.rect = pygame.Rect(0, 0, TILE_SIZE // 2, TILE_SIZE // 2)
        self.rect.center = (x, y)


class GridList:
    tw: int = TILE_SIZE
    stw: int = tw // 2
    columns: int = SCREEN_X // TILE_SIZE
    rows: int = SCREEN_Y // TILE_SIZE
    offset_x: int = SCREEN_X // 2
    next_grid = None
    grid: list = None

    def load_map1(self):
        self.next_grid = self.load_map2
        self.grid = [
            0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1,
            1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0,
            1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1,
            1, 4, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0,
            1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 5, 0, 1, 1,
            0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1,
            1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0,
            1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 9, 9, 0, 0, 1, 1,
            2, 0, 0, 1, 0, 6, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1,
            1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            0, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1,
        ]

    def load_map2(self):
        self.next_grid = self.load_map3
        self.grid = [
            0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1,
            0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1,
            0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1,
            0, 0, 0, 8, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            0, 0, 0, 0, 0, 1, 0, 0, 5, 0, 0, 0, 1, 3, 0, 1,
            7, 0, 0, 0, 0, 1, 1, 3, 1, 3, 1, 3, 1, 3, 0, 1,
            0, 0, 0, 0, 0, 0, 1, 0, 0, 4, 1, 3, 3, 3, 0, 1,
            0, 0, 0, 7, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 1,
            0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1,
            2, 1, 0, 0, 1, 1, 3, 0, 0, 1, 1, 0, 0, 0, 0, 1,
            0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 3, 1,
            7, 1, 1, 3, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 3, 1,
        ]

    def load_map3(self):
        self.next_grid = self.load_map4
        self.grid = [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1,
            1, 1, 0, 3, 0, 0, 0, 9, 1, 1, 0, 3, 0, 0, 0, 1,
            1, 6, 0, 3, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1,
            1, 1, 0, 3, 0, 0, 9, 9, 0, 5, 1, 1, 1, 3, 5, 1,
            1, 6, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3, 3, 0, 1,
            1, 1, 0, 1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1,
            1, 1, 3, 1, 1, 3, 3, 3, 7, 3, 0, 0, 1, 1, 1, 1,
            1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1,
            1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
            1, 3, 4, 3, 1, 1, 1, 3, 1, 3, 1, 3, 1, 0, 1, 0,
        ]

    def load_map4(self):
        self.next_grid = self.load_map1
        self.grid = [
            0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1,
            1, 1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 7, 7, 3, 7, 0, 0, 0, 0, 0, 0, 7, 1,
            1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 8, 0, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 1,
            1, 0, 0, 0, 8, 0, "*", 0, 8, 0, 0, 1, 0, 0, 0, 1,
            1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1,
            1, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1,
            4, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 1,
        ]

    def get_spawn(self) -> tuple:
        index = 0
        for row in range(self.rows):
            for column in range(self.columns):
                if self.grid[index] == 2 or self.grid[index] == "@":
                    return column * self.tw + (self.tw // 2), row * self.tw + (self.tw // 2)
                index += 1

    def get_check_pont(self) -> tuple:
        index = 0
        for row in range(self.rows):
            for column in range(self.columns):
                if self.grid[index] == 5:
                    return column * self.tw + (self.tw // 2), row * self.tw + (self.tw // 2)
                index += 1

    def get_tile(self, x, y):
        grid_x = x // TILE_SIZE
        grid_y = y // TILE_SIZE
        index = grid_x
        index += grid_y * SCREEN_X // TILE_SIZE
        return self.grid[index]

    def replace_tile(self, x, y, new_tile):
        grid_x = int(x // TILE_SIZE)
        grid_y = int(y // TILE_SIZE)
        index = grid_x
        index += grid_y * SCREEN_X // TILE_SIZE
        self.grid[index] = new_tile

    def tile_swap(self, old_tile1, new_tile1, old_tile2, new_tile2):
        index = 0
        for row in range(self.rows):
            for column in range(self.columns):
                if self.grid[index] == old_tile1:
                    self.grid[index] = new_tile1
                elif self.grid[index] == old_tile2:
                    self.grid[index] = new_tile2
                index += 1

    def draw_small(self, screen: pygame.Surface, x, y, r1, g1, b1, r2, g2, b2, r3, g3, b3, r4, g4, b4):
        pygame.draw.rect(screen, (r1, g1, b1), (x, y, self.stw, self.stw))
        pygame.draw.rect(screen, (r2, g2, b2), (x + self.stw, y, self.stw, self.stw))
        pygame.draw.rect(screen, (r3, g3, b3), (x, y + self.stw, self.stw, self.stw))
        pygame.draw.rect(screen, (r4, g4, b4), (x + self.stw, y + self.stw, self.stw, self.stw))

    def draw(self, screen: pygame.Surface, color_set, frame):
        index = 0

        t1 = 255 - abs(color_set) // 2
        t2 = 128 - abs(color_set) // 2
        t3 = 247 - abs(color_set) // 2
        t4 = 120 - abs(color_set) // 2

        for row in range(self.rows):
            y = row * self.tw
            for column in range(self.columns):
                x = column * self.tw

                if self.grid[index] == 0:
                    self.draw_small(screen, x, y, 0, 0, 0, 8, 8, 8, 8, 8, 8, 0, 0, 0)

                elif self.grid[index] == 1:
                    self.draw_small(screen, x, y, 64, 64, 64, 72, 72, 72, 72, 72, 72, 64, 64, 64)

                elif self.grid[index] == 2 or self.grid[index] == "@":
                    pygame.draw.rect(screen, (0, 196 - abs(color_set), 0), (x, y, self.tw, self.tw))

                elif self.grid[index] == 3:
                    if color_set < 0:
                        self.draw_small(screen, x, y, t1, t2, 0, t3, t4, 0, t3, t4, 0, t1, t2, 0)
                    else:
                        self.draw_small(screen, x, y, t3, t4, 0, t1, t2, 0, t1, t2, 0, t3, t4, 0)

                elif self.grid[index] == 4:
                    pygame.draw.rect(screen, (0, 255 - abs(color_set), 255 - abs(color_set)), (x, y, self.tw, self.tw))

                elif self.grid[index] == 5:
                    pygame.draw.rect(screen, (0, 96, 0), (x, y, self.tw, self.tw))

                elif self.grid[index] == 6:
                    if color_set < 0:
                        self.draw_small(screen, x, y, 64, 64, 64, 72, 72, 72, 72, 72, 72, 64, 64, 64)
                    else:
                        self.draw_small(screen, x, y, 72, 72, 72, 64, 64, 64, 64, 64, 64, 72, 72, 72)

                elif self.grid[index] == 7:
                    self.draw_small(screen, x, y, 0, 208, 0, 0, 224, 0, 72, 72, 72, 64, 64, 64)

                elif self.grid[index] == 8:
                    self.draw_small(screen, x, y, 16, 16, 16, 32, 32, 32, 32, 32, 32, 16, 16, 16)

                elif self.grid[index] == "*":
                    self.draw_small(screen, x, y, 8, 8, 8, 16, 16, 16, 16, 16, 16, 8, 8, 8)

                elif self.grid[index] == 9:
                    if frame == 0:
                        self.draw_small(screen, x, y, 32, 32, 32, 48, 48, 48, 48, 48, 48, 32, 32, 32)
                    else:
                        self.draw_small(screen, x, y, 48, 48, 48, 32, 32, 32, 32, 32, 32, 48, 48, 48)

                elif self.grid[index] == "(":
                    if frame == 1:
                        self.draw_small(screen, x, y, 32, 32, 32, 48, 48, 48, 48, 48, 48, 32, 32, 32)
                    else:
                        self.draw_small(screen, x, y, 48, 48, 48, 32, 32, 32, 32, 32, 32, 48, 48, 48)

                index += 1


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    grid = GridList()
    grid.load_map1()
    px, py = grid.get_spawn()
    spx, spy = px, py
    player = Player(px, py)
    y_speed = 0
    fall_time = 0

    color_set = 63
    tile_swap_timer = 64
    wheel_spin_timer = 16
    frame = 0

    clock = pygame.time.Clock()
    pressed_keys = set()

    running = True

    while running:
        clock.tick(60)
        running = not bool(pygame.event.get(pygame.QUIT))

        color_set -= 1
        if color_set == -64:
            color_set = 63

        tile_swap_timer -= 1
        if tile_swap_timer == 0:
            tile_swap_timer = 64
            grid.tile_swap(8, "*", "*", 8)

        wheel_spin_timer -= 1
        if wheel_spin_timer == 0:
            wheel_spin_timer = 16
            if frame == 0:
                frame = 1
            else:
                frame = 0

        current_x, current_y = player.rect.center
        y_collision = 0

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed_keys.add(event.key)
            elif event.type == pygame.KEYUP:
                pressed_keys.remove(event.key)

        if pygame.K_ESCAPE in pressed_keys or pygame.K_BACKSPACE in pressed_keys:
            running = 0

        tile = player.get_collisions(current_x, current_y + 1, grid)
        if tile == 1 or tile == 7 or tile == 8 or tile == 9 or tile == "(":
            y_speed = 0
            fall_time = 0
        else:
            y_speed -= GRAVITY
            fall_time += 1

        if pygame.K_w in pressed_keys or pygame.K_SPACE in pressed_keys:
            if fall_time == 0:
                if grid.get_tile(current_x, (TILE_SIZE // 2) + current_y) == 7:
                    y_speed = JUMP_H * 1.5
                else:
                    y_speed = JUMP_H

        current_y -= y_speed

        tile = player.get_collisions(current_x, current_y, grid)
        if tile == 1 or tile == 7 or tile == 8 or tile == 9 or tile == "(":
            if y_speed > 0:
                tile = player.get_collisions(current_x, current_y, grid)
                while tile == 1 or tile == 7 or tile == 8 or tile == 9 or tile == "(":
                    current_y += 1
                    tile = player.get_collisions(current_x, current_y, grid)
            else:
                tile = player.get_collisions(current_x, current_y, grid)
                while tile == 1 or tile == 7 or tile == 8 or tile == 9 or tile == "(":
                    current_y -= 1
                    tile = player.get_collisions(current_x, current_y, grid)
            y_collision = 1

        tile = player.get_collisions(current_x, current_y, grid)
        if tile == 3:
            current_x, current_y = spx, spy
            y_speed = 0

        player.rect.center = current_x, current_y

        tile = player.get_collisions(current_x, current_y, grid)
        if tile == 9 or tile == "(":
            if y_speed > 0:
                tile = player.get_collisions(current_x, current_y, grid)
                while tile == 9 or tile == "(":
                    current_y += 1
                    tile = player.get_collisions(current_x, current_y, grid)
            else:
                tile = player.get_collisions(current_x, current_y, grid)
                while tile == 9 or tile == "(":
                    current_y -= 1
                    tile = player.get_collisions(current_x, current_y, grid)
            y_collision = 1

        tile = player.get_collisions(current_x, current_y + 1, grid)
        if tile == 9:
            current_x += WHEEL_SPEED
            tile = player.get_collisions(current_x, current_y, grid)
            while tile == 1 or tile == 7 or tile == 8 or tile == 9 or tile == "(":
                current_x -= 1
                tile = player.get_collisions(current_x, current_y, grid)
        elif tile == "(":
            current_x -= WHEEL_SPEED
            tile = player.get_collisions(current_x, current_y, grid)
            while tile == 1 or tile == 7 or tile == 8 or tile == 9 or tile == "(":
                current_x += 1
                tile = player.get_collisions(current_x, current_y, grid)

        if pygame.K_d in pressed_keys:
            current_x += SPEED
            tile = player.get_collisions(current_x, current_y, grid)
            while tile == 1 or tile == 7 or tile == 8 or tile == 9 or tile == "(":
                current_x -= 1
                tile = player.get_collisions(current_x, current_y, grid)
        elif pygame.K_a in pressed_keys:
            current_x -= SPEED
            tile = player.get_collisions(current_x, current_y, grid)
            while tile == 1 or tile == 7 or tile == 8 or tile == 9 or tile == "(":
                current_x += 1
                tile = player.get_collisions(current_x, current_y, grid)

        if player.get_collisions(current_x, current_y, grid) == 4:
            grid.next_grid()
            px, py = grid.get_spawn()
            spx, spy = px, py
            current_x, current_y = spx, spy
            y_speed = 0

        if player.get_collisions(current_x, current_y, grid) == 5:
            if grid.get_tile(spx, spy) == "@":
                grid.replace_tile(spx, spy, 6)
            else:
                grid.replace_tile(spx, spy, 0)
            spx, spy = grid.get_check_pont()
            grid.replace_tile(current_x, current_y, 2)
            y_speed = 0

        if y_collision == 1:
            y_speed = 0

        player.rect.center = current_x % 960, current_y % 720

        screen.fill((0, 0, 0))
        grid.draw(screen, math.floor(color_set), frame)
        player.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
