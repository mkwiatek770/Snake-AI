import random

import pygame
import pygame.font

from app.snake import Snake
from app.food import Food
from app.utils import NODE_SIZE, Direction

FPS = 20
AREA_WIDTH = 640
SIDEBAR_WIDTH = 300
HEIGHT = 400


class App:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.snake = Snake((AREA_WIDTH, HEIGHT))
        self.food = Food(AREA_WIDTH // 2, HEIGHT // 2)
        self.fps_clock = pygame.time.Clock()

    def run(self) -> None:
        self.on_init()

        while self.snake.is_alive:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            self.fps_clock.tick(FPS)
        self.on_cleanup()

    def on_init(self) -> None:
        pygame.init()
        total_size = (AREA_WIDTH + SIDEBAR_WIDTH, HEIGHT)
        self._display_surf = pygame.display.set_mode(total_size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.font = pygame.font.Font(pygame.font.get_default_font(), 24)

    def on_event(self, event) -> None:
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_a, pygame.K_LEFT):
                self.snake.turn_head(Direction.left)
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                self.snake.turn_head(Direction.right)
            elif event.key in (pygame.K_w, pygame.K_UP):
                self.snake.turn_head(Direction.up)
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                self.snake.turn_head(Direction.down)

    def on_loop(self) -> None:
        self.snake.move()
        if self.snake.check_food_collision(self.food.x, self.food.y):
            self._new_food()
            self.snake.points += 1
            self.snake.eat()

    def on_render(self) -> None:
        self._display_surf.fill((0, 0, 0))
        self._draw_food()
        self._draw_snake()
        self._draw_sidebar_info()
        pygame.display.flip()

    def on_cleanup(self) -> None:
        pygame.quit()

    def _draw_food(self) -> None:
        pygame.draw.rect(self._display_surf, (255, 0, 0), [self.food.x, self.food.y, NODE_SIZE, NODE_SIZE], 0)

    def _draw_snake(self) -> None:
        for node in self.snake.nodes:
            pygame.draw.rect(self._display_surf, (255, 255, 255), [node.x, node.y, NODE_SIZE, NODE_SIZE], 0)

    def _draw_sidebar_info(self):
        pygame.draw.line(self._display_surf, (255, 255, 255), (AREA_WIDTH, 0), (AREA_WIDTH, HEIGHT))
        text_surface = self.font.render(f'Score: {self.snake.points}', True, (255, 0, 0))
        self._display_surf.blit(text_surface, dest=(AREA_WIDTH + 40, 40))

    def _new_food(self) -> None:
        snake_intersection = True
        while snake_intersection:
            new_x = random.randint(0, AREA_WIDTH // NODE_SIZE) * NODE_SIZE
            new_y = random.randint(0, HEIGHT // NODE_SIZE) * NODE_SIZE
            for node in self.snake.nodes:
                if node.x == new_x and node.y == new_y:
                    break
            else:
                snake_intersection = False
        self.food = Food(new_x, new_y)


if __name__ == "__main__":
    app = App()
    app.run()
