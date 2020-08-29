import random
from typing import List
import numpy as np
from app.v2.utils import sigmoid


class NeuralNet:
    #https: // www.youtube.com / watch?v = MPmLWsHzPlU
    # Obejrzeć Coding train i zaimplementować

    def __init__(self, weights: List[float] = None, biases: List[float] = None) -> None:
        self.biases = biases if biases else [random.uniform(0, 1) for _ in range(5)]
        self.weights = weights if weights else [random.uniform(0, 1) for _ in range(5)]

    def feed_forward(self, a) -> float:
        """
        Main function, takes an input vector and calculate the output by propagation through the network
        """
        for b, w in zip(self.biases, self.weights):
            # Dot product: https://en.wikipedia.org/wiki/Dot_product
            a = sigmoid(np.dot(w, a) + b)  # call activation function
        return a
