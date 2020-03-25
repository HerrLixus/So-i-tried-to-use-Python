import numpy as np
import random


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


inputs_for_test = np.array([[1, 0, 0, 0],
                            [0, 1, 1, 0],
                            [0, 0, 1, 0],
                            [1, 1, 0, 0]])

expected_outputs = np.array([[1, 0, 0, 1]]).T
weights = np.array([random.randrange(-1, 1), random.randrange(-1, 1),
                    random.randrange(-1, 1), random.randrange(-1, 1)], dtype=float)


def train(inputs, weight, expected):
    output = sigmoid(np.dot(inputs, weight))
    error = expected - output
    adj = np.dot(inputs.T, error*(output*(1-output)))
    weight = weight + adj
    return weight


def form_outputs(train_data, inp, wei, etal):
    weight = wei
    for i in range(2000):
        weight = train(train_data, weight, etal)
    out = sigmoid(np.dot(train_data, weight))
    out = list(map(lambda x: x[0], out))
    out = list(map(lambda x: 1 if x > 0.5 else 0, out))
    return out


print(form_outputs(inputs_for_test, np.array([0, 0, 0, 0]), weights, expected_outputs))
