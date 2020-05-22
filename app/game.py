
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
                self.snake.turn(Direction.left)
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                self.snake.turn(Direction.right)
            elif event.key in (pygame.K_w, pygame.K_UP):
                self.snake.turn(Direction.up)
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                self.snake.turn(Direction.down)

    def on_loop(self) -> None:
        self.snake.move()

    def on_render(self) -> None:
        self._display_surf.fill((0, 0, 0))
        self._draw_food()
        self._draw_snake()
        pygame.display.flip()

    def on_cleanup(self) -> None:
        pygame.quit()

    def _draw_food(self):
        pygame.draw.rect(self._display_surf, (255, 0, 0), [self.food.x, self.food.y, NODE_SIZE, NODE_SIZE], 0)

    def _draw_snake(self):
        for node in self.snake.nodes:
            pygame.draw.rect(self._display_surf, (255, 255, 255), [node.x, node.y, NODE_SIZE, NODE_SIZE], 0)


if __name__ == "__main__":
    app = App()
    app.run()
