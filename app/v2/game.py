from typing import List

import pygame
import pygame.font

from app.v2.snake import Snake
from app.v2.population import Population
from app.v2.node import Node
from app.v2.constants import FPS, GRID_SIZE, NODE_SIZE


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Game:
    def __init__(self):
        self.running = True
        self.screen = None
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
            self.on_end_generation(generation, population.best_fitness, population.best_agent.chromosome)
            population.crossover()

    def display_best_snake(self, chromosome: List[float]):
        print("Display best snake chromosome: ", chromosome)
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
        self.screen = pygame.display.set_mode(total_size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._font = pygame.font.Font(pygame.font.get_default_font(), 24)
        self.running = True

    def on_event(self, event) -> None:
        if event.type == pygame.QUIT:
            self.running = False

    def on_end_generation(self, generation_number: int, fitness: float, chromosome: List[float]) -> None:

        continue_button_clicked = False
        snake_simulation = False

        while not continue_button_clicked:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if mouse_x in range(20, 71) and mouse_y in range(200, 251):
                        snake_simulation = True
                        continue_button_clicked = True
                    elif mouse_x in range(160, 211) and mouse_y in range(200, 251):
                        snake_simulation = False
                        continue_button_clicked = True
            # Display summary info and buttons
            self.screen.fill(BLACK)
            self.screen.blit(self._font.render(f'Generation: {generation_number}', True, RED), (20, 20))
            self.screen.blit(self._font.render(f'Best Fitness: {fitness}', True, RED), (20, 50))
            self.screen.blit(self._font.render(f'Show simulation?', True, WHITE), (20, 160))
            pygame.draw.rect(self.screen, GREEN, (20, 200, 50, 50))
            pygame.draw.rect(self.screen, RED, (160, 200, 50, 50))
            pygame.display.update()

        if snake_simulation:
            print("Here snake simulation will be shown with possibility to restart")
            snake = Snake(chromosome=chromosome)
            while snake.is_alive:
                self.screen.fill(BLACK)
                self._draw_snake(snake.nodes)
                self._draw_food(snake.food)
                pygame.display.update()
                next_dir = snake.next_direction()
                if next_dir != snake.head.direction:
                    snake.turn_head(next_dir)
                snake.move()
                # draw grid with snake and food
                self.fps_clock.tick(FPS)


    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pass

    def _draw_snake(self, snake_nodes: List[Node]) -> None:
        for node in snake_nodes:
            x = node.x * GRID_SIZE
            y = node.y * GRID_SIZE
            pygame.draw.rect(self.screen, WHITE, (x, y, NODE_SIZE, NODE_SIZE))

    def _draw_food(self, food: Node) -> None:
        pygame.draw.rect(self.screen, RED, (food.x, food.y, NODE_SIZE, NODE_SIZE))


if __name__ == '__main__':
    app = Game()
    app.run(population_size=1, generations=3)
