# import pygame


SCREEN_X = 960
SCREEN_Y = 720
TILE_SIZE = 60
SPEED = 4


class Player:
    rect: pygame.Rect

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)

    def __init__(self, x, y):
        self.rect = pygame.Rect(0, 0, TILE_SIZE // 2, TILE_SIZE // 2)
        self.rect.center = (x, y)


class GridList:
    tw: int = TILE_SIZE
    columns: int = SCREEN_X // TILE_SIZE
    rows: int = SCREEN_Y // TILE_SIZE
    offset_x: int = SCREEN_X // 2
    grid: list

    def __init__(self):
        self.grid = [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 2, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1,
            1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1,
            1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1,
            1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1,
            1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        ]

    def get_spawn(self) -> tuple:
        index = 0
        for row in range(self.rows):
            for column in range(self.columns):
                if self.grid[index] == 2:
                    return column * self.tw + (self.tw // 2), row * self.tw + (self.tw // 2)
                index += 1

    def get_tile(self, x, y):
        grid_x = x // TILE_SIZE
        grid_y = y // TILE_SIZE
        index = grid_x
        index += grid_y * SCREEN_X // TILE_SIZE
        return self.grid[index]

    def draw(self, screen: pygame.Surface):
        index = 0
        for row in range(self.rows):
            y = row * self.tw
            for column in range(self.columns):
                x = column * self.tw

                if self.grid[index] == 1:
                    pygame.draw.rect(screen, (64, 64, 64), (x, y, self.tw, self.tw))

                elif self.grid[index] == 2:
                    pygame.draw.rect(screen, (0, 192, 0), (x, y, self.tw, self.tw))

                index += 1


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    grid = GridList()
    px, py = grid.get_spawn()
    player = Player(px, py)
    clock = pygame.time.Clock()
    pressed_keys = set()

    running = True
    while running:
        clock.tick(60)
        running = not bool(pygame.event.get(pygame.QUIT))

        current_x, current_y = player.rect.center

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed_keys.add(event.key)
            elif event.type == pygame.KEYUP:
                pressed_keys.remove(event.key)

        if pygame.K_w in pressed_keys:
            current_y -= SPEED
        elif pygame.K_s in pressed_keys:
            current_y += SPEED

        if grid.get_tile(current_x, current_y) != 1:
            player.rect.center = current_x, current_y
        else:
            current_x, current_y = player.rect.center

        if pygame.K_d in pressed_keys:
            current_x += SPEED
        elif pygame.K_a in pressed_keys:
            current_x -= SPEED

        if grid.get_tile(current_x, current_y) != 1:
            player.rect.center = current_x, current_y

        screen.fill((0, 0, 0))
        grid.draw(screen)
        player.draw(screen)
        pygame.display.flip()


# if __name__ == '__main__':
    # main()
