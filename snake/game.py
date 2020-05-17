
import pygame


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = (640, 400)
    
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
        pass

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