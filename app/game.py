
import pygame
from app.snake import Snake
from app.food import Food


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.size = self.width, self.height = 640, 400
        self.snake = Snake()
        self.food = Food(self.width / 2, self.height / 2)

    def on_init(self) -> None:
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event) -> None:
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self) -> None:
        pass

    def on_render(self) -> None:
        self._display_surf.fill((0, 0, 0))
        pygame.draw.rect(self._display_surf, (255, 0, 0), [self.food.x, self.food.y, self.food.size, self.food.size], 0)
        # for node in self.snake.nodes:
        #     self._display_surf.blit(self._image_surf, (node.x, node.y))
        pygame.display.flip()

    def on_cleanup(self) -> None:
        pygame.quit()

    def on_execute(self) -> None:
        if self.on_init() is False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    app = App()
    app.on_execute()
