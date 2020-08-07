import random
from typing import List

from app.snake import Snake


class Population:

    def __init__(self, size: int = 100, agents: List[Snake] = None) -> None:
        self.size = size
        self.agents = list(agents) if agents else [Snake() for _ in range(self.size)]
        self.best_fitness = 0

    def run_generation(self):
        for agent in self.agents:
            agent.play()

    def calculate_fitness(self) -> None:
        best_fitness = 0
        for agent in self.agents:
            fitness = agent.fitness()
            if fitness > best_fitness:
                best_fitness = fitness
        self.best_fitness = best_fitness

    def crossover(self) -> None:
        new_agents: List[Snake] = []
        total_fitness = sum(agent.fitness for agent in self.agents)
        pool_of_agents = []
        for agent in self.agents:
            pool_of_agents.extend([agent] * agent.fitness * round((agent.fitness / total_fitness) * 100))
        # One-point roulette wheel selection
        for _ in range(self.size):
            father = random.choice(pool_of_agents)
            mother = random.choice(pool_of_agents)
            random_chunk_index = random.randint(0, len(father.chromosome) - 1)
            child_chromosome = father.chromosome[:random_chunk_index] + mother.chromosome[random_chunk_index:]
            # conduct mutation
            self.mutation(child_chromosome)
            child = Snake(chromosome=child_chromosome)
            new_agents.append(child)
        # replace current offspring with new one
        self.agents = new_agents

    @staticmethod
    def mutation(chromosome: List[float], bit_error_rate: float = 0.02) -> None:
        for i in range(len(chromosome)):
            if random.random() < bit_error_rate:
                chromosome[i] = round(random.uniform(0, 1), 2)


def run(generations: int = 10) -> None:
    # initial population
    population = Population()
    for generation in range(1, generations + 1):
        print(f'Generation {generation}')
        population.run_generation()
        population.calculate_fitness()
        # Here will be stop where the best snake game playing will be shown till clicking button 'Next generation'
        population.crossover()
        print(f'End of generation {generation}.:')
        print(f'Best fitness: {population.best_fitness}')
