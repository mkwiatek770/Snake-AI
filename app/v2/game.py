from typing import List

import pygame
import pygame.font

from app.v2.snake import Snake
from app.v2.population import Population
from app.v2.constants import FPS, GRID_SIZE, NODE_SIZE


class Game:
    def __init__(self):
        self.running = True
        self._display_surface = None
        self._image_surface = None
        self._font = None
        self.fps_clock = pygame.time.Clock()

    def run(self, population_size: int, generations: int):
        self.on_init()
        # initial population
        # Draw on screen loading screen informing population X is training
        population = Population(population_size)
        for generation in range(1, generations + 1):
            print(f'Generation {generation}')
            population.run_generation()
            population.calculate_fitness()
            print(f'End of generation {generation}:')
            print(f'Best fitness: {population.best_fitness}\n')
            # Here will be stop where the best snake game playing will be shown till clicking button 'Next generation'
            self.display_best_snake(population.best_agent.chromosome)
            population.crossover()

    def display_best_snake(self, chromosome: List[int]):
        print("Display best snake chromosome: ", chromosome)
        self.on_init_generation()

        snake = Snake(chromosome=chromosome, display_mode=True)
        while snake.is_alive:
            self.on_loop()
            self.on_render()
            self.fps_clock.tick(FPS)
        print("Snake is dead")
        self.on_cleanup()

    def on_init(self):
        pygame.init()
        total_size = (NODE_SIZE * GRID_SIZE, NODE_SIZE * GRID_SIZE)
        self._display_surface = pygame.display.set_mode(total_size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._font = pygame.font.Font(pygame.font.get_default_font(), 24)
        self.running = True

    def on_event(self, event) -> None:
        if event.type == pygame.QUIT:
            self.running = False

    def on_init_generation(self):
        pass

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pass


if __name__ == '__main__':
    app = Game()
    app.run(population_size=1, generations=1)
