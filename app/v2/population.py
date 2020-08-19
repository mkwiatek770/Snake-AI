import random
from typing import List

from app.v2.snake import Snake
from app.v2.constants import BIT_ERROR_RATE


class Population:
    def __init__(self, size: int = 100) -> None:
        self.size = size
        self.agents = [Snake() for _ in range(self.size)]
        self.best_fitness = 0
        self.best_agent = None

    def run_generation(self):
        for agent in self.agents:
            agent.play()

    def calculate_fitness(self) -> None:
        best_fitness = 0
        best_agent_index = 0
        for index, agent in enumerate(self.agents):
            fitness = agent.fitness
            if fitness > best_fitness:
                best_fitness = fitness
                best_agent_index = index
        self.best_fitness = best_fitness
        self.best_agent = self.agents[best_agent_index]

    def crossover(self) -> None:
        new_agents: List[Snake] = []
        total_fitness = sum(agent.fitness for agent in self.agents)
        pool_of_agents = []
        for agent in self.agents:
            pool_of_agents.extend([agent] * round((agent.fitness / total_fitness) * 100))
        # One-point roulette wheel selection
        for _ in range(self.size):
            parent = random.choice(pool_of_agents)
            chromosome = parent.weights
            # conduct mutation
            self.mutation(chromosome)
            child = Snake(weights=chromosome, biases=parent.biases)
            new_agents.append(child)
        # replace current offspring with new one
        self.agents = new_agents

    @staticmethod
    def mutation(chromosome: List[float]) -> None:
        for i in range(len(chromosome)):
            if random.random() < BIT_ERROR_RATE:
                chromosome[i] = round(random.uniform(0, 1), 2)
