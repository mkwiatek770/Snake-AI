import random
import pygame
from app.snake import Snake
from app.food import Food
from app.utils import NODE_SIZE, Direction

FPS = 30


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.size = self.width, self.height = 640, 400
        self.snake = Snake(self.size)
        self.food = Food(self.width / 2, self.height / 2)
        self.fps_clock = pygame.time.Clock()
        self.points = 0

    def run(self) -> None:
        if self.on_init() is False:
            self._running = False

        while self.snake.is_alive:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            self.fps_clock.tick(FPS)
        self.on_cleanup()

    def on_init(self) -> None:
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

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
            self._add_points()

    def on_render(self) -> None:
        self._display_surf.fill((0, 0, 0))
        self._draw_food()
        self._draw_snake()
        pygame.display.flip()

    def on_cleanup(self) -> None:
        pygame.quit()

    def _draw_food(self) -> None:
        pygame.draw.rect(self._display_surf, (255, 0, 0), [self.food.x, self.food.y, NODE_SIZE, NODE_SIZE], 0)

    def _draw_snake(self) -> None:
        for node in self.snake.nodes:
            pygame.draw.rect(self._display_surf, (255, 255, 255), [node.x, node.y, NODE_SIZE, NODE_SIZE], 0)

    def _new_food(self) -> None:
        snake_intersection = True
        while snake_intersection:
            new_x = random.randint(0, self.width - NODE_SIZE)
            new_y = random.randint(0, self.height - NODE_SIZE)
            for node in self.snake.nodes:
                if abs(new_x - node.x) <= NODE_SIZE and abs(new_y - node.y) <= NODE_SIZE:
                    break
            else:
                snake_intersection = False
        self.food = Food(new_x, new_y)

    def _add_points(self) -> None:
        self.points += 1
        print(f"Points: {self.points}")

if __name__ == "__main__":
    app = App()
    app.run()
