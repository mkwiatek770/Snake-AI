import random
from typing import List
import numpy as np
from app.v2.utils import sigmoid, normalize


class NeuralNet:
    #https: // www.youtube.com / watch?v = MPmLWsHzPlU
    # Obejrzeć Coding train i zaimplementować

    def __init__(self) -> None:

        input_nodes = 6
        hidden_nodes = 2
        output_nodes = 1

        self.weights_ih = np.random.rand(hidden_nodes, input_nodes)
        self.weights_ho = np.random.rand(output_nodes, hidden_nodes)
        self.bias_h = np.random.rand(hidden_nodes, 1)
        self.bias_o = np.random.rand(output_nodes, 1)

    def feed_forward(self, vision) -> float:
        """
        Main function, takes an input vector and calculate the output by propagation through the network
        """
        normalized_data = normalize(vision)
        input_matrix = np.array(normalized_data).reshape((len(normalized_data), 1))

        hidden = np.matmul(self.weights_ih, input_matrix)
        hidden = np.add(hidden, self.bias_h)
        # activation function
        hidden = sigmoid(hidden)

        output = np.matmul(self.weights_ho, hidden)
        output = np.add(output, self.bias_o)
        # activation function
        output = sigmoid(output)

        print('Output', output)
        return float(output)
