''' This is a Very primative neural network I built to help me understand Neural networks.
    This script makes a basic NN that has two inputs and one output.
    The weights and biases are randomly set at and there is no backpropagation in this NN.
    The output is a number between 0 and 1 but this does vary as the weights and biases are random in this script
'''
import numpy as np
# Basic Neural Network with 2 input and one output.
def NeuralNetwork(x1, x2, w1, w2, b):
    # z is the weighted sum of all the inputs plus a bias.
    z = x1 * w1 + x2 * w2 + b
    return sigmoid(z)

# Sigmoid Function Used to squash the values between 0 to 1 
def sigmoid(x):
    return 1/(1 + np.exp(-x))

# Sets a random Value for the weights and Biase.
w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.randn()

# A high output means its almost certain, low output means its certain its something else middle output means it is uncertain.
print(NeuralNetwork (3, 1.5, w1, w2, b))